from django.core.management import BaseCommand
from products.models import Category, Subcategory, Product, SubcategoryImage, CategoryImage, ProductImage


class Command(BaseCommand):
    def create_product_with_category_and_subcategory(self, category_title, subcategory_title, product_data):
        category, _ = Category.objects.get_or_create(title=category_title)
        CategoryImage.objects.create(category=category)

        subcategory, created = Subcategory.objects.get_or_create(title=subcategory_title, category=category)
        SubcategoryImage.objects.create(subcategory=subcategory)

        if created:
            category.subcategories.add(subcategory)
        product = Product.objects.create(category=category, subcategory=subcategory, **product_data)
        ProductImage.objects.create(product=product)

        return product

    def handle(self, *args, **options):
        products_data = [
            {
                'category_title': 'Комплектующие для ПК',
                'subcategory_title': 'Процессоры',
                'product_data': {
                    'price': 300.0,
                    'count': 10,
                    'title': 'Процессор AMD',
                    'limited': True,
                    'description': 'This is an example product.',
                    'freeDelivery': False,
                    'fullDescription': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                                       "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                                       "when an unknown printer took a galley of type and scrambled it to make a type "
                                       "specimen book. It has survived not only five centuries, but also the leap "
                                       "into electronic typesetting, remaining essentially unchanged.",
                }
            },
            {
                'category_title': 'Жёсткие диски',
                'subcategory_title': 'SSD',
                'product_data': {
                    'price': 150.0,
                    'count': 10,
                    'title': 'SSD Disk',
                    'description': 'This is an example product.',
                    'freeDelivery': True,
                    'fullDescription': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                                       "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                                       "when an unknown printer took a galley of type and scrambled it to make a "
                                       "type specimen book. It has survived not only five centuries, but also the "
                                       "leap into electronic typesetting, remaining essentially unchanged.",
                }
            },
            {
                'category_title': 'Оргтехника',
                'subcategory_title': 'Принтеры',
                'product_data': {
                    'price': 80.0,
                    'count': 10,
                    'title': 'Принтер Canon',
                    'description': 'This is an example product.',
                    'fullDescription': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                                       "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                                       "when an unknown printer took a galley of type and scrambled it to make a type "
                                       "specimen book. It has survived not only five centuries, but also the leap "
                                       "into electronic typesetting, remaining essentially unchanged.",
                }
            }
        ]

        for product_info in products_data:
            category_title = product_info['category_title']
            subcategory_title = product_info['subcategory_title']
            product_data = product_info['product_data']
            self.create_product_with_category_and_subcategory(category_title, subcategory_title, product_data)

        self.stdout.write(self.style.SUCCESS('Successfully created products'))
