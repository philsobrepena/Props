# Generated by Django 4.2.1 on 2023-06-15 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprops', '0002_rename_name_props_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='props',
            name='item',
            field=models.CharField(choices=[('1', '123'), ('2', '234')], max_length=1),
        ),
    ]
