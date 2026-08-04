"""
Memgraph benchmark runner.

Implements the BaseRunner interface for executing the benchmark against
a Memgraph instance.
"""

from pathlib import Path

from gqlalchemy import Memgraph

from benchmarks.common import BaseRunner


class MemgraphRunner(BaseRunner):
    """Runner implementation for Memgraph."""

    def __init__(self, config: dict):
        super().__init__(config)

        memgraph_cfg = config["memgraph"]

        self.uri = memgraph_cfg["uri"]
        self.username = memgraph_cfg.get("username", "")
        self.password = memgraph_cfg.get("password", "")

        self.client = None

    def connect(self):
        """Create a Memgraph connection."""
        # Parse bolt://host:port
        address = self.uri.replace("bolt://", "")
        host, port = address.split(":")

        self.client = Memgraph(
            host=host,
            port=int(port),
            username=self.username or None,
            password=self.password or None,
        )

        # Simple connectivity check
        self.client.execute("RETURN 1;")

    def load_dataset(self):
        """
        Placeholder dataset loader.

        A production implementation should batch-import nodes and
        relationships from the generated dataset.
        """
        dataset_file = Path(
            self.config["dataset"]["file"]
        )

        if not dataset_file.exists():
            raise FileNotFoundError(
                f"Dataset not found: {dataset_file}"
            )

        print(f"Dataset found: {dataset_file}")
        print("Dataset loading not yet implemented.")

    def execute_query(self, query: str):
        """Execute a single Cypher query."""
        list(self.client.execute_and_fetch(query))

    def close(self):
        """
        Close the Memgraph connection.

        gqlalchemy manages the underlying connection automatically,
        so no explicit close operation is currently required.
        """
        self.client = None
