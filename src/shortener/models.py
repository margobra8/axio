from django.db import models


class AxioURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)  # everytime the model is saved
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created

    def __str__():
        return str(self.url)

    def __unicode__():
        return str(self.url)
