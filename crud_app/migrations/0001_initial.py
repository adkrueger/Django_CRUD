# Generated by Django 2.2.5 on 2021-01-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of message.', max_length=120)),
                ('message', models.TextField(help_text="what's on your mind...")),
            ],
        ),
    ]
