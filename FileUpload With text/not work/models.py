###Models####
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

class GeneralInformation(db.Model):
    __tablename__ = "GeneralInformation"
    id = db.Column(db.Integer, primary_key=True)
    Volume = db.Column(db.String(20))
    PaperName = db.Column(db.String(100))
    FirstName = db.Column(db.String(20))
    LasttName = db.Column(db.String(20))
    Country = db.Column(db.String(20))
    Organization = db.Column(db.String(20))
    Email = db.Column(db.String(20))
    
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,Volume,PaperName,FirstName,LasttName,Organization,Country,Email):
        self.Volume = Volume
        self.PaperName = PaperName
        self.FirstName = FirstName
        self.LasttName = LasttName
        self.Country = Country
        self.Organization = Organization
        self.Email = Email
    def __repr__(self):
        return '' % self.id

class ContactAuthorDetails(db.Model):
    __tablename__ = "ContactAuthorDetails"
    id = db.Column(db.Integer, primary_key=True)
    GeneralInformationId=db.Column(db.Integer,ForeignKey('GeneralInformation.id'))
    Author = db.Column(db.String(20))
    EmailId = db.Column(db.String(100))
    Telephone = db.Column(db.String(20))
    KeyWords = db.Column(db.String(200))
    FilePath = db.Column(db.String(200))
    
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,GeneralInformationId,Author,EmailId,Telephone,KeyWords,FilePath):
        self.GeneralInformationId = GeneralInformationId
        self.Author = Author
        self.EmailId = EmailId
        self.Telephone = Telephone
        self.KeyWords = KeyWords
        self.FilePath = FilePath
    def __repr__(self):
        return '' % self.id



