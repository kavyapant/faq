# Generated by Django 3.0.5 on 2020-04-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_auto_20200425_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subcategory',
            field=models.TextField(blank=True, choices=[('Web Development', 'Web Development')], null=True),
        ),
    ]
