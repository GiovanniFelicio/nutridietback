# Generated by Django 3.2 on 2021-05-16 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person',
            managers=[
            ],
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.IntegerField()),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=4)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person_address', to='person.person')),
            ],
            options={
                'db_table': 'person_address',
            },
        ),
    ]