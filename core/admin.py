from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models 

# Register your models here.
admin.site.register(models.Marque)
admin.site.register(models.Category)


admin.site.register(models.Product)

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'image', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'phone', 'address', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'address', 'image', 'is_staff', 'is_active')}
        ),
    )

    
class CartItemInline(admin.TabularInline):
    model = models.CartItem
    extra = 1  # Nombre d'items vides par défaut

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_total_price', 'created_at')  # Afficher le prix total
    readonly_fields = ('get_total_price',)  # Rendre 'get_total_price' en lecture seule
    inlines = [CartItemInline]

admin.site.register(models.Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'get_total_price')
    readonly_fields = ('get_total_price',)
    search_fields = ('product__title',)
    list_filter = ('cart',)
    ordering = ('cart',)
    list_per_page = 20
admin.site.register(models.CartItem, CartItemAdmin)