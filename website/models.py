from django.db import models


class QuemSomosCard(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição", help_text="Texto principal do card.")

    # Campos de controle (Boas práticas)
    ordem = models.IntegerField(
        "Ordem de Exibição",
        default=0,
        help_text="Cards com números menores aparecem primeiro.",
    )
    ativo = models.BooleanField(
        "Ativo", default=True, help_text="Desmarque para ocultar este card do site."
    )

    # Datas de auditoria
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Card - Quem Somos"
        verbose_name_plural = "Cards - Quem Somos"
        ordering = ["ordem", "id"]  # Ordena automaticamente pela ordem definida

    def __str__(self):
        return self.titulo


class Announcement(models.Model):
    message = models.CharField("Mensagem", max_length=255)
    # Permite ao redator escolher uma data ou usa a data atual por padrão
    date = models.DateField("Data de Publicação", auto_now_add=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Aviso"
        verbose_name_plural = "Avisos"
        ordering = ["-date"]  # Os mais recentes aparecem primeiro

    def __str__(self):
        return f"{self.date} - {self.message[:30]}..."


class EspecificacaoTecnica(models.Model):
    valor = models.CharField("Valor", max_length=50, help_text="Ex: 210, 3.5, 1550")
    unidade = models.CharField("Unidade", max_length=20, help_text="Ex: kg, kW, s, mm")
    rotulo = models.CharField(
        "Rótulo", max_length=100, help_text="Ex: Massa Total, 0-100 km/h"
    )

    # Campos de controlo
    ordem = models.IntegerField("Ordem de Exibição", default=0)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Especificação Técnica"
        verbose_name_plural = "Especificações Técnicas"
        ordering = ["ordem", "id"]

    def __str__(self):
        return f"{self.rotulo}: {self.valor} {self.unidade}"


class SobreProjeto(models.Model):
    titulo = models.CharField("Título da Seção", max_length=100)
    texto_geral = models.TextField("Descrição Geral")
    video_url = models.URLField("URL do Vídeo (YouTube)", blank=True, null=True)

    class Meta:
        verbose_name = "Sobre - Geral"


class Subsistema(models.Model):
    # Identificação
    nome = models.CharField("Nome do Subsistema", max_length=100)
    slug = models.SlugField(
        "URL Slug", unique=True, help_text="Preenchimento automático. Ex: powertrain"
    )

    # Área 1: Para o Card na página "Sobre"
    resumo_card = models.CharField(
        "Resumo do Card",
        max_length=150,
        help_text="Texto curto de chamada (Máx 150 caracteres).",
    )
    icone = models.CharField(
        "Ícone SVG ou Classe",
        max_length=100,
        blank=True,
        help_text="Opcional. Ex: fa-solid fa-car",
    )

    # Área 2: Para a Página Detalhada
    conteudo_pagina = models.TextField(
        "Conteúdo Completo", help_text="Texto completo com imagens e detalhes técnicos."
    )

    # Controles
    ordem = models.IntegerField("Ordem de Exibição", default=0)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Subsistema"
        verbose_name_plural = "Subsistemas"
        ordering = ["ordem"]

    def __str__(self):
        return self.nome
