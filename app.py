from flask import Flask, render_template, jsonify
from llm import resp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San francisco, USA',
    'salary': '$ 120,000'
}]


@app.route("/")
def hello_world():
  # print(resp("who you are?"))
  return render_template('home.html', jobs=JOBS, company_name='Rishabh')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route('/api/data', methods=['POST'])
def receive_data():
  print("hellow")
  data = request.json  # Assuming the data is sent in JSON format
  # Process the data in Python
  # ...

  # Respond with data (optional)
  response_data = {'result': 'Data received successfully'}
  print(data)
  # data = data + "kumar"
  data = resp(data)
  return jsonify(data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
