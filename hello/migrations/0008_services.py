# Generated by Django 3.0.5 on 2020-04-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_remove_destination_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.TextField(blank=True, null=True)),
                ('subcat', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
