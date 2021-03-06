# Generated by Django 3.2.4 on 2021-06-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_meeting_alotradingplatform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='AloTradingPlatform',
        ),
        migrations.AddField(
            model_name='meeting',
            name='AlgoTradingPlatform',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('Tradingview', 'Tradingview'), ('MT4/MT5', 'MT4/MT5'), ('Ninjatrader', 'Ninjatrader'), ('AmiBroker', 'AmiBroker'), ('Others', 'Other? Specify in comments box')], default='Python', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='Status',
            field=models.CharField(choices=[('Requested', 'Requested'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled')], default='Requested', max_length=20),
        ),
    ]
