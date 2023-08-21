import json

from django.core.management import BaseCommand

from catalog.models import Product
from onlinestore.settings import BASE_DIR
import codecs


class Command(BaseCommand):

    file = f'{BASE_DIR}\data.json'

    @staticmethod
    def read_json():
        with codecs.open(Command.file, 'r', encoding='utf-8', errors='ignore') as file:
            product_list = json.loads(file.read())
        return product_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        product_for_create = []
        for product in Command.read_json():
            product_for_create.append(
                Product(title=product['fields']['title'], description=product['fields']['description'],
                        product_image=product['fields']['product_image'],
                        category_id=product['fields']['category'], purchase_price=product['fields']['purchase_price'],
                        date_creation=product['fields']['date_creation'],
                        last_modified_date=product['fields']['last_modified_date']
                        ))
        Product.objects.bulk_create(product_for_create)
