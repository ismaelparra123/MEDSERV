# Generated by Django 3.2.19 on 2023-06-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre_instructor')),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=12, verbose_name='fono_instructor')),
            ],
        ),
    ]
