# Generated by Django 3.2.3 on 2021-10-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0012_asset_expences_income_liabilities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.TextField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('internal_ref_no', models.TextField(max_length=100)),
                ('cash', models.TextField(max_length=100)),
                ('user_id', models.TextField(max_length=100)),
                ('account', models.TextField(max_length=100)),
                ('customer_id', models.TextField(max_length=100)),
                ('customer_name', models.TextField(max_length=100)),
                ('item_id1', models.TextField(max_length=100)),
                ('item_id2', models.TextField(max_length=100)),
                ('item_details1', models.TextField(max_length=100)),
                ('item_details2', models.TextField(max_length=100)),
                ('price1_1', models.TextField(max_length=100)),
                ('price1_2', models.TextField(max_length=100)),
                ('price2_1', models.TextField(max_length=100)),
                ('price2_2', models.TextField(max_length=100)),
                ('quantity1', models.TextField(max_length=100)),
                ('quantity2', models.TextField(max_length=100)),
                ('quantity3', models.TextField(max_length=100)),
                ('quantity4', models.TextField(max_length=100)),
                ('amount1', models.TextField(max_length=100)),
                ('amount2', models.TextField(max_length=100)),
                ('sales_ex1', models.TextField(max_length=100)),
                ('sales_ex2', models.TextField(max_length=100)),
                ('job1', models.TextField(max_length=100)),
                ('job2', models.TextField(max_length=100)),
                ('labour_charge', models.TextField(max_length=100)),
                ('other_charge', models.TextField(max_length=100)),
                ('total1', models.TextField(max_length=100)),
                ('total2', models.TextField(max_length=100)),
                ('total3', models.TextField(max_length=100)),
                ('total4', models.TextField(max_length=100)),
                ('total5', models.TextField(max_length=100)),
                ('total6', models.TextField(max_length=100)),
                ('discount', models.TextField(max_length=100)),
                ('tax', models.TextField(max_length=100)),
            ],
        ),
    ]
