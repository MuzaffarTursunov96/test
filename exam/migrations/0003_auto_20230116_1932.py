# Generated by Django 3.0.5 on 2023-01-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20230116_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentanswer',
            name='marks',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
