"""
KognioDB (Cloud) benchmark runner.

This runner demonstrates how to execute benchmark workloads against a
cloud-hosted KognioDB-compatible endpoint using a REST API.

Update the implementation if your KognioDB deployment exposes a different
authentication or query interface.
"""

from pathlib import Path
import requests

from benchmarks.common import BaseRunner


class KognioDBRunner(BaseRunner):
    """Runner implementation for KognioDB Cloud."""

    def __init__(self, config: dict):
        super().__init__(config)

        cfg = config["cognodb"]

        self.endpoint = cfg["endpoint"].rstrip("/")
        self.api_key = cfg["api_key"]
        self.session = None

    def connect(self):
        """Initialize an HTTP session."""
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def load_dataset(self):
        """
        Placeholder dataset loader.

        Replace this method with the appropriate bulk import endpoint
        provided by your KognioDB deployment.
        """
        dataset_file = Path(self.config["dataset"]["file"])

        if not dataset_file.exists():
            raise FileNotFoundError(
                f"Dataset not found: {dataset_file}"
            )

        print(f"Dataset found: {dataset_file}")
        print("KognioDB dataset loading not yet implemented.")

    def execute_query(self, query: str):
        """
        Execute a benchmark query.

        Expected request format (example):

        POST /query
        {
            "query": "<query text>"
        }

        Modify the endpoint or payload to match your deployment.
        """
        response = self.session.post(
            f"{self.endpoint}/query",
            json={"query": query},
            timeout=self.config["benchmark"]["query_timeout_seconds"],
        )

        response.raise_for_status()

        # Force response parsing so query execution time includes transfer.
        response.json()

    def close(self):
        """Close the HTTP session."""
        if self.session is not None:
            self.session.close()
            self.session = None
