# Generated by Django 3.1 on 2021-06-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('phoneno', models.IntegerField()),
                ('emailid', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]