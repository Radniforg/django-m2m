from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    theme = models.ManyToManyField(
        'Theme',
        through='Variant',
        related_name='scopes'
    )
    objects = models.Manager()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.title

class Theme(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Тематический раздел'

    def __str__(self):
        return self.name


class Variant(models.Model):

    theme = models.ForeignKey(
        Theme,
        verbose_name='Тематический раздел',
        on_delete=models.CASCADE,
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )

    main = models.BooleanField(verbose_name='Основной',
                               default=False)

    class Meta:
        unique_together = ('theme', 'article')
