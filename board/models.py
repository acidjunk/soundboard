from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Auditable(models.Model):
    """
    Abstract model for created_on / created_by and modified_on/modified_by
    """
    created_on = models.DateTimeField(_("date/time created"), editable=False, auto_now_add=True)
    modified_on = models.DateTimeField(_("date/time modified"), editable=False, auto_now=True)

    # These fields will be populated automatically through soundboard.board.middleware.UserAuditMiddleware
    created_by = models.ForeignKey(User, editable=False, related_name='%(app_label)s_%(class)s_created_by', null=True,
                                   default=None)
    modified_by = models.ForeignKey(User, editable=False, related_name='%(app_label)s_%(class)s_modified_by', null=True,
                                    default=None)

    class Meta:  # pylint: disable=C1001, W0232, R0903
        abstract = True


class SoundBoard(Auditable):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Return string representation for SoundBoard object."""
        return self.name


class Sound(Auditable):
    sound_board = models.ForeignKey(SoundBoard, related_name='sounds')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        """Return string representation for Sound object."""
        return "{} ({})".format(self.name, self.sound_board)
