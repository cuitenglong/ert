# Generated by Django 2.2.2 on 2019-06-10 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationtest', '0009_auto_20190610_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relationtest.AreaInfo'),
        ),
    ]