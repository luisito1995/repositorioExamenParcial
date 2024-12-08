# Generated by Django 5.1.3 on 2024-12-07 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloArticulo', models.CharField(max_length=200)),
                ('contenidoArticulo', models.TextField()),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wikiApp.tema')),
            ],
        ),
    ]