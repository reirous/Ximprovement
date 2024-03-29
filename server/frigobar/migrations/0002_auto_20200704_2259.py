# Generated by Django 3.0.7 on 2020-07-05 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frigobar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='justification',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Order justification'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderType',
            field=models.IntegerField(choices=[(0, 'Sales Order'), (1, 'Bonus Order')], default=0),
        ),
    ]
