from django.db import models


class TimeBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBaseModel):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, default=1, verbose_name='Telegram user id')
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"N{self.id}, ({self.user_id} - {self.name})"


class Referral(TimeBaseModel):
    class Meta:
        verbose_name = 'Referral'
        verbose_name_plural = 'Referrals'

    id = models.ForeignKey(User, unique=True, primary_key=True, on_delete=models.CASCADE)
    referral_id = models.BigIntegerField()

    def __str__(self):
        return f"N{self.id} - ot {self.referral_id}"


class Item(TimeBaseModel):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(null=True)

    category_code = models.CharField(max_length=20)
    category_name = models.CharField(max_length=20)
    subcategory_code = models.CharField(max_length=20)
    subcategory_name = models.CharField(max_length=20)

    def __str__(self):
        return f"N{self.id} - {self.name}"


class Purchase(TimeBaseModel):
    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    purchase_time = models.DateTimeField(auto_now_add=True)
    shipping_address = models.JSONField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    receiver = models.CharField(max_length=100, null=True)
    successful = models.BooleanField(default=False)

    def __str__(self):
        return f"N{self.id} - {self.item_id} ({self.quantity})"
