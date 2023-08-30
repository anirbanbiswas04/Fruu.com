from io import BytesIO
from PIL import Image
from django.core.files import File


def img_compress(image, size=(300, 200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO() 
    img.save(thumb_io, 'JPEG', quality=70) 
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail
