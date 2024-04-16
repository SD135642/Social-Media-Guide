from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


cafes = {
    "1":{
        "id": "1",
        "name": "Joe Coffee",
        "image": "https://joecoffeecompany.com/wp-content/uploads/2018/09/Columbia-NW-Corner-960x720.jpg",
        "description": "Matcha is savory but not too grassy. The temperature is good although it could be hotter. The mixing is usually thorough, although not always. They use unsweetened milk. The sizes are really small though, yet cost the same as big drinks anywhere else. The drawings depend greatly on the barista.",
        "price": "$5.50",
        "rating": "7",
        "similar": ["Dear Mama", "Café Blériot XI"]

    },
    "2":{
            "id": "2",
            "name": "Dear Mama",
            "image": "https://fy2019annualreport.cufo.columbia.edu/sites/default/files/styles/cu_crop/public/content/Dear%20Mama%203.JPG?itok=ZfwTuEAP",
            "description": "The matcha is just the right flavor, not too savoury or sweet. The temperature is hot. The mixing is great. They use unsweetened milk. The sizes are generous, but the prices aren't. The drawings are usually good.",
            "price": "$6.00",
            "rating": "9",
            "similar": ["Joe Coffee", "Café Blériot XI"]

    },
    "3": {
            "id": "3",
            "name": "Matto",
            "image": "https://media-cdn.tripadvisor.com/media/photo-s/28/16/34/fb/caption.jpg",
            "description": "The matcha isn't the best, although it's mixed well. They use lower quality sweetened milk. The size is small. The only decent thing is the price, which is consistently low at all franchises.",
            "price": "$3.50",
            "rating": "6",
            "similar": ["Zelma Caffee", "The Chipped Cup"]

    },
    "4": {
            "id": "4",
            "name": "The Chipped Cup",
            "image": "https://media.timeout.com/images/101826277/1372/772/image.webp",
            "description": "The matcha is good but nothing special. The drawings are simple but carefully made. They use unsweetened milk. The temperature is slightly below what it could be. The size is rather small for the price.",
            "price": "$6.50",
            "rating": "7",
            "similar": ["Zelma Caffee", "Matto"]

    },
    "5": {
            "id": "5",
            "name": "Peaky Barista",
            "image": "https://cdn.businessyab.com/assets/uploads/9d6c29e91285967faba9faa3868a7714_-united-states-new-york-new-york-county-manhattan-broadway-2680-peaky-barista-646-684-3037.jpg",
            "description": "Good matcha, a little grassy. Standard choice of milks, good temperature. An acceptable spot for matcha. Great drawings and very nice pastries to go with matcha!.",
            "price": "$6.50",
            "rating": "7",
            "similar": ["The Chipped Cup", "Lackawanna", "Zelma Caffee"]

    },
    "6": {
            "id": "6",
            "name": "Zelma Caffe",
            "image": "https://s3-media0.fl.yelpcdn.com/bphoto/y7DE3Z5Gc9GALW8quVoYgg/o.jpg",
            "description": "Good matcha. Good choices of non-diary milk. Detailed drawings. Offers great cold matcha as well! Good size and quality for the price.",
            "price": "$6.00",
            "rating": "7",
            "similar": ["Peaky Barista", "The Chipped Cup", "Lackawanna"]

    },
    "7": {
            "id": "7",
            "name": "Paris Baguette",
            "image": "https://cdn.vox-cdn.com/thumbor/Ix3GPrcnHqEYf3XUjW2mnDJhdSI=/0x0:3872x2592/1820x1213/filters:focal(1627x987:2245x1605):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/67215421/948250472.jpg.0.jpg",
            "description": "Horrible matcha, as soon as it cools down it's not even fully liquid anymore because of the amount of sugar. Too expensive for such poor quality. Difficult to assess the temperature or mixing due to how much closer to diabetes a single sip makes you. The pastries can occasionally cure the disappointment from such a bad drink.",
            "price": "$6.00",
            "rating": "1",
            "similar": ["Starbucks"]

    },
    "8": {
            "id": "8",
            "name": "Lackawanna",
            "image": "https://2.bp.blogspot.com/-zqzVcIExeF8/WiXZeW-xrKI/AAAAAAAAIKY/9yGKxzkJLwQ2XPnXs1oEv2JTdOEuFqlBwCK4BGAYYCw/s1600/IMG_7914.jpg",
            "description": "The matcha is a tiny bit too sweet, but overall good. Vast selection of non-diary milks! The price is acceptable for the generous size. The quality and the design of the cups add to the experience. Great selection of other drinks too!",
            "price": "$6.00",
            "rating": "8",
            "similar": ["Zelma Caffe", "The Chipped Cup"]

    },
    "9": {
            "id": "9",
            "name": "Café Blériot XI",
            "image": "https://s3-media0.fl.yelpcdn.com/bphoto/8z6b3DIDLiKzULdVn4AsQA/l.jpg",
            "description": "Fancy upper east size cafe with decent matcha. It's hot, mixed well, and tastes nice. Obviously overpriced. The size is also on the smaller size.",
            "price": "$7.00",
            "rating": "7",
            "similar": ["Peaky Barista", "Joe Coffee", "Dear Mama"]

    },
    "10": {
            "id": "10",
            "name": "Brooklyn Roasting Company",
            "image": "https://cdn.th3rdwave.coffee/merchants/N3gD8PYa/N3gD8PYa-lg_2x.png",
            "description": "Good matcha, but nothing special. The mixing could be more thorough. The temperature isn't high enough. There is no drawing. You can tell they focus more on coffee than teas. The size is regular.",
            "price": "5.50",
            "rating": "7",
            "similar": ["Zelma Caffe", "Peaky Barista", "The Chipped Cup"]

    }
}

# ROUTES


@app.route('/')
def homepage():
   return render_template('homepage.html', cafes=cafes)


@app.route('/view/<id>')
def display_item(id=None):
    global cafes
    cafe = cafes[id]
    return render_template('item.html', cafe=cafe)

# AJAX FUNCTIONS

# ajax for people.js
@app.route('/search/<text>')
def search(text=None):
    query = text
    results = []

    for cafe_id, cafe in cafes.items():
        if query.lower() in cafe['name'].lower():
            results.append(cafe['id'])

    return render_template('results.html', results=results, cafes=cafes, text=text)



if __name__ == '__main__':
   app.run(debug = True)
