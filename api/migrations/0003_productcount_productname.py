# Generated by Django 3.2.3 on 2021-05-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcount',
            name='productname',
            field=models.ManyToManyField(related_name='product', to='api.Product'),
        ),
    ]