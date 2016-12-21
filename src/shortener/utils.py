import random
import string as s

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)


def generate_code(size=SHORTCODE_MIN, chars=s.ascii_lowercase + s.digits):
    """
    Genera shortcodes ASCII para el acortamiento de las url
    :param size: sets the size of the shortcode str (check CharField.max_value)
    :param chars: defines the characters to iterate through
    :return: code
    """
    new_code = ""
    for char in range(size):
        new_code += random.choice(chars)
    return new_code


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = generate_code(size=size)
    klass = instance.__class__  # grab from the models and have duck typing inherit class
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
