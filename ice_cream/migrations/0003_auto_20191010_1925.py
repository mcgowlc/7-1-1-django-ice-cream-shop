# Generated by Django 2.2.6 on 2019-10-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20191009_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='available',
            field=models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('seasonal', 'seasonal')], max_length=255),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
