from django.core.management.base import BaseCommand

from scrapper.management.scrape_utils import model_film
from scrapper.management.scrape_utils.scrapper_gather import main_gather
from scrapper.management.scrape_utils.scrapper_parse import main_parse
from scrapper.models import Film



class Command(BaseCommand):
    help = 'Start scrape-parse Function'

    def handle(self, *args, **options):
        main_parse(main_gather())
        print('finished parse')
        print(model_film)
        Film.objects.bulk_create(model_film)