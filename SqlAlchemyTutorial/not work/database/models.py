from .db import db

# class for silver
class PageHits(db.Document):
    apiName = db.StringField(required=True)
    count = db.IntField()
    def to_json(self):
        return {"apiName": self.apiName,
                "count": self.count}


# class for silver
class GeneralInformation(db.Document):
    Volume = db.StringField(required=True)
    PaperName = db.StringField(required=True)
    FirstName = db.StringField(required=True)
    LastName=db.StringField(required=True)
    Country = db.StringField(required=True)
    Organization = db.StringField(required=True)
    Email = db.StringField(required=True)
    def to_json(self):
        return {"Volume": self.Volume,
                "PaperName": self.PaperName,"FirstName":self.FirstName,"LastName":self.LastName,"Country":self.Country,"Organization":self.Organization,"Email":self.Email}

