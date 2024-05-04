# Generated by Django 4.2 on 2024-05-04 02:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gonoshop_tienda", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="producto",
            name="color",
        ),
        migrations.AddField(
            model_name="producto",
            name="color",
            field=models.ManyToManyField(
                related_name="+",
                related_query_name="+",
                to="gonoshop_tienda.colorproducto",
            ),
        ),
    ]