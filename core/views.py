from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from django.db.models import Count
import random
from rest_framework import status


from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode


# Create your views here.
class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    queryset = models.Category.objects.all()

class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:5]
    
class MarqueList(generics.ListAPIView):
    serializer_class = serializers.MarqueSerializer

    queryset = models.Marque.objects.all()  

class ProducList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.all()
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]
    
class PopularProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.filter(rating__gte=4.0, rating__lte=5.0)
        queryset = queryset.annotate(random_order=Count('id'))
        queryset = list(queryset)
        random.shuffle(queryset)
        return queryset[:20]
    
class ProducListByType(APIView):
    serializer_class = serializers.ProductSerializer

    def get(self,request):
        query = request.query_params.get('product_type', None)

        if query:
            queryset = models.Product.objects.filter(product_type__icontains=query)
            queryset = queryset.annotate(random_order=Count('id'))
            product_list = list(queryset)
            random.shuffle(product_list)

            limeted_product_list = product_list[:20]
            serializer = serializers.ProductSerializer(limeted_product_list, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Pas de produit de ce type'}, status=status.HTTP_400_BAD_REQUEST)
 

class SimilarProductList(APIView):

    def get(self,request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category=query)
            product_list = list(products)
            random.shuffle(product_list)
            limeted_product_list = product_list[:6]
            serializer = serializers.ProductSerializer(limeted_product_list, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Pas de produit similaire pour cette catégorie'}, status=status.HTTP_400_BAD_REQUEST)
        
class SearchProductByTitle(APIView):

    def get(self,request):
        query = request.query_params.get('q', None)

        if query:
            products = models.Product.objects.filter(title__icontains=query)
            serializer = serializers.ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Pas de produit trouvé pour' + query}, status=status.HTTP_400_BAD_REQUEST)
        

class ProductByCategory(APIView):

    def get(self,request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category=query)
            serializer = serializers.ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Pas de produit trouvé pour cette catégorie'}, status=status.HTTP_400_BAD_REQUEST)





# Récupérer le panier d'un utilisateur
class CartDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Récupérer le panier de l'utilisateur
        cart = get_object_or_404(models.Cart, user=request.user)

        # Sérialiser les données du panier
        serializer = serializers.CartSerializer(cart)

        # Retourner les données du panier (y compris le total)
        return Response({
            "cart": serializer.data,
            "total_price": cart.get_total_price()
        })



# Ajouter un produit au panier
class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        # Récupérer le produit
        product = get_object_or_404(models.Product, id=product_id)

        # Récupérer ou créer un panier pour l'utilisateur
        cart, created = models.Cart.objects.get_or_create(user=user)

        # Ajouter ou mettre à jour l'item dans le panier
        cart_item, item_created = models.CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        else:
            cart_item.quantity = int(quantity)
            cart_item.save()

        return Response({"message": "Produit ajouté au panier"}, status=status.HTTP_201_CREATED)



# ✅ Supprimer un produit du panier
class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, item_id):
        user = request.user
        cart = get_object_or_404(models.Cart, user=user)
        cart_item = get_object_or_404(models.CartItem, cart=cart, id=item_id)

        cart_item.delete()
        return Response({"message": "Produit supprimé du panier"}, status=status.HTTP_204_NO_CONTENT)


# ✅ Mettre à jour la quantité d’un produit dans le panier
class UpdateCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, item_id):
        user = request.user
        quantity = request.data.get("quantity")

        if not quantity or int(quantity) < 1:
            return Response({"error": "Quantité invalide"}, status=status.HTTP_400_BAD_REQUEST)

        cart = get_object_or_404(models.Cart, user=user)
        cart_item = get_object_or_404(models.CartItem, cart=cart, id=item_id)
        
        cart_item.quantity = int(quantity)
        cart_item.save()

        return Response({"message": "Quantité mise à jour"}, status=status.HTTP_200_OK)


# vue pour la rénitilisation du mot de passe


class PasswordResetConfirmView(APIView):
    def post(self, request, uid, token):
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = get_user_model().objects.get(pk=uid)
        except Exception:
            return Response({"detail": "Invalid token or user"}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        # Logique pour la réinitialisation du mot de passe ici
        # Tu peux demander à l'utilisateur de choisir un nouveau mot de passe
        return Response({"detail": "Password reset successfully"}, status=status.HTTP_200_OK)
