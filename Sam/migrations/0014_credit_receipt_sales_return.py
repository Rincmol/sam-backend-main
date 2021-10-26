# Generated by Django 3.2.3 on 2021-10-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sam', '0013_cash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.TextField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('internal_ref_no', models.TextField(max_length=100)),
                ('due_on', models.TextField(max_length=100)),
                ('user_id', models.TextField(max_length=100)),
                ('credit_limit_amt', models.TextField(max_length=100)),
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
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.TextField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('internal_ref_no', models.TextField(max_length=100)),
                ('due_on', models.TextField(max_length=100)),
                ('credit_limit_amt', models.TextField(max_length=100)),
                ('user_id', models.TextField(max_length=100)),
                ('customer_id', models.TextField(max_length=100)),
                ('customer_name', models.TextField(max_length=100)),
                ('si_no1', models.TextField(max_length=100)),
                ('si_no2', models.TextField(max_length=100)),
                ('si_no3', models.TextField(max_length=100)),
                ('invoice_no1', models.TextField(max_length=100)),
                ('invoice_no2', models.TextField(max_length=100)),
                ('invoice_no3', models.TextField(max_length=100)),
                ('invoice_date1', models.TextField(max_length=100)),
                ('invoice_date2', models.TextField(max_length=100)),
                ('invoice_date3', models.TextField(max_length=100)),
                ('duedate1', models.TextField(max_length=100)),
                ('duedate2', models.TextField(max_length=100)),
                ('duedate3', models.TextField(max_length=100)),
                ('invoice_amt1', models.TextField(max_length=100)),
                ('invoice_amt2', models.TextField(max_length=100)),
                ('invoice_amt3', models.TextField(max_length=100)),
                ('received_amt1', models.TextField(max_length=100)),
                ('received_amt2', models.TextField(max_length=100)),
                ('received_amt3', models.TextField(max_length=100)),
                ('outstanding1', models.TextField(max_length=100)),
                ('outstanding2', models.TextField(max_length=100)),
                ('outstanding3', models.TextField(max_length=100)),
                ('discount1', models.TextField(max_length=100)),
                ('discount2', models.TextField(max_length=100)),
                ('discount3', models.TextField(max_length=100)),
                ('balance_amt1', models.TextField(max_length=100)),
                ('balance_amt2', models.TextField(max_length=100)),
                ('balance_amt3', models.TextField(max_length=100)),
                ('tick_space1', models.TextField(max_length=100)),
                ('tick_space2', models.TextField(max_length=100)),
                ('tick_space3', models.TextField(max_length=100)),
                ('partial1', models.TextField(max_length=100)),
                ('partial2', models.TextField(max_length=100)),
                ('partial3', models.TextField(max_length=100)),
                ('total1', models.TextField(max_length=100)),
                ('total2', models.TextField(max_length=100)),
                ('total3', models.TextField(max_length=100)),
                ('total4', models.TextField(max_length=100)),
                ('total5', models.TextField(max_length=100)),
                ('total6', models.TextField(max_length=100)),
                ('on_account', models.TextField(max_length=100)),
                ('discount', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.TextField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('internal_ref_no', models.TextField(max_length=100)),
                ('user_id', models.TextField(max_length=100)),
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
