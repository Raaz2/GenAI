from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    availability = db.Column(db.Boolean)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        if stock>0:
            self.availability = True
        else:
            self.availability = False
