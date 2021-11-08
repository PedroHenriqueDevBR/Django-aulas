from django.db import models
import uuid
import os

def upload_image_formater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)

    def has_image(self):
        return self.image != None and self.image != ''

    def remove_image(self):
        if self.has_image():
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        self.image = None

    def delete(self):
        self.remove_image()
        super().delete()

