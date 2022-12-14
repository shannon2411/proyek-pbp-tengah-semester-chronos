# Generated by Django 3.2.7 on 2021-11-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=30)),
                ('ingredient', models.TextField()),
                ('minimum_age', models.CharField(max_length=50)),
                ('doses_gap', models.TextField()),
            ],
        ),
    ]
