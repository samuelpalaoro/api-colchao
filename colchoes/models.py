# products/models.py
from django.db import models
from django.utils.text import slugify

# --- Modelos de Suporte (para organização e filtros) ---
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Ex: Ortobom, Castor, Emma")
    logo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, help_text="Um breve histórico ou foco da marca.")

    def __str__(self):
        return self.name

class MattressType(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Ex: Molas Ensacadas, Espuma D33, Híbrido, Látex")
    description = models.TextField(help_text="Explicação sobre o que é este tipo de tecnologia.")

    def __str__(self):
        return self.name

# --- O Modelo Principal do Produto: Colchão ---

class Product(models.Model):

    # --- 1. Informações Fundamentais e de Identificação ---
    name = models.CharField(max_length=255, help_text="O nome completo do produto. Ex: Colchão Queen Molas Ensacadas Freedom")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, help_text="A marca deste colchão.")
    mattress_type = models.ForeignKey(MattressType, on_delete=models.PROTECT, help_text="A tecnologia principal do colchão.")
    is_active = models.BooleanField(default=True, help_text="Marque para que este produto apareça no site.")

    # --- 2. SEO e URL ---
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="URL amigável (gerado automaticamente se deixado em branco).")
    meta_title = models.CharField(max_length=75, blank=True, help_text="Título para o Google (opcional). Se vazio, um padrão será usado.")
    meta_description = models.CharField(max_length=160, blank=True, help_text="Descrição para o Google (opcional).")

    # --- 3. Monetização e Mídia ---
    affiliate_link1 = models.URLField(blank=True, null=True, help_text='Ex: "https://www.amazon.com.br/dp/B08XYZ1234"')
    affiliate_link2= models.URLField(blank=True, null=True, help_text='Ex: "https://www.magazine.com.br/dp/B08XYZ1234"')
    affiliate_link3= models.URLField(blank=True, null=True, help_text='Ex: "https://www.mercadolivre.com.br/dp/B08XYZ1234"')
    image_url = models.URLField(max_length=1024, help_text="Link da imagem principal do produto.")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, help_text="Imagem do produto (opcional).")

    # --- 4. Blocos de Conteúdo para o Template (A Mágica do SEO Programático) ---
    page_title = models.CharField(max_length=255, help_text="Título principal que aparecerá no topo da página. Ex: Análise Completa do Colchão Ortobom Freedom")
    introduction_text = models.TextField(help_text="Parágrafo inicial. Apresente o colchão e para quem ele é indicado.")

    comfort_section_title = models.CharField(max_length=255, default="Nível de Conforto e Firmeza")
    comfort_section_text = models.TextField(help_text="Descreva a sensação de deitar no colchão. É macio, firme, intermediário?")

    technology_section_title = models.CharField(max_length=255, default="Tecnologia e Materiais de Construção")
    technology_section_text = models.TextField(help_text="Explique as tecnologias (molas, espumas especiais, tecidos) e como elas beneficiam o usuário.")

    who_is_it_for_section_title = models.CharField(max_length=255, default="Este Colchão é Ideal Para Você?")
    who_is_it_for_text = models.TextField(help_text="Seja específico. Ex: 'Ideal para casais, pessoas que se mexem muito à noite, ou quem sofre com calor.'")

    conclusion_section_title = models.CharField(max_length=255, default="Veredito Final: Vale a Pena Comprar?")
    conclusion_text = models.TextField(help_text="Resuma os pontos e dê sua recomendação final, guiando para o botão de compra.")

    # --- 5. Dados Estruturados e Variáveis (JSONField) ---
    technical_specs = models.JSONField(blank=True, null=True, help_text="Use formato JSON. Ex: {\"altura_cm\": 28, \"suporte_peso_kg\": 120, \"garantia_anos\": 5}")
    pros_and_cons = models.JSONField(blank=True, null=True, help_text="Use formato JSON. Ex: {\"pros\": [\"Excelente suporte\", \"Não esquenta\"], \"cons\": [\"Pode ser pesado\", \"Preço elevado\"]}")

    # --- 6. Campos para Filtros e Comparações ---
    SIZE_CHOICES = [('SOLTEIRO', 'Solteiro'), ('CASAL', 'Casal'), ('QUEEN', 'Queen'), ('KING', 'King')]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='CASAL')

    FIRMNESS_CHOICES = [(1, 'Extra Macio'), (2, 'Macio'), (3, 'Intermediário'), (4, 'Firme'), (5, 'Extra Firme')]
    firmness_level = models.IntegerField(choices=FIRMNESS_CHOICES, default=3)

    # --- 7. Campos para SEO e Marketing de Conteúdo ---
    target_audience_text = models.CharField(max_length=255, blank=True, help_text="Complete a frase 'Este colchão é perfeito para...'. Ex: 'casais que valorizam a independência de movimentos.'")
    best_for_scenario = models.CharField(max_length=255, blank=True, help_text="Cenário ideal de uso. Ex: 'quartos de hóspedes de luxo', 'aliviar dores na lombar'.")
    main_competitor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, help_text="Selecione o principal concorrente direto deste produto para criar links de comparação.")

    # --- 8. Campos para Prova Social e Confiança ---
    user_rating_score = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, help_text="Nota média de usuários (de 0.0 a 5.0).")
    expert_review_snippet = models.TextField(blank=True, help_text="Citação curta de um 'especialista' (você!) que resuma o produto. Ex: 'O melhor equilíbrio entre maciez e suporte que testamos.'")
    awards = models.CharField(max_length=255, blank=True, help_text="Prêmios que o produto ganhou. Ex: 'Selo de Melhor Custo-Benefício 2024'.")

    # --- 9. Campos para Enriquecimento de Mídia e Conteúdo ---
    video_review_url = models.URLField(blank=True, help_text="Link de um vídeo review do YouTube (pode ser seu ou de terceiros).")
    gallery_images = models.JSONField(blank=True, null=True, help_text="Links para imagens adicionais. Ex: [{\"url\": \"link1\", \"alt\": \"vista de cima\"}, {\"url\": \"link2\", \"alt\": \"detalhe do tecido\"}]")
    faq_section = models.JSONField(blank=True, null=True, help_text="Perguntas e respostas sobre o produto. Ex: [{\"question\": \"Ele vem enrolado?\", \"answer\": \"Sim, este modelo é do tipo bed-in-a-box.\"}]")

    # --- 10. Dados Técnicos Avançados para Comparações ---
    heat_dissipation_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True, help_text="Nota de 1 a 5 para a capacidade de não esquentar.")
    motion_isolation_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True, help_text="Nota de 1 a 5 para o isolamento de movimento (bom para casais).")
    edge_support_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True, help_text="Nota de 1 a 5 para o suporte nas bordas.")

    STATUS_CHOICES = [('DRAFT', 'Rascunho'), ('PUBLISHED', 'Publicado'), ('ARCHIVED', 'Arquivado')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    version = models.IntegerField(default=1, help_text="Versão do conteúdo, para controle interno.")
    last_updated_by_user = models.DateTimeField(auto_now=True, help_text="Data da última atualização do conteúdo.")

    # --- Auto-gerar o slug ao salvar ---
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand.name}-{self.name}-{self.size}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
