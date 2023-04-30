from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=55, unique=True, null=False, blank=True)
    birth_day = models.DateField(null=False, blank=True)
    photo = models.ImageField(upload_to='psychomatrix/')


class PsychomatrixBaseContent(models.Model):
    code = models.CharField(
        max_length=55,
        unique=True,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    text = models.CharField(
        max_length=10240,
        null=True,
        blank=True
    )
    advice = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )
    recommendation = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )
    celebrities = models.ManyToManyField(
        Celebrity, through='PsychomatrixBaseCelebrity',
        related_name='psychomatrixbase'
    )

    def __str__(self):
        return f"{self.title} - {self.code}"

    class Meta:
        db_table = 'psychomatrix_basic_contents'


class PsychomatrixAdditionalContent(models.Model):
    code = models.CharField(
        max_length=55,
        unique=True,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=55,
        null=True,
        blank=True
    )
    annotation = models.CharField(
        max_length=4096,
        null=True,
        blank=True
    )
    level = models.IntegerField(
        null=True,
        blank=True
    )
    text = models.CharField(
        max_length=10240,
        null=True,
        blank=True
    )
    celebrities = models.ManyToManyField(
        Celebrity, through='PsychomatrixAdditionalCelebrity',
        related_name='psychomatrixadditional'
    )

    def __str__(self):
        return f"{self.level if self.level else '-'} {self.title}"

    class Meta:
        db_table = 'psychomatrix_additional_contents'


class PsychomatrixBaseCelebrity(models.Model):
    characteristic = models.ForeignKey(
        PsychomatrixBaseContent, on_delete=models.PROTECT,
        related_name='psychomatrixbase_in_celebrity'
    )
    celebrity = models.ForeignKey(
        Celebrity, on_delete=models.CASCADE,
        related_name='psychomatrixbase_in_celebrity'
    )

    class Meta:
        db_table = 'psychomatrix_base_celebrity'


class PsychomatrixAdditionalCelebrity(models.Model):
    characteristic = models.ForeignKey(
        PsychomatrixAdditionalContent, on_delete=models.PROTECT,
        related_name='psychomatrixadditional_in_celebrity'
    )
    celebrity = models.ForeignKey(
        Celebrity, on_delete=models.CASCADE,
        related_name='psychomatrixadditional_in_celebrity'
    )

    class Meta:
        db_table = 'psychomatrix_additional_celebrity'
