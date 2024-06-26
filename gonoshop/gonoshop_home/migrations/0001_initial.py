# Generated by Django 4.2 on 2024-05-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ImagenCarrusel",
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
                ("titulo", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(max_length=50, verbose_name="Descripción"),
                ),
                ("imagen", models.ImageField(upload_to="home/carrusel/%Y/%m/%d/%H")),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "visible",
                    models.BooleanField(
                        default=False, verbose_name="Mostrar en la Pagina Web"
                    ),
                ),
            ],
            options={
                "verbose_name": "Imagen Carrusel",
                "verbose_name_plural": "Imágenes Carrusel",
            },
        ),
    ]
