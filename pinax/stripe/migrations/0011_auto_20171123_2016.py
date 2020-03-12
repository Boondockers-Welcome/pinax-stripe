# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0011_auto_20171121_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='transfer_schedule_weekly_anchor',
            new_name='payout_schedule_weekly_anchor',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='transfer_statement_descriptor',
            new_name='payout_statement_descriptor',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='transfers_enabled',
            new_name='payouts_enabled',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transfer_schedule_delay_days',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transfer_schedule_interval',
        ),
        migrations.RemoveField(
            model_name='account',
            name='transfer_schedule_monthly_anchor',
        ),
        migrations.AddField(
            model_name='account',
            name='payout_schedule_delay_days',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='payout_schedule_interval',
            field=models.CharField(blank=True, choices=[('Manual', 'manual'), ('Daily', 'daily'), ('Weekly', 'weekly'), ('Monthly', 'monthly')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='payout_schedule_monthly_anchor',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
