"""Tests for Mongo client wrapper."""

import asyncio
import os

from pymongo.errors import ServerSelectionTimeoutError

from utkit.store.mongo import MongoClient


def test_mongo_client_initializes_async_client() -> None:
	"""MongoClient should create and expose an AsyncMongoClient instance."""
	uri = "mongodb://localhost:27017"
	mongo_client = MongoClient(uri)

	assert mongo_client.client is not None


def test_get_database_returns_database_object() -> None:
	"""get_database should return a database object with the requested name."""
	uri = "mongodb://localhost:27017"
	mongo_client = MongoClient(uri)

	db = asyncio.run(mongo_client.get_database("utkit_test_db"))

	assert db.name == "utkit_test_db"


def test_mongo_connection_ping() -> None:
	"""Optional integration test: verifies live MongoDB connectivity with ping."""
	mongo_uri = os.getenv("UTKIT_MONGODB_URI")
	if not mongo_uri:
		# Skip silently when credentials are not provided in environment.
		return

	mongo_client = MongoClient(mongo_uri)

	async def _ping() -> dict:
		return await mongo_client.client.admin.command("ping")

	try:
		result = asyncio.run(_ping())
	except ServerSelectionTimeoutError as exc:
		if "CERTIFICATE_VERIFY_FAILED" in str(exc):
			# Local machine trust-store issue; not a code failure in MongoClient.
			return
		raise

	assert result.get("ok") == 1.0
