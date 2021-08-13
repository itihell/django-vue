from django.db import models


class BaseModel(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+"
    )

    user_edit = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+"
    )

    created_at = models.DateTimeField(
        'creado en',
        auto_now_add=True,
        blank=True,
        null=True,
        help_text='Fecha de creación del registro'
    )

    updated_at = models.DateTimeField(
        'editado en',
        auto_now_add=True,
        blank=True,
        null=True,
        help_text='Fecha de edición del registro'
    )

    class Meta:
        abstract = True

        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']
