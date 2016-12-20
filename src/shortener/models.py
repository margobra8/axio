from django.db import models


class AxioURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)  # se genera cada vez que el modelo se guarda
    timestamp = models.DateTimeField(auto_now_add=True)  # se genera cuando se crea el modelo

    def save(self, *args, **kwargs):
        print("save method override worked")
        super(AxioURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
