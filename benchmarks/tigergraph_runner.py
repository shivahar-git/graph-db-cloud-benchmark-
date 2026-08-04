"""
TigerGraph benchmark runner.

Implements the BaseRunner interface for executing benchmark workloads
against a TigerGraph database.
"""

from pathlib import Path

import pyTigerGraph as tg

from benchmarks.common import BaseRunner


class TigerGraphRunner(BaseRunner):
    """Runner implementation for TigerGraph."""

    def __init__(self, config: dict):
        super().__init__(config)

        tg_cfg = config["tigergraph"]

        self.host = tg_cfg["host"]
        self.graph_name = tg_cfg["graph_name"]
        self.username = tg_cfg["username"]
        self.password = tg_cfg["password"]

        self.connection = None

    def connect(self):
        """Establish a TigerGraph connection."""
        self.connection = tg.TigerGraphConnection(
            host=self.host,
            graphname=self.graph_name,
            username=self.username,
            password=self.password,
        )

        # Authenticate
        self.connection.getToken()

    def load_dataset(self):
        """
        Placeholder dataset loader.

        Future implementation should import the generated CSV dataset
        using TigerGraph loading jobs or REST APIs.
        """
        dataset_file = Path(self.config["dataset"]["file"])

        if not dataset_file.exists():
            raise FileNotFoundError(
                f"Dataset not found: {dataset_file}"
            )

        print(f"Dataset found: {dataset_file}")
        print("TigerGraph dataset loader not yet implemented.")

    def execute_query(self, query: str):
        """
        Execute a query.

        NOTE:
        TigerGraph uses GSQL rather than Cypher. This placeholder assumes
        compatibility for the benchmark framework. A production benchmark
        should translate benchmark queries into equivalent GSQL queries.
        """
        self.connection.runInstalledQuery(
            queryName=query.strip(),
            params={},
        )

    def close(self):
        """Release the connection."""
        self.connection = None
