
import os
from django.conf import settings
from django.db import mig

import csv

def create_store_data(apps, schema_editor):
    Store = apps.get_model('main', 'Store')
    with open('main/csv_data/data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            Store.objects.create(
                store_id=row['store_id'],
                timezone_str=row['timezone_str'],
            )

def populate_store_start_end_time(apps, schema_editor):
    Store = apps.get_model('main', 'Store')
    StoreTiming = apps.get_model('main', 'StoreTiming')
    with open('main/csv_data/Menu_hours.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            store = Store.objects.filter(store_id=row['store_id']).first()
            if store:
                store_timing = StoreTiming.objects.create(
                    store=store,
                    day=row['day'],
                    start_time=row['start_time_local'],
                    end_time=row['end_time_local'],
                )
                print(store_timing)

# def populate_store_start_end_time(apps, schema_editor):
#     Store = apps.get_model('main', 'Store')
#     StoreTiming = apps.get_model('main', 'StoreTiming')

#     import csv
#     file_path = os.path.join(settings.BASE_DIR, 'data', 'business_hours.csv')  # update if necessary
#     with open(file_path) as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if 'day' in row:
#                 StoreTiming.objects.create(
#                     store_id=row['store_id'],
#                     day=row['day'],
#                     start_time=row['start_time_local'],
#                     end_time=row['end_time_local']
#                 )
#             elif 'timezone_str' in row:
#                 Store.objects.update_or_create(
#                     store_id=row['store_id'],
#                     defaults={'timezone_str': row['timezone_str']}
 #               )


class Migrate(mig.Migrate):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        mig.RunPython(create_store_data,reverse_code=mig.RunPython.noop),
        mig.RunPython(populate_store_start_end_time,reverse_code=mig.RunPython.noop),
    ]
