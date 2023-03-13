from .models import Blog, Category
from faker import Faker

def run():
    fake = Faker(['en-US'])
    categorys=(
        'Sports',
        'Technology',
        'Science',
        'Politics',
    )

    for category in categorys:
        new_category = Category.objects.create(name = category)
        for _ in range(10):
            Blog.objects.create(category = new_category, title = fake.name(), content = fake.text())

    print('Finished')