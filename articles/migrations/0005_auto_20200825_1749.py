# Generated by Django 3.1 on 2020-08-25 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200825_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.theme', verbose_name='Тематический раздел'),
        ),
    ]
