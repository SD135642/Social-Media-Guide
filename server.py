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
        "title": "Location",
        "text": "Compare these two images. What users are *not* going to look at and follow these pages? Tap on the images to learn the answers.",
        "image1": "/static/images/img10.png",
        "image2": "/static/images/img11.png",
        "img_text1": "People from outside California are less likely to follow this page, followed by people from other countries. However, the coverage of this post is large since the Golden Gate bridge is a famous tourist attraction, so there might still be a number of followers from other countries.",
        "img_text2": "Only people who speak Korean will follow this page, meaning that the main audience will be located in South Korea or the United States. The coverage of this post is very limited."
    },
    "12":{
        "id": "12",
        "title": "Niche",
        "text": "Compare these two images. What users are going to look at these and follow these pages? Tap on the images to learn the answers.",
        "image1": "/static/images/img12.png",
        "image2": "/static/images/img14.png",
        "img_text1": "Those who own horses or are interested in horses will be interested in this kind of content. This post is not very specific and it relies on visual information rather than text, so it has wide coverage all over the world.",
        "img_text2": "Someone who has pets AND plants would be interested in this. Compared to the previous one, this topic is very specific as it is only relevant to pet owners and it relies on reading."
    },
    "13":{
        "id": "13",
        "title": "Age",
        "text": "Compare these two images. What users are going to look at these and follow these pages? Tap on the images to learn the answers.",
        "image1": "/static/images/img15.png",
        "image2": "/static/images/img13.png",
        "img_text1": "This is a reel from a cartoon, the target audience is children or parents. Adults will not compose the majority of its viewers.",
        "img_text2": "This one has sophisticated and locally-focused humor, it is aimed at adults who are familiar with New York City. Children or teenagers are less likely to engage with it."
    },
    "21":{
        "id": "21",
        "title": "Consistency",
        "text": "Look at the images and think how often and consistent your posting is compared to these plans.",
        "image1": "/static/images/img25.png",
        "image2": "/static/images/img31.png",
        "img_text1": "This is an example content plan. Especially if you are just starting to grow your social media, it is very helpful to set specific goals and deadlines for yourself.",
        "img_text2": "Which category do you fall into? Do you post less than, about the same, or more than the statistics suggest?"
    },
    "22":{
        "id": "22",
        "title": "Personal Engagement",
        "text": "Look at the examples below of what personal engagement can look like.",
        "image1": "/static/images/img16.png",
        "image2": "/static/images/img18.png",
        "img_text1": "Politely replying to DMs in a timely manner is a great example of personal engagement, and it is invaluable especially if you have your own business.",
        "img_text2": "Replying publicly in the comments under your posts is a great way to boost visibility and user engagement."
    },
    "23":{
        "id": "23",
        "title": "Catchy Content",
        "text": "Look at the pictures below. What exactly about these posts attracts attention?",
        "image1": "/static/images/img17.png",
        "image2": "/static/images/img19.png",
        "img_text1": "This creator is posting something highly questionable and controversial. By doing this, you can expect plenty of engagement, although a lot of the viewers will be disagreeing with your position. But black PR is still PR!",
        "img_text2": "This creator captures your attention by claiming they did something that sounds impossible or illogical. Stating something that doesn't make sense at first invites the user to think deeper about it, ultimately pulling him or her in."
    },
    "31":{
        "id": "31",
        "title": "Diversification",
        "text": "Compare these two images. What is the difference between how these creators utilize Instagram and present their profile page?",
        "image1": "/static/images/img23.png",
        "image2": "/static/images/img24.png",
        "img_text1": "This creator relies exclusively on their content, which is all videos. She doesn't have saved stories, a lot of information in her bio, and her content seems quite repetitive right away.",
        "img_text2": "This creator utilizes a variety of media and has a detailed bio, which shows different angles of her personality."
    },
    "32":{
        "id": "32",
        "title": "Trends and Quality",
        "text": "Compare these two images. What do you think these creators are doing very well?",
        "image1": "/static/images/img20.png",
        "image2": "/static/images/img26.png",
        "img_text1": "This creator utilizes the trends to boost their content, in particular, it uses the scene and the music from a popular movie which has thousands of fans who are all more likely to engage with, or at least see this post now.",
        "img_text2": "This creator's content is very high quality. All the pictures are crisp, rich in color, and aesthetically pleasing. The quality of your content is incredibly important, especially if your niche implies a lot of photography."
    },
    "33":{
        "id": "33",
        "title": "Collaboration",
        "text": "Compare these two images. What do you think these creators are doing very well?",
        "image1": "/static/images/img22.png",
        "image2": "/static/images/img27.png",
        "img_text1": "This creator is collaborating with Samsung, boosting his visibility and exposure drastically. Collaborating with brands whose services or products intersect with your content is highly beneficial for gaining followers as well as growing your profits from social media.",
        "img_text2": "This creator collaborates with two celebrities both with millions of fans who are now very likely to see hiw content."
    }
}

quiz_info = {
    "4":{
        "image" : "/static/images/img28.png",
    },
    "5":{
        "image" : "/static/images/img29.png"
    },
    "6":{
        "image" : "/static/images/img30.png"
    },
    "7": {
        "image" : "/static/images/img32.png"
    },
    "8": {
        "image" : "/static/images/img33.png"
    }
}


# ROUTES

@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/quiz/intro/<id>')
def quiz_intro(id=None):
    return render_template('quiz_intro.html', id = id)


@app.route('/learning/<id>')
def display_learning(id=None):
    int_id = int(id)
    global quiz_info
    if int_id == 4:
        this_quiz_info = quiz_info[id]
        return render_template('quiz.html', id = id, quiz_info=this_quiz_info)
    elif int_id == 5:
        this_quiz_info = quiz_info[id]
        return render_template('quiz1.html', id = id, quiz_info=this_quiz_info)
    elif int_id == 6:
        this_quiz_info = quiz_info[id]
        return render_template('quiz2.html', id = id, quiz_info=this_quiz_info)
    elif int_id == 7:
            this_quiz_info = quiz_info[id]
            return render_template('quiz3.html', id = id, quiz_info=this_quiz_info)
    elif int_id == 8:
            this_quiz_info = quiz_info[id]
            return render_template('quiz4.html', id = id, quiz_info=this_quiz_info)
    elif int_id < 1:
        return render_template('homepage.html')
    elif int_id > 8:
        return render_template('final.html')
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
