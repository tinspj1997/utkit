"""Tests for Cloudflare R2 client presigned URL functionality."""
import os
from unittest.mock import Mock, patch
import pytest

from utkit.store.cloudflare.r2 import R2Client


class TestR2ClientPresignedURL:
    """Test suite for R2Client presigned URL generation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Set environment variables for testing
        self.test_account_id = "test-account-id"
        self.test_access_key_id = "2285c549f83fada44a225cd537568e7b"
        self.test_secret_key = "fae8bc59228f8b60baf650a7f835981e0072b1dc1e888bed32e997ed9fbba09b"
        self.test_endpoint = "https://f10523bd6f065b8cdc1c16b93724c180.r2.cloudflarestorage.com/"

        # Set environment variables
        os.environ["R2_ACCOUNT_ID"] = self.test_account_id
        os.environ["R2_ACCESS_KEY_ID"] = self.test_access_key_id
        os.environ["R2_SECRET_ACCESS_KEY"] = self.test_secret_key
        os.environ["R2_ENDPOINT"] = self.test_endpoint

    def teardown_method(self):
        """Clean up after each test method."""
        # Remove environment variables
        for key in ["R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_ENDPOINT"]:
            os.environ.pop(key, None)

    def test_generate_presigned_url_basic(self):
        """Test basic presigned URL generation."""
        client = R2Client(
            account_id=self.test_account_id,
            access_key_id=self.test_access_key_id,
            secret_key=self.test_secret_key,
        )

        # Mock the boto3 client's generate_presigned_url method
        mock_url = "https://test-bucket.r2.cloudflarestorage.com/test-key.txt?X-Amz-Signature=abc123"
        with patch.object(client.client, "generate_presigned_url", return_value=mock_url):
            result = client.generate_presigned_url("test-bucket", "test-key.txt")
            assert result == mock_url

    def test_generate_presigned_url_custom_expiration(self):
        """Test presigned URL generation with custom expiration."""
        client = R2Client(
            account_id=self.test_account_id,
            access_key_id=self.test_access_key_id,
            secret_key=self.test_secret_key,
        )

        # Mock the boto3 client's generate_presigned_url method
        mock_url = "https://test-bucket.r2.cloudflarestorage.com/test-key.txt?X-Amz-Signature=def456"
        with patch.object(client.client, "generate_presigned_url", return_value=mock_url):
            result = client.generate_presigned_url("test-bucket", "test-key.txt", expiration=7200)
            assert result == mock_url

    def test_generate_presigned_url_with_environment_variables(self):
        """Test presigned URL generation using environment variables."""
        # Remove parameters, should use environment variables
        client = R2Client()

        # Mock the boto3 client's generate_presigned_url method
        mock_url = "https://test-bucket.r2.cloudflarestorage.com/test-key.txt?X-Amz-Signature=ghi789"
        with patch.object(client.client, "generate_presigned_url", return_value=mock_url):
            result = client.generate_presigned_url("test-bucket", "test-key.txt", expiration=1800)
            assert result == mock_url

    def test_generate_presigned_url_error_handling(self):
        """Test error handling during presigned URL generation."""
        client = R2Client(
            account_id=self.test_account_id,
            access_key_id=self.test_access_key_id,
            secret_key=self.test_secret_key,
        )

        # Mock the boto3 client's generate_presigned_url method to raise an exception
        with patch.object(client.client, "generate_presigned_url", side_effect=Exception("URL generation failed")):
            with pytest.raises(Exception, match="URL generation failed"):
                client.generate_presigned_url("test-bucket", "test-key.txt")

    def test_integration_mock_test(self):
        """Integration test with mocked boto3 client for presigned URL generation."""
        # Create a mock boto3 client
        mock_boto3_client = Mock()

        # Configure mock response
        mock_url = "https://test-bucket.r2.cloudflarestorage.com/test-key.txt?X-Amz-Signature=integration123"
        mock_boto3_client.generate_presigned_url = Mock(return_value=mock_url)

        # Patch boto3.client to return our mock
        with patch("boto3.client", return_value=mock_boto3_client):
            client = R2Client(
                account_id=self.test_account_id,
                access_key_id=self.test_access_key_id,
                secret_key=self.test_secret_key,
            )

            # Test presigned URL generation
            result = client.generate_presigned_url("test-bucket", "test-key.txt", expiration=3600)
            assert result == mock_url
            mock_boto3_client.generate_presigned_url.assert_called_once_with(
                "get_object", Params={"Bucket": "test-bucket", "Key": "test-key.txt"}, ExpiresIn=3600
            )

    def test_generate_presigned_url_different_buckets_and_keys(self):
        """Test presigned URL generation with different bucket and key combinations."""
        client = R2Client(
            account_id=self.test_account_id,
            access_key_id=self.test_access_key_id,
            secret_key=self.test_secret_key,
        )

        # Mock the boto3 client's generate_presigned_url method
        mock_url = "https://example-bucket.r2.cloudflarestorage.com/example-file.txt?X-Amz-Signature=test123"
        with patch.object(client.client, "generate_presigned_url", return_value=mock_url):
            # Test with different bucket and key
            result = client.generate_presigned_url("example-bucket", "example-file.txt", expiration=1800)
            assert result == mock_url

    def test_generate_presigned_url_long_expiration(self):
        """Test presigned URL generation with long expiration time."""
        client = R2Client(
            account_id=self.test_account_id,
            access_key_id=self.test_access_key_id,
            secret_key=self.test_secret_key,
        )

        # Mock the boto3 client's generate_presigned_url method
        mock_url = "https://test-bucket.r2.cloudflarestorage.com/test-key.txt?X-Amz-Signature=long-exp"
        with patch.object(client.client, "generate_presigned_url", return_value=mock_url):
            # Test with long expiration (24 hours = 86400 seconds)
            result = client.generate_presigned_url("test-bucket", "test-key.txt", expiration=86400)
            assert result == mock_url