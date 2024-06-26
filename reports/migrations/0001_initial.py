# Generated by Django 4.2.6 on 2024-03-28 05:59

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
            name='case',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=100)),
                ('case_type', models.CharField(max_length=100)),
                ('case_description', models.TextField()),
                ('case_date', models.DateField()),
                ('case_created_on', models.DateField(auto_now_add=True)),
                ('case_location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('case_files', models.FileField(upload_to='case_files/')),
                ('case_status', models.CharField(blank=True, max_length=50, null=True)),
                ('inspector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inspector', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
