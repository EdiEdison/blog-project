# Generated by Django 4.0.5 on 2022-07-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='put your name in here', max_length=20),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
