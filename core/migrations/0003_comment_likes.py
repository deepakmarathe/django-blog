# Generated by Django 4.1.3 on 2022-11-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]