from flask import Flask, render_template, jsonify


app = Flask(__name__,static_url_path='/static')

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Delhi, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA'
    }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
