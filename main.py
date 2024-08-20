from flask import Flask,render_template,request
import json
app = Flask(__name__)



#Default page
#Have to write the data into the json file to get the data 
@app.route('/')
def index():
  return render_template('index.html')

#Project page
@app.route('/projects/')
def projects():
  return render_template('projects.html')

#Resume page
@app.route('/resume/')
def resume():
  return render_template('resume.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)