from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = getattr(settings, "AWS_DEFAULT_ACL", None)


class PublicMediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = getattr(settings, "AWS_DEFAULT_ACL", None)
    file_overwrite = False
