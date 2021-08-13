from django.db import models

from .base_model import BaseModel
from .permissions import Permission


class Role(BaseModel):
    user = None
    user_edit = None
    name = models.CharField(max_length=250)
    guard_name = models.CharField(max_length=250)
    permissions = models.ManyToManyField(Permission, db_table='auth\".\"role_has_permissions')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'auth\".\"roles'


class UserHasRole(BaseModel):
    user = None
    user_edit = None
    created_at = None
    updated_at = None
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='+'
    )
    model = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.role.name

    class Meta:
        managed = False
        db_table = 'auth\".\"user_has_roles'
