from datetime import date
from flask import Flask, render_template, request
from utils import ScoreBoard

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def compare_time(time1: str, time2: str) -> bool:
        if time1 == "" or time2 == "": return False
        timeint1 = int(time1.replace(':','').replace('.',''))
        timeint2 = int(time2.replace(':','').replace('.',''))
        return timeint1 < timeint2
    return dict(compare_time=compare_time)

@app.route('/')
def show_score_board():
  # body = 'Hello World. ' + 'Today is: ' + str(date.today())

  sb = ScoreBoard(time_standard=(request.args.get('ts') or "JO_10_MALE"))
  sb.add_time_standards()
  if request.args.get('id'):
    for swimmer_id in request.args.get('id').split(','):
      sb.add_swimmer(swimmer_id)
  else:
    # sb.add_swimmer('carlos-li')
    # sb.add_swimmer('nevoh-almog')
    pass


  # df = sb.gen_report(format='dataframe')
  # records = df.to_dict(orient='records')
  # rownames = df.index.values
  # colnames = df.columns.values
  # return body + "<pre>" + str(df) + "</pre>"
  # return render_template('table.html', records=records, rownames=rownames, colnames=colnames)

  records, rownames, colnames = sb.gen_report(format="records")
  # print(rownames)
  # print(colnames)
  # print(records)
  return render_template('table.html', records=records, rownames=rownames, colnames=colnames)


if  __name__ == '__main__':
  # app.run(debug=True)
  app.run()
  