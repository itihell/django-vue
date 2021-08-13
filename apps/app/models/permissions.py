from django.db import models

from .base_model import BaseModel


class Permission(BaseModel):
    user = None
    user_edit = None
    name = models.CharField(max_length=250)
    guard_name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'auth\".\"permissions'


class UserHasPermission(BaseModel):
    user = None
    user_edit = None
    created_at = None
    updated_at = None
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE
    )
    model = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.permission.name

    class Meta:
        managed = False
        db_table = 'auth\".\"user_has_permissions'
