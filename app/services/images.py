from app.models import Image
from app import db

def create_image(user_id, image_url):
    image = Image(user_id=user_id, image_url=image_url)
    db.session.add(image)
    db.session.commit()
    return image

def get_images_by_user(user_id):
    return Image.query.filter_by(user_id=user_id).all()
