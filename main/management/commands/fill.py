from django.core.management import BaseCommand

from main.models import Students


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Ivan'},
            {'last_name': 'Ivanov', 'first_name': 'Petr'},
            {'last_name': 'Semenov', 'first_name': 'Semen'},
            {'last_name': 'Maslov', 'first_name': 'Oleg'},
            {'last_name': 'Kuzmin', 'first_name': 'Luka'},
        ]
        # for item in student_list:
        #     Students.objects.create(**item)

        students_for_create = []
        for item in student_list:
            students_for_create.append(Students(**item))
        Students.objects.bulk_create(students_for_create)


