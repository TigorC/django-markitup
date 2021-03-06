from __future__ import unicode_literals

import posixpath

from django.conf import settings as django_settings

from markitup import settings


def absolute_url(path, prefix=None):
    if prefix is None:
        prefix = django_settings.STATIC_URL
    if path.startswith('http://') or path.startswith('https://') or path.startswith('/'):
        return path
    return posixpath.join(prefix, path)
