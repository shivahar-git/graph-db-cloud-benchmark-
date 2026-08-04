"""
Neo4j benchmark runner.

Implements the BaseRunner interface for executing the benchmark against
a Neo4j instance.
"""

from pathlib import Path

from neo4j import GraphDatabase

from benchmarks.common import BaseRunner


class Neo4jRunner(BaseRunner):
    """Runner implementation for Neo4j."""

    def __init__(self, config: dict):
        super().__init__(config)

        neo4j_cfg = config["neo4j"]

        self.uri = neo4j_cfg["uri"]
        self.username = neo4j_cfg["username"]
        self.password = neo4j_cfg["password"]
        self.database = neo4j_cfg.get("database", "neo4j")

        self.driver = None

    def connect(self):
        """Create a Neo4j driver connection."""
        self.driver = GraphDatabase.driver(
            self.uri,
            auth=(self.username, self.password),
        )

        # Verify connectivity
        self.driver.verify_connectivity()

    def load_dataset(self):
        """
        Placeholder dataset loader.

        A production implementation would parse the generated dataset and
        create nodes/relationships using batch transactions.
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
        with self.driver.session(database=self.database) as session:
            result = session.run(query)

            # Consume the full result to ensure accurate timing.
            list(result)

    def close(self):
        """Close the Neo4j connection."""
        if self.driver is not None:
            self.driver.close()
