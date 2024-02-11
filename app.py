from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Petaling Jaya, Selangor',
    'salary': 'RM2,400'
  },
  {
    'id': 2,
    'title': 'Software Developer',
    'location': 'Petaling Jaya, Selangor',
    'salary': 'RM3,500'
  },
  {
    'id': 3,
    'title': 'Game Developer',
    'location': 'Remote',
    'salary': 'USD2,500'
  },
  {
    'id': 4,
    'title': '3D Animator',
    'location': 'Remote',
    'salary': 'AUS3,000'
  },
]

@app.route("/")

def index():
  return render_template("home.html", jobs=JOBS, companyname = 'Job Hub')

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
