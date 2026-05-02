from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any


@dataclass
class S3Client:
    client: Any  # boto3 S3 client object

    def list_buckets(self) -> list[dict] | None:
        response = self.client.list_buckets()
        return response.get("Buckets", [])

    def upload_file(
        self,
        file_name: str,
        bucket: str,
        object_name: str | None = None,
        extra_args: dict | None = None,
    ) -> bool:
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        if extra_args:
            self.client.upload_file(file_name, bucket, object_name, ExtraArgs=extra_args)
        else:
            self.client.upload_file(file_name, bucket, object_name)
        return True

    def upload_fileobj(
        self,
        file_obj: Any,
        bucket: str,
        object_name: str,
        extra_args: dict | None = None,
    ) -> bool:
        if extra_args:
            self.client.upload_fileobj(file_obj, bucket, object_name, ExtraArgs=extra_args)
        else:
            self.client.upload_fileobj(file_obj, bucket, object_name)
        return True

    def download_file(
        self,
        bucket: str,
        object_name: str,
        file_name: str,
        extra_args: dict | None = None,
    ) -> bool:
        if extra_args:
            self.client.download_file(bucket, object_name, file_name, ExtraArgs=extra_args)
        else:
            self.client.download_file(bucket, object_name, file_name)
        return True

    def download_fileobj(
        self,
        bucket: str,
        object_name: str,
        file_obj: Any,
        extra_args: dict | None = None,
    ) -> bool:
        if extra_args:
            self.client.download_fileobj(bucket, object_name, file_obj, ExtraArgs=extra_args)
        else:
            self.client.download_fileobj(bucket, object_name, file_obj)
        return True

    def generate_presigned_url(
        self,
        bucket: str,
        object_name: str,
        expiration: int = 3600,
    ) -> str | None:
        response = self.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket, "Key": object_name},
            ExpiresIn=expiration,
        )
        return response

    def generate_presigned_post(
        self,
        bucket: str,
        object_name: str,
        expiration: int = 3600,
        fields: dict | None = None,
        conditions: list | None = None,
    ) -> dict | None:
        response = self.client.generate_presigned_post(
            bucket,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration,
        )
        return response

    def delete_object(self, bucket: str, object_name: str) -> bool:
        self.client.delete_object(Bucket=bucket, Key=object_name)
        return True

    def head_object(self, bucket: str, object_name: str) -> dict | None:
        response = self.client.head_object(Bucket=bucket, Key=object_name)
        return response
