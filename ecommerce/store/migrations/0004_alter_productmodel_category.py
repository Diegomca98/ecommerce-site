# Generated by Django 3.2 on 2021-04-23 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productmodel_has_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(max_length=200, verbose_name='Brand'),
        ),
    ]