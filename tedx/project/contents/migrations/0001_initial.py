# Generated by Django 5.0.6 on 2024-05-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=300, null=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_no', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='table2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Physics', models.SmallIntegerField(null=True)),
                ('Chemistry', models.SmallIntegerField(null=True)),
                ('Maths', models.SmallIntegerField(null=True)),
            ],
        ),
    ]
