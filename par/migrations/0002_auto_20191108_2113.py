# Generated by Django 2.2.7 on 2019-11-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('par', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='par',
            name='sort_order',
            field=models.PositiveSmallIntegerField(db_index=True, default=0, editable=False, verbose_name='Sort'),
        ),
    ]
