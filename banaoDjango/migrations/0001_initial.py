# Generated by Django 4.1.7 on 2023-03-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Useryash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=15)),
                ('cpassword', models.CharField(max_length=15)),
            ],
        ),
    ]
