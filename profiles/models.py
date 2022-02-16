from django.db import models

# Create your models here.

# модель для храрения картинки (или полного профиля пользователя)
class UserProfile(models.Model):
    # upload_to использует путь из settings.py MEDIA_ROOT.
    # Внутри созадёт вложеную папку /img
    image = models.ImageField(upload_to="img")