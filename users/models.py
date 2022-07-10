from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# adding an image model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='_profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
        img.save(self.image.path)

# one to one relation with the User model. cascade = user deleted, delete profile. if profile deleted, user remains.
# dunder str method: without it, printing out a profile is just going to print profile_object.
# run migrations for changes to take effect in the db
# tip: install pillow to use image fields
# the image location is passed on in the <src> tag via URL, django hashes the name of the image so another image w the same name cannot override the old image.
