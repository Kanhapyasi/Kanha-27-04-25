

from django.db import mig, models
import django.db.models.deletion


class Migrate(mig.Migrate):

    dependencies = [
        ('main', '0003_auto_20230725_2048'),
    ]

    operations = [
        mig.AlterField(
            model_name='storestatuslog',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_logs', to='main.store'),
        ),
        mig.AlterField(
            model_name='storetiming',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='main.store'),
        ),
    ]
