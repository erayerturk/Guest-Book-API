# Generated by Django 5.0.3 on 2024-03-16 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("entry", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entry",
            options={"ordering": ["-created_date"]},
        ),
    ]