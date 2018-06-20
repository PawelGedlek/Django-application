# Generated by Django 2.0.6 on 2018-06-20 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20180620_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='price',
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default='1900'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='films.Category'),
        ),
    ]