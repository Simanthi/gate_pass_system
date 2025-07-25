# Generated by Django 5.2.1 on 2025-07-26 09:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_data', '0001_initial'),
        ('drivers', '0001_initial'),
        ('gatepass', '0002_gatepass_qr_code'),
        ('vehicles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatepass',
            name='actual_entry_time',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='actual_exit_time',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='approval_reason',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='requested_by',
        ),
        migrations.RemoveField(
            model_name='gatepass',
            name='requested_exit_time',
        ),
        migrations.AddField(
            model_name='gatepass',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatepass',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_gatepasses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gatepass',
            name='entry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatepass',
            name='exit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatepass',
            name='person_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gatepass',
            name='person_name',
            field=models.CharField(default='James', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatepass',
            name='person_nid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gatepass',
            name='person_phone',
            field=models.CharField(default='9363503048', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gatepass',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_gatepasses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gatepasses', to='drivers.driver'),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='gate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gatepasses', to='core_data.gate'),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='purpose',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gatepasses', to='core_data.purpose'),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/'),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gatepasses', to='vehicles.vehicle'),
        ),
    ]
