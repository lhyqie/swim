from datetime import timedelta
from flask import Blueprint, Flask, render_template, request, session, redirect, url_for, after_this_request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from utils import ScoreBoard, ScoreCard
from wtforms import SelectField, TextAreaField
from swimmers import predefined_swimmers
from times import times_name_pair, national_times_name_pair, national_timemap
from data.schema import db, SwimmerProfile

import json
import logging
import requests
import os
import sqlite3
import urllib.parse


basedir = os.path.abspath(os.path.dirname(__file__))
main = Blueprint("main", __name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # this need to be top-level, otherwise server will throw error: RuntimeError: A secret key is required to use CSRF.

def create_app():    
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'swimmer-profile.db')
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.register_blueprint(main)

    with app.app_context():
      db.init_app(app)    


@app.context_processor
def utility_processor_compare_time():
    def compare_time(time1: str, time2: str) -> bool:
      if time1 == '' or time2 == '': return False
      try:
        timeint1 = int(time1.replace(':','').replace('.',''))
        timeint2 = int(time2.replace(':','').replace('.',''))
      except ValueError:
        return False
      return timeint1 < timeint2
    return dict(compare_time=compare_time)

@app.context_processor
def utility_processor_national_time_tool_tip():
    def national_time_tool_tip(timemap:dict, event:str) -> str:
      res = ''
      for standard, map in timemap.items():
        for event_name, time in map.items():
          if event_name == event and time:
            standard = standard.rjust(4, '\u00A0')
            res += f'{standard}:\u00A0{time}\u000A'
      return res.strip()
    return dict(national_time_tool_tip=national_time_tool_tip)


@app.route('/board', methods=('GET', 'POST'))
def board(format='records+nationaltime'):
  timestandard = request.args.get('ts') or session.get('ts') or 'JO-10-MALE'
  nationaltime = request.args.get('nt') or session.get('nt') or ''
  season = request.args.get('season') or session.get('season') or ''
  if nationaltime == '': format = 'records'
  
  logging.debug(f'request.method={request.method}')
  logging.debug(f'timestandard={timestandard}')
  logging.debug(f'nationaltime={nationaltime}')
  logging.debug(f'format={format}')

  sb = ScoreBoard(time_standard=timestandard, national_time=nationaltime)
  sb.add_time_standards()
  swimmer_param = request.args.get('id') or session.get('swimmers')
  if swimmer_param:
    for swimmer_id in swimmer_param.split(','):
      sb.add_swimmer(swimmer_id)
  if format in ('records', 'records+nationaltime'):
    records, rownames, colnames = sb.gen_report(format=format)
  elif format == 'dataframe':
    df = sb.gen_report(format=format)
    records = df.to_dict(orient='records')
    rownames = df.index.values
    colnames = df.columns.values
  else:
    raise Exception(f'format {format} is not supported')
  logging.debug(f'records size={len(records)}, rownames size={len(rownames)}, colnames size={len(colnames)}')

  if request.method == 'POST':
    session['ts'] = request.form.get('timestandard','JO-10-MALE')
    session['nt'] = request.form.get('nationaltime','')
    session['swimmers'] = request.form['hidden_swimmers']
    session['season'] = request.form.get('season','')
    if len(request.form['more_swimmers']) and len(request.form['more_swimmers'].split(',')) >= 1:
       session['swimmers'] += (',' if session['swimmers'] else '') + request.form['more_swimmers']
    logging.debug(f'request.arg: {request.args}')
    logging.debug(f"session[ts]:{session['ts']}")
    logging.debug(f"session[swimmers]:{session['swimmers']}")
    return redirect(url_for('board', **request.args))
  else:
    @after_this_request
    def do_sth_after(response):
       logging.debug('Finished. response:{response}')
       return response

    return render_template('board.html', season=season, nationaltime=nationaltime, national_timemap=national_timemap,
                           records=records, rownames=rownames, colnames=colnames, form=form)


