# Generated by Django 4.2.1 on 2023-06-05 20:27

import django.core.validators
from django.db import migrations, models
import goplaces.models


class Migration(migrations.Migration):
    dependencies = [
        ("goplaces", "0002_alter_link_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="keyword",
            field=models.CharField(
                max_length=32,
                validators=[
                    django.core.validators.MinLengthValidator(1),
                    goplaces.models.validate_keyword,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="link",
            name="url",
            field=models.URLField(verbose_name="Link"),
        ),
    ]
