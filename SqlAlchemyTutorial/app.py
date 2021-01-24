# ============================================================
# before run this file read tutorial
# 
# https://www.kite.com/blog/python/flask-sqlalchemy-tutorial/
# ===========================================================

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book


app = Flask(__name__)
#Connect to Database and create database session
# engine = create_engine('sqlite:///books-collection.db')
engine = create_engine('mysql://root:Meta@123@localhost/alchemyDb')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#landing page that will display all the books in our database
#This function operate on the Read operation.
@app.route('/')
@app.route('/books')
def showBooks():
   books = session.query(Book).all()
   return render_template("books.html", books=books)



#This will let us Create a new book and save it in our database
@app.route('/books/new/',methods=['GET','POST'])
def newBook():
   if request.method == 'POST':
       newBook = Book(title = request.form['name'], author = request.form['author'], genre = request.form['genre'])
       session.add(newBook)
       session.commit()
       print(newBook.id)
       return redirect(url_for('showBooks'))
   else:
       return render_template('newBook.html')


#This will let us Update our books and save it in our database
@app.route("/books/<int:book_id>/edit/", methods = ['GET', 'POST'])
def editBook(book_id):
   editedBook = session.query(Book).filter_by(id=book_id).one()
   if request.method == 'POST':
       if request.form['name']:
           editedBook.title = request.form['name']
           return redirect(url_for('showBooks'))
   else:
       return render_template('editBook.html', book = editedBook)

#This will let us Delete our book
@app.route('/books/<int:book_id>/delete/', methods = ['GET','POST'])
def deleteBook(book_id):
   bookToDelete = session.query(Book).filter_by(id=book_id).one()
   if request.method == 'POST':
       session.delete(bookToDelete)
       session.commit()
       return redirect(url_for('showBooks', book_id=book_id))
   else:
       return render_template('deleteBook.html',book = bookToDelete)


if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0',debug=True)