# Generated by Django 2.2.2 on 2019-06-10 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationtest', '0006_auto_20190610_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temp',
            options={'ordering': ['title', '-addr', 'age'], 'verbose_name': '临时表', 'verbose_name_plural': '临时表'},
        ),
    ]