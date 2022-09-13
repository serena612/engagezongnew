# Generated by Django 3.2.7 on 2021-11-22 18:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('operator', '0017_auto_20211118_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='default_currency',
            field=models.CharField(choices=[('₦', 'Naira'), ('$', 'USD')], default='₦', max_length=3),
        ),
        migrations.CreateModel(
            name='RedeemPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='packages/')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operator.operator')),
            ],
            options={
                'verbose_name_plural': 'Redeem Packages',
            },
        ),
        migrations.CreateModel(
            name='PurchaseCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('icon', models.ImageField(upload_to='purchase_coins/')),
                ('coins', models.PositiveIntegerField()),
                ('bonus', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operator.operator')),
            ],
            options={
                'verbose_name': 'Purchase Coins',
                'verbose_name_plural': 'Purchase Coins',
                'ordering': ('-coins',),
            },
        ),
    ]