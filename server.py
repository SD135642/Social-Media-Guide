from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


topic_overviews = {
    "1":{
        "id": "1",
        "subbranch": 1,
        "title": "Tailoring Content",
        "subtitle1": "Location",
        "subtitle2": "Niche",
        "subtitle3": "Age",
        "image1": "",
        "image2": "",
        "image3": ""
    },
    "2":{
        "id": "2",
        "subbranch": 2,
        "title": "Quality and Outreach",
        "subtitle1": "Location",
        "subtitle2": "Niche",
        "subtitle3": "Age",
        "image1": "",
        "image2": "",
        "image3": ""

    },
    "3": {
        "id": "3",
        "subbranch": 3,
        "title": "Fostering Engagement",
        "subtitle1": "Diversification",
        "subtitle2": "Trends and Quality",
        "subtitle3": "Collaboration",
        "image1": "",
        "image2": "",
        "image3": ""

    }
}

topics = {
    "11":{
        "id": "11",
        "title": "Tailoring Content",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "2":{
        "id": "12",
        "title": "Tailoring Content",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "3":{
        "id": "13",
        "title": "Tailoring Content",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "4":{
        "id": "21",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "5":{
        "id": "22",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "6":{
        "id": "23",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "7":{
        "id": "31",
        "title": "Fostering Engagement",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "8":{
        "id": "32",
        "title": "Fostering Engagement",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "9":{
        "id": "33",
        "title": "Fostering Engagement",
        "text": "Text",
        "image1": "",
        "image2": ""
    }
}


# ROUTES


@app.route('/')
def homepage():
   return render_template('homepage.html')


@app.route('/learning/<id>')
def display_learning(id=None):
    global topic_overviews
    topic_overview = topic_overviews[id]
    return render_template('learning.html', topic_overview=topic_overview)

@app.route('/topic/<id>')
def display_topic(id=None):
    global topics
    print("Here is the id: " + id)
    topic = topics[id]
    return render_template('topic.html', topic=topic)




if __name__ == '__main__':
   app.run(debug = True)
