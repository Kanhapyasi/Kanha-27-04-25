

from django.db import mig
from main.models import StoreStatus

import csv

def create_store_status_log(apps, schema_editor):
    Store = apps.get_model('main', 'Store')
    StoreStatusLog = apps.get_model('main', 'StoreStatusLog')
    with open('main/csv_data/store_status.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            store = Store.objects.filter(store_id=row['store_id']).first()
            status = StoreStatus.ACTIVE if row['status'] == 'active' else StoreStatus.INACTIVE
            timestamp = row['timestamp_utc'][:len(row['timestamp_utc'])-4]
            if store:
                status_log = StoreStatusLog.objects.create(
                    store=store,
                    status=status,
                    timestamp=timestamp
                )
                print(status_log)

class Migrate(mig.Migrate):

    dependencies = [
        ('main', '0002_auto_20230725_2026'),
    ]

    operations = [
        mig.RunPython(create_store_status_log, reverse_code=mig.RunPython.noop),
    ]
