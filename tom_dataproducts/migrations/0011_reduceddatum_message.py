# Generated by Django 4.1 on 2022-10-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_alerts', '0005_alertstreammessage'),
        ('tom_dataproducts', '0010_manual_20210305_fix_spectroscopy'),
    ]

    operations = [
        migrations.AddField(
            model_name='reduceddatum',
            name='message',
            field=models.ManyToManyField(to='tom_alerts.alertstreammessage'),
        ),
    ]
