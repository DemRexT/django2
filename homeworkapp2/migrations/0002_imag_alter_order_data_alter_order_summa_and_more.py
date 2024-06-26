# Generated by Django 5.0.4 on 2024-04-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='./images/')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='summa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_reg',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