@app.route('/card', methods=('GET', 'POST'))
def card():
  if request.method == 'POST':
    session['swimmer'] = request.form.get('swimmer_id','')
    session['nt'] = request.form.get('nationaltime','')
    session['season'] = request.form.get('season','')
    logging.debug(f'request.arg: {request.args}')
    logging.debug(f"session[swimmer]: {session['swimmer']}")
    logging.debug(f"session[nt]: {session['nt']}")
    logging.debug(f"session[season]: {session['season']}")
    return redirect(url_for('card', **request.args))
  
  swimmer = request.args.get('id') or session.get('swimmer')
  if not swimmer:
    return redirect(url_for('form2', **request.args))

  nationaltime = request.args.get('nt') or session.get('nt') or ''
  season = request.args.get('season') or session.get('season') or ''
  logging.debug(f'swimmer={swimmer}  nationaltime={nationaltime}  season={season}')
  sc = ScoreCard(swimmer, nationaltime)
  records, rownames, colnames = sc.gen_report()
  logging.debug(f'records size={len(records)}, rownames size={len(rownames)}, colnames size={len(colnames)}')  
  return render_template('card.html', season=season, nationaltime=sc.national_time, national_timemap=national_timemap,
                         records=records, rownames=rownames, colnames=colnames, form=form)


@app.route('/', methods=('GET', 'POST'))
@app.route('/search')
def index():
    return render_template("search.html")
  
@app.route('/search_results_from_db')
def search_db():
    q = request.args.get("q")
    logging.debug(f'q={q}')
    
    results = set()
    keys = q.strip().split()
    
    for key in keys:
        matches = SwimmerProfile.query.filter(SwimmerProfile.firstname.icontains(key) | SwimmerProfile.lastname.icontains(key) | SwimmerProfile.team.icontains(key))
        for match in matches:
            results.add(match)
    return render_template("search_results_from_db.html", results=sorted(results))

  
@app.route("/search_results_from_api")
def search_api():
    q = request.args.get("q")
    q = urllib.parse.quote(q)
    logging.debug(f'q={q}')
    url = f'https://api.swimstandards.com/swimmers?$search={q}&lsc=&$limit=10&$skip=0'
    logging.debug(f'fetch result from API via {url}')
    response = requests.get(url)
    entries = json.loads(response.content)['data']
    return render_template("search_results_from_api.html", results=entries)


class ScoreBoardForm(FlaskForm):
  more_swimmers = TextAreaField('More Free-text Swimmers')
  timestandard = SelectField('Championship Meet Qualifying Time Standards', choices=times_name_pair, default="JO-10-MALE")
  nationaltime = SelectField('(Optional) National Age Group Motivational Time', choices=national_times_name_pair)


class ScoreCardForm(FlaskForm):
  nationaltime = SelectField('National Age Group Motivational Time', choices=national_times_name_pair)


@app.route('/compare/', methods=('GET', 'POST'))
@app.route('/select/', methods=('GET', 'POST'))
def form():
  form = ScoreBoardForm()
  return render_template('form.html', predefined_swimmers=predefined_swimmers, form=form)


@app.route('/swimmer/', methods=('GET', 'POST'))
@app.route('/swim/', methods=('GET', 'POST'))
def form2():
  form = ScoreCardForm()
  return render_template('form2.html', predefined_swimmers=predefined_swimmers, form=form)
  

@app.route('/cache/')
@app.route('/cachedb/')
@app.route('/dbcache/')
@app.route('/db/')
@app.route('/testdb/')
def testdb():
  conn = sqlite3.connect('swimmers.db')
  conn.row_factory = sqlite3.Row
  swimmers = conn.execute('SELECT * FROM swimmers').fetchall()
  conn.close()
  return render_template('testdb.html', swimmers=swimmers)


if  __name__ == '__main__':
  port = 5000
  debug = True
  if debug:
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', 
                        level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
  
  create_app()
  app.run(debug=debug, port=port)
