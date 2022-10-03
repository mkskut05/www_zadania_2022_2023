# Generated by Django 4.1.1 on 2022-10-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gracz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gracza', models.IntegerField(max_length=55)),
                ('nickname', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Postac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_postaci', models.IntegerField(max_length=55)),
                ('hp', models.IntegerField(max_length=1000)),
            ],
        ),
    ]