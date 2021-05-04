# Generated by Django 3.2 on 2021-05-02 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=1)),
                ('crn', models.CharField(max_length=20, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.person')),
            ],
            options={
                'db_table': 'professional',
            },
        ),
    ]