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
        "image1": "/static/images/img1.png",
        "image2": "/static/images/img3.png",
        "image3": "/static/images/img2.png"
    },
    "2":{
        "id": "2",
        "subbranch": 2,
        "title": "Personal Engagement",
        "subtitle1": "Catchy Content",
        "subtitle2": "Consistency",
        "subtitle3": "Age",
        "image1": "/static/images/img4.png",
        "image2": "/static/images/img5.png",
        "image3": "/static/images/img6.png"
    },
    "3": {
        "id": "3",
        "subbranch": 3,
        "title": "Fostering Engagement",
        "subtitle1": "Diversification",
        "subtitle2": "Trends and Quality",
        "subtitle3": "Collaboration",
        "image1": "/static/images/img3.png",
        "image2": "",
        "image3": ""

    }
}

topics = {
    "11":{
        "id": "11",
        "title": "Tailoring Content",
        "text": "Compare these two images. What users are not going to look at and follow these pages? Tap on the images to learn the answers.",
        "image1": "",
        "image2": ""
    },
    "12":{
        "id": "12",
        "title": "Tailoring Content",
        "text": "Compare these two images. What users are not going to look at these and follow these pages? Tap on the images to learn the answers.",
        "image1": "",
        "image2": ""
    },
    "13":{
        "id": "13",
        "title": "Tailoring Content",
        "text": "Compare these two images. What users are not going to look at these and follow these pages? Tap on the images to learn the answers.",
        "image1": "",
        "image2": ""
    },
    "21":{
        "id": "21",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "22":{
        "id": "22",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "23":{
        "id": "23",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "",
        "image2": ""
    },
    "31":{
        "id": "31",
        "title": "Fostering Engagement",
        "text": "Compare these two images. What do these kinds of engagement help the creator with? What would their followers think? Tap on the images to learn the answers.",
        "image1": "",
        "image2": ""
    },
    "32":{
        "id": "32",
        "title": "Fostering Engagement",
        "text": "Compare these two images. What do these posts imply that draws the viewer's’ attention? Tap on the images to learn the answers.",
        "image1": "",
        "image2": ""
    },
    "33":{
        "id": "33",
        "title": "Fostering Engagement",
        "text": "Look at these two images. What category does your account fall into? Choose and click on the right category on the left image. Do you have a content plan similar to the image on the right?",
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

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')





if __name__ == '__main__':
   app.run(debug = True)
