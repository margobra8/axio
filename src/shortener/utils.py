import random
import string as s


def generate_code(size=6, chars=s.ascii_lowercase + s.digits):
    """
    Generates and ascii shortcodes for url shortening purposes
    :param size: sets the size of the shortcode str (check CharField.max_value)
    :param chars: defines the characters to iterate through
    :return: code
    """
    new_code = ""
    for char in range(size):
        new_code += random.choice(chars)
    return new_code


def create_shortcode(instance, size=6):
    new_code = generate_code(size=size)
    klass = instance.__class__  # grab from the models and have duck typing inherit class
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
