from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)




@app.route("/")
def flask_tutorial():
  jobs_list = load_jobs_from_db()
  return render_template('home.html',
                        jobs=jobs_list,
                        ) 
  
@app.route("/api/jobs")
def list_jobs():
  jobs_list = load_jobs_from_db()
  return jsonify(jobs_list)

@app.route("/job/<ID>")
def show_job(ID):
    job = load_job_from_db(ID)
    if not job:
      return "Not Found", 404
    else:
      return render_template('jobpage.html', job = job)

@app.route("/job/<ID>/apply", methods=['post'])
def apply_to_job(ID):
  data = request.form
  job = load_job_from_db(ID)
  add_application_to_db(ID, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)