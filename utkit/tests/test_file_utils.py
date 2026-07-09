import hashlib

from utkit.utils.file import get_file_checksum


def test_get_file_checksum_returns_sha256_digest(tmp_path) -> None:
    file_path = tmp_path / "example.txt"
    content = b"hello from utkit"
    file_path.write_bytes(content)

    assert get_file_checksum(file_path) == hashlib.sha256(content).hexdigest()


def test_get_file_checksum_supports_custom_algorithm(tmp_path) -> None:
    file_path = tmp_path / "example.txt"
    content = b"hello from utkit"
    file_path.write_bytes(content)

    assert get_file_checksum(file_path, algorithm="md5") == hashlib.md5(content).hexdigest()
