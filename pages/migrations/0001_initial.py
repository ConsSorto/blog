# Generated by Django 4.2.5 on 2023-10-08 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='URL Amigable')),
                ('visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado en')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
            },
        ),
    ]
