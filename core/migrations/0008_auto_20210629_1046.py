# Generated by Django 3.2.4 on 2021-06-29 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210629_0855'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CutomerQueries',
            new_name='CustomerQueries',
        ),
        migrations.AlterModelOptions(
            name='customerqueries',
            options={'verbose_name': 'Customer Query', 'verbose_name_plural': 'Customer Queries'},
        ),
    ]