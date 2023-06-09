# Generated by Django 4.1 on 2023-03-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("created", models.DateTimeField(verbose_name="date created")),
                (
                    "auther",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.auther"
                    ),
                ),
            ],
        ),
    ]
