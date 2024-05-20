# Generated by Django 5.0.4 on 2024-05-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('avatar', models.ImageField(blank='True', null='True', upload_to='students/', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'ordering': ('last_name',),
            },
        ),
    ]
