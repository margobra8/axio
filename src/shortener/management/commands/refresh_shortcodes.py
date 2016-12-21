from django.core.management.base import BaseCommand, CommandError
from shortener.models import AxioURL


class Command(BaseCommand):
    help = 'Refreshes the shortcodes for all links in the db'

    # TODO: add an argument for the last x items added to the db
    # def add_arguments(self, parser):
    #     parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return AxioURL.manage.refresh_shortcodes()
