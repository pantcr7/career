from flask import Flask, render_template, jsonify,request
from database import engine, text, load_job_from_db
import os

app = Flask(__name__)

JOBS = [
    {
        'id':
        1,
        'title':
        'Senior Full Stack Developer',
        'location':
        'Remote / San Francisco',
        'type':
        'Full-time',
        'salary':
        '$120k - $180k',
        'category':
        'Engineering',
        'description':
        ("We're seeking an experienced Full Stack Developer to join our engineering team. "
         "You'll build scalable web applications using modern technologies like React, "
         "Node.js, and AWS. Strong problem-solving and collaboration skills are a must."
         )
    },
    {
        'id':
        2,
        'title':
        'Data Scientist',
        'location':
        'San Francisco, CA',
        'type':
        'Full-time',
        'salary':
        '$110k - $150k',
        'category':
        'Data Science',
        'description':
        ("Looking for a Data Scientist passionate about extracting insights from large datasets. "
         "You’ll work with Python, TensorFlow, and SQL to build predictive models and analytics dashboards."
         )
    },
    {
        'id':
        3,
        'title':
        'Data Engineer',
        'location':
        'Chicago, IL',
        'type':
        'Full-time',
        'salary':
        '$105k - $140k',
        'category':
        'Data Science',
        'description':
        ("We need a skilled Data Engineer to design and maintain our ETL pipelines. "
         "Experience with Apache Airflow, AWS Redshift, and data modeling is required."
         )
    },
    {
        'id':
        4,
        'title':
        'UI/UX Designer',
        'location':
        'Remote',
        'type':
        'Contract',
        'salary':
        '$70/hr',
        'category':
        'Design',
        'description':
        ("Join our creative team as a UI/UX Designer. You'll design user-centric interfaces, "
         "create wireframes, and collaborate closely with developers to ensure a seamless user experience."
         )
    },
    {
        'id':
        5,
        'title':
        'DevOps Engineer',
        'location':
        'New York, NY',
        'type':
        'Full-time',
        'salary':
        '$130k - $170k',
        'category':
        'Engineering',
        'description':
        ("Seeking a DevOps Engineer to automate deployments, manage CI/CD pipelines, "
         "and optimize cloud infrastructure. Proficiency in Docker, Kubernetes, and AWS is essential."
         )
    },
]


def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
            print(jobs)
        return jobs


@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='CareerHub')
    #return render_template('home.html', jobs=JOBS, company_name='CareerHub')


@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job, company_name='CareerHub')



@app.route('/apply-for-job/<id>', methods=['POST'])
def apply_for_job(id):
    form_data = request.form.to_dict()  
    add_application_to_db(id, form_data)
    #files = request.files                   # uploaded files

    return render_template('submit_success.html',applicant_name=form_data['full_name'],company_name='CareerHub')


def add_application_to_db(job_id, data):
    # Combine job_id with the data dictionary
    params = {'job_id': job_id, **data}

    query = text("""
        INSERT INTO job_applications 
        (job_id, full_name, email, phone, linkedin_url, portfolio_url, cover_letter)
        VALUES (:job_id, :full_name, :email, :phone, :linkedin_url, :portfolio_url, :cover_letter)
    """)

    # Execute query with context manager
    with engine.begin() as connection:  # engine.begin() auto-commits
        connection.execute(query, params)


if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True)

