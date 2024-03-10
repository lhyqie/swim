from flask import Flask, render_template, request, session, redirect, url_for, after_this_request
from flask_wtf import FlaskForm
from utils import ScoreBoard
from wtforms import SelectField, SubmitField, TextAreaField
from swimmers import predefined_swimmers
from times import times_name_pair

import logging
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

@app.context_processor
def utility_processor():
    def compare_time(time1: str, time2: str) -> bool:
        if time1 == '' or time2 == '': return False
        timeint1 = int(time1.replace(':','').replace('.',''))
        timeint2 = int(time2.replace(':','').replace('.',''))
        return timeint1 < timeint2
    return dict(compare_time=compare_time)


@app.route('/', methods=('GET', 'POST'))
@app.route('/board', methods=('GET', 'POST'))
def board(format='records'):
  timestandard = request.args.get('ts') or session.get('ts') or 'JO-10-MALE'
  logging.debug(f'request.method={request.method}')
  logging.debug(f'timestandard={timestandard}')

  sb = ScoreBoard(time_standard=timestandard)
  sb.add_time_standards()
  swimmer_param = request.args.get('id') or session.get('swimmers')
  if swimmer_param:
    for swimmer_id in swimmer_param.split(','):
      sb.add_swimmer(swimmer_id)
  if format == 'records':
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
    session['swimmers'] = request.form['hidden_swimmers']
    if len(request.form['more_swimmers']) and len(request.form['more_swimmers'].split(',')) >= 1:
       session['swimmers'] += (',' if session['swimmers'] else '') + request.form['more_swimmers']
    logging.debug(f'request.arg: {request.args}')
    logging.debug(f"session[ts]:{session['ts']}")
    logging.debug(f"session[swimmers]:{session['swimmers']}")

    @after_this_request
    def do_sth_after(response):
       logging.debug('Finished. response:{response}')
       return response
    return redirect(url_for('board', **request.args))
  else:
    return render_template('board.html', records=records, rownames=rownames, colnames=colnames, form=form)


class TimestandardForm(FlaskForm):
  more_swimmers = TextAreaField('More Free-text Swimmers')
  timestandard = SelectField('Time Standards', choices=times_name_pair)
  submit = SubmitField('Go')


@app.route('/select/', methods=('GET', 'POST'))
def form():
  form = TimestandardForm()
  return render_template('form.html', predefined_swimmers=predefined_swimmers, form=form)


if  __name__ == '__main__':
  port = 5000
  debug = True
  if debug:
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', 
                        level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
  app.run(debug=debug, port=port)
