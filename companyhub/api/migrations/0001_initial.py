# Generated by Django 4.0.2 on 2022-02-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('homepage_url', models.URLField(max_length=256)),
                ('market_value', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('administration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administration', to='api.administration')),
            ],
        ),
    ]
