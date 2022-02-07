# Generated by Django 4.0.1 on 2022-02-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employers',
            options={'verbose_name': 'Працiвник', 'verbose_name_plural': 'Працiвники'},
        ),
        migrations.AlterModelOptions(
            name='insurance',
            options={'verbose_name': 'Страховка', 'verbose_name_plural': 'Страховки'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Посада', 'verbose_name_plural': 'Посади'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статуси'},
        ),
        migrations.AlterField(
            model_name='employers',
            name='description',
            field=models.TextField(verbose_name='Опис'),
        ),
    ]