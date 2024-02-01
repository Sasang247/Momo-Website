# Generated by Django 4.2.4 on 2024-01-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momo', '0005_alter_allmenu_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
