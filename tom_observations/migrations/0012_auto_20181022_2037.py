# Generated by Django 2.0.6 on 2018-10-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_observations', '0011_auto_20181019_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataproduct',
            name='product_id',
            field=models.CharField(blank=True, max_length=2000, null=True, unique=True),
        ),
    ]