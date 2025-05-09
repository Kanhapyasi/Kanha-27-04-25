

from django.db import mig, models
import django.db.models.deletion


class Migrate(mig.Migrate):

    initial = True

    dependencies = [
    ]

    operations = [
        mig.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('timezone_str', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        mig.CreateModel(
            name='StoreTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
            ],
        ),
        mig.CreateModel(
            name='StoreStatusLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')])),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='Time Stamp in UTC')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.store')),
            ],
        ),
    ]
