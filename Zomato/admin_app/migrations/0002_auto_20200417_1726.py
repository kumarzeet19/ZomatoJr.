# Generated by Django 3.0 on 2020-04-17 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admin_app.Country'),
        ),
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admin_app.Country'),
        ),
        migrations.AddField(
            model_name='region',
            name='state',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='admin_app.State'),
        ),
    ]
