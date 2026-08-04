"""
Common utilities and abstract base class for graph database benchmark runners.
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from pathlib import Path
from statistics import mean, median
from typing import Dict, List

import psutil


class BaseRunner(ABC):
    """
    Base class that all graph database runners inherit from.
    """

    def __init__(self, config: dict):
        self.config = config
        self.query_dir = Path(config["queries"]["directory"])
        self.query_files = config["queries"]["files"]

    # ------------------------------------------------------------------
    # Abstract methods
    # ------------------------------------------------------------------

    @abstractmethod
    def connect(self):
        """Connect to the database."""

    @abstractmethod
    def load_dataset(self):
        """Load the benchmark dataset."""

    @abstractmethod
    def execute_query(self, query: str):
        """Execute a single query."""

    @abstractmethod
    def close(self):
        """Close the database connection."""

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------

    def read_query(self, filename: str) -> str:
        """Read a Cypher query from disk."""
        path = self.query_dir / filename

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def current_memory_mb(self) -> float:
        """Return current process memory usage."""
        process = psutil.Process()
        return process.memory_info().rss / (1024 * 1024)

    def current_cpu_percent(self) -> float:
        """Return current CPU utilization."""
        return psutil.cpu_percent(interval=0.2)

    def run_queries(self) -> Dict:
        """
        Execute every configured query and return benchmark metrics.
        """

        latencies: List[float] = []
        peak_memory = 0.0
        peak_cpu = 0.0

        warmups = self.config["benchmark"]["warmup_runs"]
        runs = self.config["benchmark"]["benchmark_runs"]

        for filename in self.query_files:

            query = self.read_query(filename)

            # Warm-up runs
            for _ in range(warmups):
                self.execute_query(query)

            # Timed runs
            for _ in range(runs):

                start = time.perf_counter()

                self.execute_query(query)

                elapsed_ms = (time.perf_counter() - start) * 1000

                latencies.append(elapsed_ms)

                peak_memory = max(
                    peak_memory,
                    self.current_memory_mb(),
                )

                peak_cpu = max(
                    peak_cpu,
                    self.current_cpu_percent(),
                )

        latencies.sort()

        avg_latency = mean(latencies)
        median_latency = median(latencies)

        p95 = latencies[int(len(latencies) * 0.95)]
        p99 = latencies[int(len(latencies) * 0.99)]

        throughput = (
            1000.0 / avg_latency
            if avg_latency > 0
            else 0
        )

        return {
            "queries_executed": len(latencies),
            "average_latency_ms": round(avg_latency, 3),
            "median_latency_ms": round(median_latency, 3),
            "p95_latency_ms": round(p95, 3),
            "p99_latency_ms": round(p99, 3),
            "throughput_qps": round(throughput, 2),
            "peak_memory_mb": round(peak_memory, 2),
            "peak_cpu_percent": round(peak_cpu, 2),
        }
