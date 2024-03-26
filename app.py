from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://./northwind?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)
# Define your model for the 'Invoices' view
class Invoice(db.Model):
    __tablename__ = 'Invoices'
    ShipName = db.Column(db.String(40))
    ShipAddress = db.Column(db.String(60))
    ShipCity = db.Column(db.String(15))
    ShipRegion = db.Column(db.String(15))
    ShipPostalCode = db.Column(db.String(10))
    ShipCountry = db.Column(db.String(15))
    CustomerID = db.Column(db.String(5))
    CustomerName = db.Column(db.String(40))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Salesperson = db.Column(db.String(60))
    OrderID = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime)
    RequiredDate = db.Column(db.DateTime)
    ShippedDate = db.Column(db.DateTime)
    ShipperName = db.Column(db.String(40))
    ProductID = db.Column(db.Integer)
    ProductName = db.Column(db.String(40))
    UnitPrice = db.Column(db.Float)
    Quantity = db.Column(db.Integer)
    Discount = db.Column(db.Float)
    ExtendedPrice = db.Column(db.Float)
    Freight = db.Column(db.Float)

    def serialize(self):
        return {
            'ShipName': self.ShipName,
            'ShipAddress': self.ShipAddress,
            'ShipCity': self.ShipCity,
            'ShipRegion': self.ShipRegion,
            'ShipPostalCode': self.ShipPostalCode,
            'ShipCountry': self.ShipCountry,
            'CustomerID': self.CustomerID,
            'CustomerName': self.CustomerName,
            'Address': self.Address,
            'City': self.City,
            'Region': self.Region,
            'PostalCode': self.PostalCode,
            'Country': self.Country,
            'Salesperson': self.Salesperson,
            'OrderID': self.OrderID,
            'OrderDate': self.OrderDate.isoformat() if self.OrderDate else None,
            'RequiredDate': self.RequiredDate.isoformat() if self.RequiredDate else None,
            'ShippedDate': self.ShippedDate.isoformat() if self.ShippedDate else None,
            'ShipperName': self.ShipperName,
            'ProductID': self.ProductID,
            'ProductName': self.ProductName,
            'UnitPrice': float(self.UnitPrice),
            'Quantity': self.Quantity,
            'Discount': float(self.Discount),
            'ExtendedPrice': float(self.ExtendedPrice),
            'Freight': float(self.Freight)
        }


    # Define a composite primary key constraint
    __table_args__ = (
        PrimaryKeyConstraint('OrderID', 'ProductID'),
    )

@app.route('/invoices')
def get_invoices():
    with app.app_context():
        invoices = Invoice.query.all()
        # Serialize the data using the custom serialize method before returning it
        return jsonify([invoice.serialize() for invoice in invoices])

# Define your model for the 'Customers' table
class Customer(db.Model):
    __tablename__ = 'Customers'
    CustomerID = db.Column(db.String(5), primary_key=True)
    CompanyName = db.Column(db.String(40), nullable=False)
    ContactName = db.Column(db.String(30))
    ContactTitle = db.Column(db.String(30))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))

    def serialize(self):
        return {
            'CustomerID': self.CustomerID,
            'CompanyName': self.CompanyName,
            'ContactName': self.ContactName,
            'ContactTitle': self.ContactTitle,
            'Address': self.Address,
            'City': self.City,
            'Region': self.Region,
            'PostalCode': self.PostalCode,
            'Country': self.Country,
            'Phone': self.Phone,
            'Fax': self.Fax
        }

@app.route('/customers')
def get_customers():
    with app.app_context():
        # Query all records from the 'Customers' table
        customers = Customer.query.all()
        # Serialize the data using the custom serialize method before returning it
        return jsonify([customer.serialize() for customer in customers])


if __name__ == '__main__':
    app.run(debug=True)
