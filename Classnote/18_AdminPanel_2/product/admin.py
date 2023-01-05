from django.contrib import admin

from .models import *

admin.site.site_title = "Clarusway Title" # <title> 
admin.site.site_header = "Clarusway Admin Portal" # <navbar>
admin.site.index_title = "Welcome to Clarusway Admin Portal" # <div#header>

# admin.site.register(Product)

# ---------------- TabularInline --------------------

class ReviewInline(admin.TabularInline): # StackedInline
    model = Review
    extra = 0 # Yeni eklenebilecek alan adeti.
    classes = ('collapse', )

# ---------------- Category --------------------

admin.site.register(Category)

# ---------------- Product --------------------

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
    # TabularInline: Alt kayıtları göster
    inlines = [ReviewInline]
    # Form element konumlandırma:
    fields = (
        ('name', 'is_in_stock'),
        ('slug'),
        ('description'),
        ('category'),
    )
    filter_horizontal = ("category", ) # Yatay Konumlandırma
    # filter_vertical = ("category", ) # Dikey Konumlandırma
    '''
    # Detaylı Form element konumlandırma:
    fieldsets = (
        ('General:', {
            # 'classes': ('',),
            'fields': (
                ('name', 'is_in_stock'),
                ('category'),
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

    ### Toplu İşlemlere İşlem Ekleme ###
    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')
    

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    set_stock_in.short_description = 'İşaretli ürünleri "Stokta Var" olarak işaretle'
    set_stock_out.short_description = 'İşaretli ürünleri "Stokta Yok" olarak işaretle'
    actions = ('set_stock_in', 'set_stock_out')
    ### --- ###

    ### Ekstra Field ###
    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days

    # list_display = ['id', 'name', 'is_in_stock', 'slug', 'create_date', 'update_date', 'added_days_ago']
    list_display += ['added_days_ago']
    ### --- ###

    ### Ekstra Field ###
    def how_many_reviews(self, object):
        return object.reviews.count()

    list_display += ['how_many_reviews']
    ### --- ###

    ### RichTextEditor ###
    '''
        $ pip install django-ckeditor
        $ pip freeze > requirements.txt
        -> setting.py:
            INSTALLED_APPS = (
                # ...
                'ckeditor',
                # ...
            )
            # ...
            CKEDITOR_CONFIGS = {
                'default' : {
                    'toolbar' : 'full',
                    'height' : 700,
                    'width' : 1000
                }
            }
    '''
    ### --- ###
    
# Call:
admin.site.register(Product, ProductAdmin)

# ---------------- Review --------------------

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_released', 'created_date')
    list_per_page = 20
    # İlişkili tablo kaydını ID olarak göster:
    raw_id_fields = ('product', )

admin.site.register(Review, ReviewAdmin)