from django.db import models
from .utils import generate_code, create_shortcode


class AxioURLManager(models.Manager):
    def all_active(self, *args, **kwargs):
        qs_main = super(AxioURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def all_inactive(self, *args, **kwargs):
        qs_main = super(AxioURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs


class AxioURLController(models.Manager):
    def refresh_shortcodes(self):
        qs = AxioURL.objects.filter(id__gte=1)
        codes_changed = 0
        for entry in qs:
            entry.shortcode = create_shortcode(entry)
            entry.save()
            codes_changed = + 1
        return "Codes refreshed: {i}".format(i=codes_changed)


class AxioURL(models.Model):
    """
    This model represents an URL object handled by the axio shortening service
    """
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # se popula cada vez que el modelo se guarda
    timestamp = models.DateTimeField(auto_now_add=True)  # se popula cuando se crea el modelo
    active = models.BooleanField(default=True)

    queries = AxioURLManager()

    def save(self, *args, **kwargs):
        """
        overrides the save method to perform extra checks, changes or updates
        :return: Model.save()
        """
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)  # sets the shortcode to a randomly generated one
        super(AxioURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
