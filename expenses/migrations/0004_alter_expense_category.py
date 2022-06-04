# Generated by Django 4.0.4 on 2022-06-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('ONLINE SERVICES', 'ONLINE SERVICES'), ('TRAVEL', 'TRAVEL'), ('FOOD', 'FOOD'), ('RENT', 'RENT'), ('OTHERS', 'OTHERS')], default='OTHERS', max_length=255),
        ),
    ]