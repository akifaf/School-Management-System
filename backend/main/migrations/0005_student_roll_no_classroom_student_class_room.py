# Generated by Django 5.0.6 on 2024-06-13 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_no', models.IntegerField()),
                ('section', models.CharField(blank=True, max_length=1, null=True)),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='class_room',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='main.classroom'),
            preserve_default=False,
        ),
    ]
