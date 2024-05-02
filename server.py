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
        "title": "Quality and Outreach",
        "subtitle1": "Consistency",
        "subtitle2": "Personal Engagement",
        "subtitle3": "Catchy Content",
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
        "image1": "/static/images/img7.png",
        "image2": "/static/images/img8.png",
        "image3": "/static/images/img9.png"

    }
}

topics = {
    "11":{
        "id": "11",
        "title": "Tailoring Content",
        "text": "Compare these two images. What users are not going to look at and follow these pages? Tap on the images to learn the answers.",
        "image1": "/static/images/img10.png",
        "image2": "/static/images/img11.png",
        "img_text1": "People from outside California are less likely to follow this page, followed by people from other countries. However, the coverage of this post is large since the Golden Gate bridge is a famous tourist attraction, so there might still be a number of followers from other countries.",
        "img_text2": "Only people who speak Korean will follow this page, meaning that the main audience will be located in South Korea or the United States. The coverage of this post is very limited."
    },
    "12":{
        "id": "12",
        "title": "Tailoring Content",
        "text": "Compare these two images. What users are not going to look at these and follow these pages? Tap on the images to learn the answers.",
        "image1": "/static/images/img12.png",
        "image2": "/static/images/img15.png",
        "img_text1": "",
        "img_text2": ""
    },
    "13":{
        "id": "13",
        "title": "Tailoring Content",
        "text": "Compare these two images. What users are not going to look at these and follow these pages? Tap on the images to learn the answers.",
        "image1": "/static/images/img14.png",
        "image2": "/static/images/img13.png",
        "img_text1": "",
        "img_text2": ""
    },
    "21":{
        "id": "21",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "/static/images/img16.png",
        "image2": "/static/images/img18.png",
    },
    "22":{
        "id": "22",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "/static/images/img17.png",
        "image2": "/static/images/img19.png"
    },
    "23":{
        "id": "23",
        "title": "Quality and Outreach",
        "text": "Text",
        "image1": "/static/images/img17.png",
        "image2": "/static/images/img17.png"
    },
    "31":{
        "id": "31",
        "title": "Fostering Engagement",
        "text": "Compare these two images. What do these kinds of engagement help the creator with? What would their followers think? Tap on the images to learn the answers.",
        "image1": "/static/images/img16.png",
        "image2": "/static/images/img17.png"
    },
    "32":{
        "id": "32",
        "title": "Fostering Engagement",
        "text": "Compare these two images. What do these posts imply that draws the viewer's’ attention? Tap on the images to learn the answers.",
        "image1": "/static/images/img18.png",
        "image2": "/static/images/img19.png"
    },
    "33":{
        "id": "33",
        "title": "Fostering Engagement",
        "text": "Look at these two images. What category does your account fall into? Choose and click on the right category on the left image. Do you have a content plan similar to the image on the right?",
        "image1": "/static/images/img13.png",
        "image2": "/static/images/img13.png"
    }
}

quiz_info = {
    "4":{
        "image" : "",
    },
    "5":{
        "image" : "",
    },
    "6":{
        "image" : ""
    },
    "7": {
        "name": "",
        "bio": "",
        "profile_pic": "",
        "channel1": "",
        "channel2": "",
        "channel3": "",
        "channel4": "",
        "channel5": ""
    }
}


# ROUTES

@app.route('/')
def homepage():
   return render_template('homepage.html')


@app.route('/learning/<id>')
def display_learning(id=None):
    int_id = int(id)
    if int_id > 3:
        global quiz_info
        this_quiz_info = quiz_info[id]
        return render_template('quiz.html', id = id, quiz_info=this_quiz_info)
    elif int_id < 1:
        return render_template('homepage.html')
    else:
        global topic_overviews
        topic_overview = topic_overviews[id]
        return render_template('learning.html', topic_overview=topic_overview, id=id)


@app.route('/final')
def final_page():
    return render_template('final.html')


@app.route('/topic/<id>')
def display_topic(id=None):
    global topics
    topic = topics[id]
    return render_template('topic.html', topic=topic, id=id)

@app.route('/quiz/<id>')
def quiz(id=None):
    global quiz_info
    this_quiz_info = quiz_info[id]
    return render_template('quiz.html', id = id, quiz_info=this_quiz_info)



if __name__ == '__main__':
   app.run(debug = True, port=5001)
