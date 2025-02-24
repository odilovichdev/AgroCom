from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Base
from drugs.models import Category


class AgroProduct(Base):

    class Status(models.TextChoices):
        DRUG = "DRUG", "Drug"
        FERTILIZER = "FERTILIZER", "Fertilizer"
        NOT_INCLUDED = "NOT_INCLUDED", 'not_included'

    name = models.CharField(max_length=250, verbose_name=_("Name"), unique=True)
    desc = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"), related_name="agroProduct")
    icon = models.ImageField(upload_to='icons/',
                             verbose_name=_("Icons"), null=True, blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NOT_INCLUDED)


    class Meta:
        verbose_name = "Drug"
        verbose_name_plural = "Drugs"
        db_table = "drug"

    def __str__(self):
        return f"{self.name}"


class AgroProductImage(models.Model):
    product = models.ForeignKey(AgroProduct, on_delete=models.CASCADE, verbose_name=_("Agro Product Image"), related_name="images")
    image = models.ImageField(upload_to="agroProduct/")

    def __str__(self):
        return f"{self.product.name} - {self.id}"

    class Meta:
        verbose_name = "Agro Product Image"
        verbose_name_plural = "Agro Product Images"
        db_table = "agro_product_images"
