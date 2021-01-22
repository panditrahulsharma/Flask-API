# https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from sqlalchemy import Table, Column, Integer, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Meta@123@127.0.0.1:3306/product'
db = SQLAlchemy(app)

# =========================================================================================
###Models####
# =========================================================================================
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,title,productDescription,productBrand,price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
    def __repr__(self):
        return '' % self.id
# general schema
class GeneralInformation(db.Model):
    __tablename__ = "GeneralInformation"
    id = db.Column(db.Integer, primary_key=True)
    Volume = db.Column(db.String(20))
    PaperName = db.Column(db.String(100))
    FirstName = db.Column(db.String(20))
    LastName = db.Column(db.String(20))
    Country = db.Column(db.String(20))
    Organization = db.Column(db.String(20))
    Email = db.Column(db.String(20))
    
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,Volume,PaperName,FirstName,LastName,Organization,Country,Email):
        self.Volume = Volume
        self.PaperName = PaperName
        self.FirstName = FirstName
        self.LastName = LastName
        self.Country = Country
        self.Organization = Organization
        self.Email = Email
    def __repr__(self):
        return '' % self.id

# contact schema
class ContactAuthorDetails(db.Model):
    __tablename__ = "ContactAuthorDetails"
    id = db.Column(db.Integer, primary_key=True)
    # ContactId=db.Column(db.Integer)
    General_Id=db.Column(db.String(20))
    Author = db.Column(db.String(20))
    AuthorEmail = db.Column(db.String(100))
    Telephone = db.Column(db.String(20))
    KeyWords = db.Column(db.String(200))
    FilePath = db.Column(db.String(200))
    
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,General_Id,Author,AuthorEmail,Telephone,KeyWords,FilePath):
        self.General_Id = General_Id
        self.Author = Author
        self.AuthorEmail = AuthorEmail
        self.Telephone = Telephone
        self.KeyWords = KeyWords
        self.FilePath = FilePath
    def __repr__(self):
        return '' % self.id

db.create_all()

# =========================================================================================
# deserilization
# =========================================================================================

class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    productDescription = fields.String(required=True)
    productBrand = fields.String(required=True)
    price = fields.Number(required=True)


class GeneralInformationSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = GeneralInformation
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    Volume = fields.String(required=True)
    PaperName = fields.String(required=True)
    FirstName = fields.String(required=True)
    LastName = fields.String(required=True)
    Country = fields.String(required=True)
    Organization = fields.String(required=True)
    Email = fields.String(required=True)

class ContactAuthorDetailsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = ContactAuthorDetails
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    General_Id = fields.Number(dump_only=True)
    Author = fields.String(required=True)
    AuthorEmail = fields.String(required=True)
    Telephone = fields.String(required=True)
    KeyWords = fields.String(required=True)
    FilePath = fields.String(required=True)


# =========================================================================================
# deserilization
# =========================================================================================


@app.route('/products', methods = ['GET'])
def index():
    get_products = Product.query.all()
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(get_products)
    return make_response(jsonify({"product": products}))

@app.route('/paper', methods = ['POST'])
def paperPost():

    Volume=request.form['Volume']
    PaperName=request.form['PaperName']
    FirstName=request.form['FirstName']
    LastName=request.form['LastName']
    Country=request.form['Country']
    Organization=request.form['Organization']
    Email=request.form['Email']

    GeneralInformationdata = {"Volume":Volume,"PaperName":PaperName,"FirstName":FirstName,"LastName":LastName,"Country":Country,"Organization":Organization,"Email":Email}


    general_schema = GeneralInformationSchema()
    GeneralInformation = general_schema.load(GeneralInformationdata)
    GeneralInformationresult = general_schema.dump(GeneralInformation.create())
    print(GeneralInformationresult['id'])

    Authordata = {"General_Id":"12","Author":request.form['Author'],"AuthorEmail":request.form['AuthorEmail'],"Telephone":request.form['Telephone'],"KeyWords":request.form['KeyWords'],"FilePath":request.form['FilePath']}
    
    print(Authordata)

    contact_schema = ContactAuthorDetailsSchema()
    ContactAuthorDetails = contact_schema.load(Authordata)
    GeneralInformationresult = general_schema.dump(ContactAuthorDetails.create())
    # print(result['id'])

    # now fill all information in contact table


    return make_response(jsonify({"product": GeneralInformationresult}),200)




@app.route('/products', methods = ['POST'])
def create_product():
    data = request.get_json()
    print(data)
    product_schema = ProductSchema()
    product = product_schema.load(data)
    result = product_schema.dump(product.create())
    return make_response(jsonify({"product": result}),200)



if __name__ == '__main__':
    app.run(debug=True)