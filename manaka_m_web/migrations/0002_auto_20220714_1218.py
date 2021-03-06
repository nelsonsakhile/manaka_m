# Generated by Django 2.2.28 on 2022-07-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manaka_m_web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clintsregister',
            name='Projects_completed',
        ),
        migrations.RemoveField(
            model_name='clintsregister',
            name='number_of_clients',
        ),
        migrations.RemoveField(
            model_name='clintsregister',
            name='successful_appeals',
        ),
        migrations.AddField(
            model_name='clintsregister',
            name='comments',
            field=models.CharField(default='', max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='clintsregister',
            name='invoice_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='clintsregister',
            name='invoice_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clintsregister',
            name='invoice_type',
            field=models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('Invoice', 'Invoice')], default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clintsregister',
            name='name',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Customer name'),
        ),
        migrations.AddField(
            model_name='clintsregister',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
