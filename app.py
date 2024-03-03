from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from utils import ScoreBoard
from wtforms import SelectField, SubmitField, TextAreaField
from swimmers import predefined_swimmers
from times import times_name_pair

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

@app.context_processor
def utility_processor():
    def compare_time(time1: str, time2: str) -> bool:
        if time1 == "" or time2 == "": return False
        timeint1 = int(time1.replace(':','').replace('.',''))
        timeint2 = int(time2.replace(':','').replace('.',''))
        return timeint1 < timeint2
    return dict(compare_time=compare_time)

@app.route('/', methods=('GET', 'POST'))
@app.route('/board', methods=('GET', 'POST'))
def board():
  timestandard = request.args.get('ts') or session['ts'] or 'JO_10_MALE'
  # print('timestandard=', timestandard)
  sb = ScoreBoard(time_standard=timestandard)
  sb.add_time_standards()

  swimmer_ids_text = request.args.get('id') or session['swimmers']
  for swimmer_id in swimmer_ids_text.split(','):
    sb.add_swimmer(swimmer_id)

  # df = sb.gen_report(format='dataframe')
  # records = df.to_dict(orient='records')
  # rownames = df.index.values
  # colnames = df.columns.values
  # return body + "<pre>" + str(df) + "</pre>"
  # return render_template('table.html', records=records, rownames=rownames, colnames=colnames)

  records, rownames, colnames = sb.gen_report(format="records")
  # print('records size: ', len(records))
  # print('rownames size: ', len(rownames))
  # print('colnames size: ', len(colnames))
  
  if request.method == 'POST':
    session['ts'] = request.form['timestandard']
    session['swimmers'] = request.form['hidden_swimmers']
    if len(request.form['more_swimmers']) and len(request.form['more_swimmers'].split(',')) >= 1:
       session['swimmers'] += ","+request.form['more_swimmers']
    # print('request.arg:', request.args)
    # print('session[ts]:', session['ts'])
    # print('session[swimmers]:', session['swimmers'])
    return redirect(url_for('board', **request.args))
  return render_template('table.html', records=records, rownames=rownames, colnames=colnames, form=form)


class TimestandardForm(FlaskForm):
  more_swimmers = TextAreaField('More free-text Swimmer')
  timestandard = SelectField('TimeStandards', choices=times_name_pair)
  submit = SubmitField('Go')


@app.route('/select/', methods=('GET', 'POST'))
def form():
  form = TimestandardForm()
  return render_template('form.html', predefined_swimmers=predefined_swimmers, form=form)


if  __name__ == '__main__':
  app.run(debug=True)
  # app.run()
