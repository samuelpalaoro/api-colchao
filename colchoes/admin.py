from django.contrib import admin
from .models import Brand, MattressType, Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Configuração do Admin para o modelo Brand.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(MattressType)
class MattressTypeAdmin(admin.ModelAdmin):
    """
    Configuração do Admin para o modelo MattressType.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configuração do Admin para o modelo Product, com organização avançada.
    """

    fieldsets = (
        ('Informações Fundamentais', {
            'fields': ('status', 'name', 'brand', 'mattress_type', 'size')
        }),
        ('SEO e URL', {
            'classes': ('collapse',),
            'fields': ('slug', 'meta_title', 'meta_description')
        }),
        ('Conteúdo Principal da Página', {
            'description': "Estes são os blocos de texto que formarão o corpo da sua análise.",
            'fields': (
                'page_title',
                'introduction_text',
                'comfort_section_title',
                'comfort_section_text',
                'technology_section_title',
                'technology_section_text',
                'who_is_it_for_section_title',
                'who_is_it_for_text',
                'conclusion_section_title',
                'conclusion_text',
            )
        }),
        ('Monetização e Mídia', {
            'fields': ('affiliate_link1', 'affiliate_link2', 'affiliate_link3', 'image_url', 'video_review_url', 'gallery_images', 'image')
        }),
        ('Dados Estruturados (JSON)', {
            'classes': ('collapse',),
            'description': "Use formato JSON válido. Ferramentas como JSONLint podem ajudar.",
            'fields': ('technical_specs', 'pros_and_cons', 'faq_section')
        }),
        ('Filtros e Comparações', {
            'fields': ('firmness_level', 'main_competitor', 'heat_dissipation_rating', 'motion_isolation_rating', 'edge_support_rating')
        }),
        ('Marketing e Prova Social', {
            'fields': ('target_audience_text', 'best_for_scenario', 'user_rating_score', 'expert_review_snippet', 'awards')
        }),
        ('Controle de Versão', {
            'fields': ('version', 'last_updated_by_user')
        }),
    )

    list_display = ('name', 'brand', 'status', 'size', 'firmness_level', 'last_updated_by_user')
    list_filter = ('status', 'brand', 'mattress_type', 'firmness_level', 'size')
    search_fields = ('name', 'brand__name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ['brand', 'mattress_type', 'main_competitor']
    readonly_fields = ('last_updated_by_user',)
    list_editable = ('status',)
