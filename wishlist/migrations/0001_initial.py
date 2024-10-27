from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_items', to='products.katalog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wishlist',
                'verbose_name_plural': 'Wishlists',
                'ordering': ['-added_on'],
            },
        ),
        migrations.AddConstraint(
            model_name='wishlist',
            constraint=models.UniqueConstraint(fields=('user', 'product'), name='unique_user_product_wishlist'),
        ),
    ]
