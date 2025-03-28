import django
import os

# Initialisation de Django
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mobile_shope_backend.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import Product, Category, Marque
from django.utils import timezone

# Récupération des marques et catégories
iphone_marque = Marque.objects.get(title="Apple")
samsung_marque = Marque.objects.get(title="Samsung")
xiaomi_marque = Marque.objects.get(title="Xiaomi")

smartphone_category = Category.objects.get(title="Iphone")

# Liste des 12 produits
products = [
    # 📱 iPhone
    Product(
        title="iPhone 15 Pro Max",
        price=1499.99,
        description="iPhone 15 Pro Max avec puce A17 Pro, écran OLED 120Hz et titane.",
        is_featured=True,
        productModel="iPhone 15 Pro Max",
        product_type="Téléphone",
        rating=4.9,
        category=smartphone_category,
        marque=iphone_marque,
        colors=["Noir Titane", "Blanc Titane", "Bleu Titane", "Naturel Titane"],
        sizes=["256 Go", "512 Go", "1 To"],
        imageUrls=[
            "https://www.apple.com/newsroom/images/product/iphone/standard/Apple-iPhone-15-Pro-lineup-230912_big.jpg.large.jpg",
            "https://www.apple.com/v/iphone-15-pro/a/images/overview/design/finish_blue_titanium__brz1gm5r1w2y_large.jpg"
        ],
        created_at=timezone.now(),
    ),
    Product(
        title="iPhone 14 Pro",
        price=1199.99,
        description="iPhone 14 Pro avec écran 6,1 pouces Super Retina XDR et Dynamic Island.",
        is_featured=False,
        productModel="iPhone 14 Pro",
        product_type="Téléphone",
        rating=4.7,
        category=smartphone_category,
        marque=iphone_marque,
        colors=["Noir", "Or", "Argent", "Violet"],
        sizes=["128 Go", "256 Go", "512 Go"],
        imageUrls=[
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-finish-select-202209-6-1inch-gold",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-14-pro-finish-select-202209-6-1inch-deeppurple"
        ],
        created_at=timezone.now(),
    ),
    Product(
        title="iPhone SE (3e génération)",
        price=489.99,
        description="iPhone SE avec puce A15 Bionic, Touch ID et 5G.",
        is_featured=False,
        productModel="iPhone SE (2022)",
        product_type="Téléphone",
        rating=4.5,
        category=smartphone_category,
        marque=iphone_marque,
        colors=["Noir", "Blanc", "Rouge"],
        sizes=["64 Go", "128 Go"],
        imageUrls=[
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-se-2022-black",
            "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-se-2022-red"
        ],
        created_at=timezone.now(),
    ),

    # 📱 Samsung
    Product(
        title="Samsung Galaxy S24 Ultra",
        price=1299.99,
        description="Galaxy S24 Ultra avec S-Pen, Snapdragon 8 Gen 3 et écran AMOLED 120Hz.",
        is_featured=True,
        productModel="Galaxy S24 Ultra",
        product_type="Téléphone",
        rating=4.8,
        category=smartphone_category,
        marque=samsung_marque,
        colors=["Noir Titane", "Gris Titane", "Violet", "Jaune"],
        sizes=["256 Go", "512 Go", "1 To"],
        imageUrls=[
            "https://images.samsung.com/is/image/samsung/p6pim/fr/2301/gallery/fr-galaxy-s24-ultra-sm-s928bzbgeub-538203433",
            "https://images.samsung.com/is/image/samsung/p6pim/fr/2301/gallery/fr-galaxy-s24-ultra-sm-s928bzbgeub-538203431"
        ],
        created_at=timezone.now(),
    ),
    Product(
        title="Samsung Galaxy Z Flip5",
        price=1099.99,
        description="Galaxy Z Flip5, smartphone pliable avec écran externe de 3,4 pouces.",
        is_featured=False,
        productModel="Galaxy Z Flip5",
        product_type="Téléphone",
        rating=4.6,
        category=smartphone_category,
        marque=samsung_marque,
        colors=["Graphite", "Menthe", "Lavande"],
        sizes=["256 Go", "512 Go"],
        imageUrls=[
            "https://images.samsung.com/is/image/samsung/p6pim/fr/sm-f731blgaeub/gallery/fr-galaxy-z-flip5-f731-488626-sm-f731blgaeub-538612540",
            "https://images.samsung.com/is/image/samsung/p6pim/fr/sm-f731blgaeub/gallery/fr-galaxy-z-flip5-f731-488626-sm-f731blgaeub-538612541"
        ],
        created_at=timezone.now(),
    ),

    # 📱 Xiaomi
    Product(
        title="Xiaomi Redmi Note 12 Pro",
        price=349.99,
        description="Redmi Note 12 Pro avec écran AMOLED 120Hz, capteur 200MP et charge rapide 120W.",
        is_featured=False,
        productModel="Redmi Note 12 Pro",
        product_type="Téléphone",
        rating=4.6,
        category=smartphone_category,
        marque=xiaomi_marque,
        colors=["Bleu Glace", "Gris Onyx", "Noir Minuit"],
        sizes=["128 Go", "256 Go"],
        imageUrls=[
            "https://i02.appmifile.com/834_operator_in/22/02/2023/5875c47611367d1537c72e19c9010fd3.jpg",
            "https://i02.appmifile.com/561_operator_in/22/02/2023/bdf23a098d3a75cfebed82962dbcd92d.jpg"
        ],
        created_at=timezone.now(),
    ),
    Product(
        title="Xiaomi 13 Ultra",
        price=999.99,
        description="Xiaomi 13 Ultra avec capteurs Leica et écran AMOLED 120Hz.",
        is_featured=True,
        productModel="Xiaomi 13 Ultra",
        product_type="Téléphone",
        rating=4.9,
        category=smartphone_category,
        marque=xiaomi_marque,
        colors=["Noir", "Vert", "Blanc"],
        sizes=["256 Go", "512 Go"],
        imageUrls=[
            "https://i02.appmifile.com/417_operator_sg/27/04/2023/c329b730b9bffca50194bbd82a4c66aa.jpg",
            "https://i02.appmifile.com/8_operator_sg/27/04/2023/940053f6a9531f76efebef52b9b32295.jpg"
        ],
        created_at=timezone.now(),
    ),
]

# Enregistrement des produits
for product in products:
    product.save()

print("📱 12 produits ajoutés avec succès !")
