# Generated by Django 3.2.6 on 2021-09-11 04:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operator', '0007_operatorevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatorwebsite',
            name='first_section_button_title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='operatorwebsite',
            name='first_section_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operatorwebsite',
            name='first_section_image',
            field=models.ImageField(null=True, upload_to='home_page_image/'),
        ),
        migrations.AddField(
            model_name='operatorwebsite',
            name='first_section_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='operatorwebsite',
            name='about_us_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='operatorwebsite',
            name='about_us_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='operatorwebsite',
            name='home_page_video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='operatorwebsite',
            name='operator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operator.operator'),
        ),
    ]
