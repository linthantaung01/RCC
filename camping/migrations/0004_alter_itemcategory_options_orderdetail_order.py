# Generated by Django 4.2.6 on 2023-10-25 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0003_remove_itemcategory_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'Item Category', 'verbose_name_plural': 'Item Categories'},
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Order', to='camping.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order_detail', models.ManyToManyField(to='camping.orderdetail')),
            ],
        ),
    ]
