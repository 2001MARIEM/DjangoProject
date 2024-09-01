from mongoengine import Document, fields
import datetime

class Image(Document):
    image_id = fields.ObjectIdField(required=True)  # Stocker l'ID du fichier GridFS
    timestamp = fields.DateTimeField(default=datetime.datetime.now)


