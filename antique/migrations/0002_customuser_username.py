# Generated by Django 4.2.7 on 2023-11-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antique', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='dell', max_length=100),
            preserve_default=False,
        ),
    ]
