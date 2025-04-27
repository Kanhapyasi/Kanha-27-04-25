

from django.db import mig, models
import django.db.models.deletion


class Migrate(mig.Migrate):

    dependencies = [
        ('main', '0005_storereport'),
    ]

    operations = [
        mig.AlterField(
            model_name='storereport',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='main.store'),
        ),
    ]
