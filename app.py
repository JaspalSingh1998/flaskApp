from flask import Flask, request, render_template
from flask_pymongo import PyMongo
import urllib.request, json

app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://goldy:goldy@cluster0.d92wapv.mongodb.net/myFirstDb?retryWrites=true&w=majority"

# Setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
def index():
  url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/barrie?unitGroup=us&key=CD9QP9TXZ7RC7ZC8PRVCGJFUA&contentType=json"
  response = urllib.request.urlopen(url)
  data = response.read()
  dict = json.loads(data)
  print(dict["address"])
	# return render_template('index.html') 

@app.route('/piechart')
def piechart():
  newdata = db.todos.find_one()
  print(newdata)
  data = { "Task" : "Hours per Day",  "Work" :11, "Eat" : 2, "Commute" : 2, "Watch TV" : 2}
  return render_template('pie-chart.html', data=data) 


if __name__ == "__main__":
  app.run()