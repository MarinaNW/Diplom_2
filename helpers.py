from faker import Faker
import string
import random

class Helper:
    @staticmethod
    def generate_name():
        """Генерация случайного имени"""
        fake = Faker('ru_RU')
        return fake.name()

    @staticmethod
    def generate_email():
        """Генерация случайного email"""
        fake = Faker('ru_RU')
        return fake.email()

    @staticmethod
    def generate_password(length=12):
        """Генерация случайного пароля заданной длины"""
        letters = string.ascii_letters + string.digits
        password = ''.join(random.choice(letters) for _ in range(length))
        return password

    @staticmethod
    def extract_ingredient_ids(data):
        return [item['_id'] for item in data]

