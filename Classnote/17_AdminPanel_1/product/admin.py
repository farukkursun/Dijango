from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Product)

### Tabular Inline###

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0 
    classes = ('collapse',)


#######ProductAdmin#############
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    # Tablo sutunları:
    list_display = ['id', 'name', 'is_in_stock', 'slug', 'create_date', 'update_date']
    # Kayda gitmek için linkleme:
    list_display_links = ['id', 'name']
    # Tablo üzerinde güncelleyebilme:
    list_editable = ['is_in_stock']
    # Filtreleme (arama değil):
    list_filter = ['is_in_stock', 'create_date', 'update_date']
    # Arama:
    search_fields = ('id', 'name')
    search_help_text = 'Arama işlemlerini buradan yapabilrsiniz.'
    # Default Sıralama:
    ordering = ('-id',)
    # Sayfa başına kayıt sayısı:
    list_per_page = 20
    # Tümünü göster yaparken max kayıt sayısı:
    list_max_show_all = 999
    # Tarihe göre filtreleme başlığı:
    date_hierarchy = 'create_date'
    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug': ['name']} # slug = SEO URL
    # Form element konumlandırma:
    inlines = [ReviewInline]
    fields = (
        ('name', 'is_in_stock'),
        ('slug'),
        ('description'),
        ('category'),
    )
    
    filter_horizontal = ("category", ) #ikisinden biri

    filter_vertical = ("category", )
    # Detaylı Form element konumlandırma: ikisi ayni anda olmaz
    '''
    fieldsets = (
        ('General:', {
            # 'classes': ('',),
            'fields': (
                ('name', 'is_in_stock'),
            ),
            'description': 'Genel ayarları buradan yapabilirsiniz.'
        }),
        ('Details:', {
            'classes': ('collapse',),
            'fields': (
                ('slug'),
                ('description'),
            ),
            'description': 'Diğer ayarları buradan yapabilirsiniz.'
        }),
    )
    '''



    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')
    

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')
    
    set_stock_in.short_description = 'İşaretli ürünleri stoğa ekle'
    set_stock_out.short_description = 'İşaretli ürünleri stoktan çıkar'

    actions = ('set_stock_in', 'set_stock_out')
    

       #### Ekstra Field ######
    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days

    list_display += ['added_days_ago']


    ####
    def how_many_reviews(self, object):
        return object.reviews.count()

    list_display += ['how_many_reviews']    

    #### RichtextEditör #######





admin.site.register(Product, ProductAdmin)
############################

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_released', 'created_date')
    list_per_page = 20
    raw_id_fields = ('product',)

admin.site.register(Review, ReviewAdmin)


