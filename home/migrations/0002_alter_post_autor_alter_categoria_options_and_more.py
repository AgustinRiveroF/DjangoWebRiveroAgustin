# Generated by Django 5.1.6 on 2025-03-05 22:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Publicación', 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(default='Sin subtitulo', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('biografia', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='home_perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
    ]
