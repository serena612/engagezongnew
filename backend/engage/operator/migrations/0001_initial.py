# Generated by Django 3.2.6 on 2021-08-18 13:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('schema', models.SlugField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('domain', models.URLField(unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='operators/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperatorConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('private_metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('api_base_url', models.URLField(null=True)),
                ('send_sms_endpoint', models.CharField(max_length=64, null=True)),
                ('general_styling', models.JSONField(blank=True, null=True)),
                ('operator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operator.operator')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
