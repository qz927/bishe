# Generated by Django 5.0.4 on 2024-06-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('book_publisher', models.CharField(max_length=20)),
                ('book_author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='bookinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
