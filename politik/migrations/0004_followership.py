# Generated by Django 2.0.7 on 2018-09-24 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('politik', '0003_auto_20180923_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politician', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='politik.Politician')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
