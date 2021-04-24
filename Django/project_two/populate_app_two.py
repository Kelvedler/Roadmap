import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')
import django
django.setup()
from app_two.models import User
from faker import Faker

fake_gen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_f_name = fake_gen.first_name()
        fake_l_name = fake_gen.last_name()
        fake_email = fake_gen.email()
        fake_userdata = User.objects.get_or_create(first_name=fake_f_name, last_name=fake_l_name, email=fake_email)[0]
        fake_userdata.save()


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('population complete')