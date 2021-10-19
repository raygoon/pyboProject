# Generated by Django 3.1.3 on 2021-10-11 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='Question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pybo.question'),
            preserve_default=False,
        ),
    ]