# Generated by Django 3.1.2 on 2020-10-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentby', models.IntegerField()),
                ('sentto_mailid', models.CharField(max_length=30)),
                ('relation', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='relationshipID',
        ),
        migrations.AddField(
            model_name='person',
            name='relationship',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
