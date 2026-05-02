import boto3
from dataclasses import dataclass

from .s3 import S3Client


@dataclass
class AWSConfig:
    """AWS connection configuration."""

    access_key_id: str
    secret_access_key: str
    region_name: str

    def create_client(self, service_name: str):
        """Create a boto3 client for the specified AWS service."""
        return boto3.client(
            service_name,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
            region_name=self.region_name,
        )


__all__ = ["AWSConfig", "S3Client"]
