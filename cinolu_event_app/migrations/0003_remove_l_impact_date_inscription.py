# Generated by Django 4.1.7 on 2023-04-11 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinolu_event_app', '0002_l_impact_date_inscription_alter_l_impact_a_participe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='l_impact',
            name='date_inscription',
        ),
    ]
