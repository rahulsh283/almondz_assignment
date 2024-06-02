# Generated by Django 3.2.25 on 2024-06-01 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almondz_app', '0006_alter_expensegroupmodel_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetxnmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='almondz_app.usermodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expensetxnmodel',
            name='owes_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owes_user', to='almondz_app.usermodel'),
        ),
    ]
