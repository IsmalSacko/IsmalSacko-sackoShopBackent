from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Correction des conflits en ajoutant des related_names
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Nouveau nom pour éviter le conflit
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  # Nouveau nom pour éviter le conflit
        blank=True
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imageUrl = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Marque(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imageUrl = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0, blank=False)
    description = models.TextField(max_length=550,blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    productModel = models.CharField(max_length=255,blank=True, null=True)
    product_type = models.CharField(max_length=255,default='Téléphone')
    rating = models.FloatField(default=1, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    colors = models.JSONField(blank=True, null=True)
    sizes = models.JSONField(blank=True, null=True)
    imageUrls = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self) -> str:
        return self.title


# modèle PANIER
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart_items.all())

    def __str__(self):
        return f"Panier de {self.user.username}"



# modèle CART ITEM (produit dans le panier)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.title} dans {self.cart.user.username}"