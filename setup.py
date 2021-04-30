#ID:ajf16n Due Date: 9/24/20
#The program in this file is the
#individual work of Alexander Franco
import sqlite3
4strings="hello"
reviewsData = sqlite3.connect('reviewData.db')
r = reviewsData.cursor()
# Create tables with specified column names
Reviews = '''
        CREATE TABLE IF NOT EXISTS Reviews(
        "Username" Char(40),
        "Restaurant" Char(50),
        "ReviewTime" datetime,
        "Rating" float,
        "Review" Char(500)
        
        )
        '''

Ratings = '''
        CREATE TABLE IF NOT EXISTS Ratings(
        "Restaurant" Char(50),
        "Food" float,
        "Service" float,
        "Ambience" float,
        "Price" float,
        "Overall" float

        )
        '''
r.execute(Reviews)
r.execute(Ratings)
#Commit changes to database
reviewsData.commit()
reviewsData.close()

def tag_decorate(func):
    def func_wrapper(string,tag):
        return "<"+tag+">"+string+"<\\"+tag+">"
    return func_wrapper

file = open("grades.txt","r")
file2 = open("grades.xml","w")
for line in file:

    tmp=line.split("\t")
    EMPLID=tmp[0]
    NAME=tmp[1]
    GRADE=tmp[2]
    LETTER=tmp[3]
    file2.write("<line>\n")
    file2.write(tag_decorate((EMPLID,"EMPLID")))
    file2.write(tag_decorate((NAME,"NAME")))
    file2.write(tag_decorate((GRADE,"GRADE")))
    file2.write(tag_decorate((LETTER,"LETTER")))
    file2.write("<\line>\n")
