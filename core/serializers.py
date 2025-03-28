from rest_framework import serializers
from djoser.serializers import UserSerializer
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title', 'imageUrl')

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marque
        fields = ('id', 'title', 'imageUrl')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class CustomUserSerializer(UserSerializer):
   

    class Meta(UserSerializer.Meta):
        model = models.CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'address', 'image')
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Inclure les détails du produit
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Product.objects.all(), source="product", write_only=True
    )

    class Meta:
        model = models.CartItem
        fields = ["id", "product", "product_id", "quantity"]

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.Cart
        fields = ["id", "user", "cart_items", "total_price"]

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.cart_items.all())


from djoser.serializers import SendEmailResetSerializer

class CustomPasswordResetSerializer(SendEmailResetSerializer):
    def get_email_options(self):
        return {
            'domain_override': 'localhost:4200',
            'use_https': False,
        }
