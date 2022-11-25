# Generated by Django 4.1.3 on 2022-11-23 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_deal_offer_alter_itemquantity_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dealitem',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dealitem',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealitems', to='core.deal'),
        ),
    ]