# Generated by Django 3.2.5 on 2021-08-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20210809_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='notes',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
