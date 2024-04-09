from django.db import models


class PostProdInstance(models.Model):
    region_choices = [
        (1, "Gulf"),
        (2, "Maritimes"),
        (3, "Quebec"),
        (4, "Newfoundland"),
        (5, "Arctic"),
        (6, "O&P"),
    ]

    season = models.PositiveIntegerField(verbose_name="season")
    region = models.PositiveIntegerField(verbose_name="region", choices=region_choices)
    name = models.CharField(max_length=1000, verbose_name="post-production environment name")
    description = models.CharField(max_length=1000, verbose_name="description")
    port = models.PositiveIntegerField(verbose_name="proxy port")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="created at")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["season", "region", "name"]
