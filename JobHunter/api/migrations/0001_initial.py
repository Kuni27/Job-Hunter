# Generated by Django 5.0.4 on 2024-04-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_type', models.CharField(choices=[('None', 'None'), ('High School', 'High School'), ('Vocational', 'Vocational'), ("Associate's", "Associate's"), ("Bachelor's", "Bachelor's"), ("Master's", "Master's"), ('PhD', 'PhD')], max_length=20)),
                ('work_history_count', models.PositiveIntegerField()),
                ('total_years_experience', models.FloatField()),
                ('currently_employed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('managed_others', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('managed_how_many', models.PositiveIntegerField()),
            ],
        ),
    ]
