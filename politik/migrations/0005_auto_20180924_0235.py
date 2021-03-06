# Generated by Django 2.0.7 on 2018-09-24 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('politik', '0004_followership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followership',
            name='politician',
        ),
        migrations.RemoveField(
            model_name='followership',
            name='user',
        ),
        migrations.AddField(
            model_name='politician',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='politician',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Followership',
        ),
    ]
