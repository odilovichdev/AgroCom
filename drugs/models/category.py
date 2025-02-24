from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Base


class Category(Base):
    name = models.CharField(max_length=250,verbose_name=_("Name"), unique=True)
    desc = models.TextField(verbose_name=_("Description"), null=True, blank=True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"