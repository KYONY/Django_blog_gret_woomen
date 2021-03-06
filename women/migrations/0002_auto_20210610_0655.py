# Generated by Django 3.2 on 2021-06-10 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['id'], 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.AddField(
            model_name='women',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
