# Generated by Django 4.1.1 on 2022-09-08 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_task_title"),
    ]

    operations = [
        migrations.AlterModelOptions(name="task", options={"ordering": ["complete"]},),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
