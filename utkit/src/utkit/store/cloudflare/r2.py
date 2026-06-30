from typing import Optional
import os
import boto3


class R2Client:
    def __init__(
        self,
        account_id: Optional[str] = None,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
    ):
        # Fetch from environment variables if not provided
        self.account_id = account_id or os.getenv("R2_ACCESS_KEY_ID")
        self.access_key = access_key or os.getenv("R2_ACCESS_KEY")
        self.secret_key = secret_key or os.getenv("R2_SECRET_ACCESS_KEY")

        # Validate required values
        if not self.account_id or not self.access_key or not self.secret_key:
            raise ValueError(
                "R2 credentials missing. Please provide account_id, access_key, and secret_key either as parameters or via environment variables (R2_ACCESS_KEY_ID, R2_ACCESS_KEY, R2_SECRET_ACCESS_KEY)"
            )

        # Get endpoint from environment or generate from account_id
        endpoint = os.getenv("R2_ENDPOINT")
        if endpoint:
            self.base_url = endpoint
        else:
            self.base_url = f"https://{self.account_id}.r2.cloudflarestorage.com"

        # Initialize boto3 client for R2
        self.client = boto3.client(
            service_name="s3",
            endpoint_url=self.base_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name="auto",
        )

    def upload_file(self, file_path: str, bucket: str, key: str):
        """Uploads a file to the specified R2 bucket."""
        self.client.upload_file(file_path, bucket, key)

    def upload_fileobj(self, file_obj, bucket: str, key: str):
        """Uploads a file-like object to the specified R2 bucket."""
        self.client.upload_fileobj(file_obj, bucket, key)

    def get_file_info(self, bucket: str, key: str):
        """Retrieves metadata for a file in the specified R2 bucket."""
        response = self.client.head_object(Bucket=bucket, Key=key)
        return response

    def download_file(self, bucket: str, key: str, file_path: str):
        """Downloads a file from the specified R2 bucket."""
        self.client.download_file(bucket, key, file_path)

    def list_objects(self, bucket: str, prefix: str = ""):
        """Lists objects in the specified R2 bucket with an optional prefix."""
        response = self.client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        return response.get("Contents", [])

    def delete_object(self, bucket: str, key: str):
        """Deletes an object from the specified R2 bucket."""
        self.client.delete_object(Bucket=bucket, Key=key)

    def generate_presigned_url(self, bucket: str, key: str, expiration: int = 3600):
        """Generates a presigned URL for accessing an object in the specified R2 bucket."""
        url = self.client.generate_presigned_url(
            "get_object", Params={"Bucket": bucket, "Key": key}, ExpiresIn=expiration
        )
        return url
