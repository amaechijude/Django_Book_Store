# Generated by Django 4.2.5 on 2024-01-17 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Authors_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('BookID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Price', models.FloatField()),
                ('Stock', models.IntegerField()),
                ('Authors_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.authors')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('CustomerID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('PasswordHash', models.CharField(max_length=100)),
                ('IsAdmin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('PaymentDate', models.DateTimeField(auto_now_add=True)),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.orders')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('OrderItemID', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Price', models.FloatField()),
                ('BookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.books')),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordApp.orders')),
            ],
        ),
    ]
