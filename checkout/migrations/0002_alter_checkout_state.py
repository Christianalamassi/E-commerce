# Generated by Django 3.2.25 on 2024-07-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='state',
            field=models.CharField(choices=[('London', 'London'), ('Bradford', 'Bradford'), ('Wakefield', 'Wakefield'), ('Nottingham', 'Nottingham'), ('Westminster', 'Westminster'), ('Coventry', 'Coventry'), ('Birmingham', 'Birmingham'), ('Liverpool', 'Liverpool'), ('Leeds', 'Leeds'), ('Bristol', 'Bristol'), ('Manchester', 'Manchester'), ('Leicester', 'Leicester')], max_length=40),
        ),
    ]