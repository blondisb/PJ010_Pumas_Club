# Generated by Django 3.2.16 on 2023-01-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mo_news',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='APP_med_news/images/'),
        ),
    ]
