# Generated by Django 4.1.3 on 2022-11-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_comment_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]