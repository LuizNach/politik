# Generated by Django 2.0.7 on 2018-08-12 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LawProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('passed', models.NullBooleanField()),
                ('createdAt', models.DateField(blank=True, null=True)),
                ('passedAt', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('office', models.TextField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.NullBooleanField()),
                ('law', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politik.LawProject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lawproject',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='politik.Politician'),
        ),
    ]
