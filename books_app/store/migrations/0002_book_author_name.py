# Generated by Django 5.0 on 2023-12-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Author_name', max_length=255),
            preserve_default=False,
        ),
    ]
