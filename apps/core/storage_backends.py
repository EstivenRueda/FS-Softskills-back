from django.conf import settings
from storages.backends.s3boto3 import S3StaticStorage


class StaticStorage(S3StaticStorage):
    location = "static"
    default_acl = getattr(settings, "AWS_DEFAULT_ACL", None)


class PublicMediaStorage(S3StaticStorage):
    location = "media"
    default_acl = getattr(settings, "AWS_DEFAULT_ACL", None)
    file_overwrite = getattr(settings, "AWS_S3_FILE_OVERWRITE", False)
