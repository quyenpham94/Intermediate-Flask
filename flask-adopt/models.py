
from flask_sqlalchemy import SQLAlchemy

GENERIC_IMG = "https://png.pngtree.com/png-clipart/20200701/original/pngtree-cat-default-avatar-png-image_5416936.jpg"

db = SQLAlchemy()

class Pet(db.Model):
    """Adoptable pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def img_url(self):
        """Return image for pet -- bespoke or generic."""
        
        return self.photo_url or GENERIC_IMG

def connect_db(app):
    db.app = app
    db.init_app(app)

    