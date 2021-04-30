#ID:ajf16n Due Date: 9/24/20
#The program in this file is the
#individual work of Alexander Franco
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
import flask

app = Flask(__name__)
app.debug=True

#Declaration of multi-use variable
value=""

@app.route("/")
def home():


    return render_template("index.html")


@app.route("/showReviews/<data>", methods=['GET', 'POST'])
def showReviews(data):
    #Connect to Review database and pull username rating and reviews
    reviewsData = sqlite3.connect('reviewData.db')
    r = reviewsData.cursor()
    r.execute("SELECT  Username, Review, Rating FROM Reviews WHERE Restaurant = ?",(data,))
    values = r.fetchall()
    #Pass SQL yield to html code to be displayed
    return render_template("showReviews.html",key=data ,values=values)


@app.route("/ShowReport")
def showReport():
    reviewsData = sqlite3.connect('reviewData.db')
    r = reviewsData.cursor()
    #Pull highest rating reviews for each distinct restaurant, only if they are within the top 10 of the database
    r.execute("SELECT DISTINCT Restaurant,Food,Service,Ambience, Price, Overall FROM  Ratings GROUP BY Restaurant ORDER BY Overall  DESC LIMIT 10 ")
    values = r.fetchall()

    #Pass SQL yield to html
    return render_template("showReport.html", values=values)


@app.route("/addReview", methods=['POST','GET'])
def addReview():
    #Function to insert review filled out through html
    def insert(user, restaurant, reviewtime, rating, review, food, service, ambience, price, overall):
        reviewsData = sqlite3.connect('reviewData.db')
        r = reviewsData.cursor()
        sql = (username, restaurant, reviewtime, rating, review)
        sqll= (restaurant, food, service, ambience, price, overall)
        r.execute("INSERT INTO Reviews VALUES (?,?,?,?,?)",sql)
        r.execute("INSERT INTO Ratings VALUES (?,?,?,?,?,?)",sqll)

        reviewsData.commit()



        reviewsData.close()
    #Declare variables
    username = ''
    restaurant=''
    rating=0
    review=''
    food=0
    service=0
    ambience=0
    price=0
    overall=0
    if request.method == 'POST':
        #Pull variable values through html
        username = request.form['username']
        restaurant= request.form['restaurant']
        food = request.form['food']
        service =request.form['service']
        ambience = request.form['ambience']
        price = request.form['price']
        overall = request.form['overall']
        rating = overall;
        review =request.form['review']
        reviewtime = datetime.datetime.now()

        insert(username, restaurant, reviewtime, rating, review, food, service, ambience, price, overall)

    return render_template("addReview.html")


@app.route("/getReviews", methods=['POST', 'GET'])
def getReviews():
    #Connect to database
    reviewsData = sqlite3.connect('reviewData.db')
    r = reviewsData.cursor()
    #Pull all reviews fitting form input on html
    if request.method == 'POST':
        v= request.form['restaurant']
        reviewed = v

        return redirect(url_for('showReviews', data=v))
    return render_template("getReviews.html")

@app.route("/input", methods=['POST', 'GET'])
def input():




    return render_template('input.html')

if __name__ == "__main__":

    reviewed=''
    app.run()

