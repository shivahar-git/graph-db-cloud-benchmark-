#!/usr/bin/env python3
"""
Graph Database Cloud Benchmark

Main entry point for running benchmarks across supported graph databases.

Usage:
    python benchmark.py
"""

from pathlib import Path
import json
import time
import yaml
import pandas as pd

from benchmarks.neo4j_runner import Neo4jRunner
from benchmarks.memgraph_runner import MemgraphRunner
from benchmarks.tigergraph_runner import TigerGraphRunner
from benchmarks.kogniodb_runner import KognioDBRunner


CONFIG_FILE = "config.yaml"


def load_config():
    """Load YAML configuration."""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_output_directory(config):
    """Ensure output directory exists."""
    output_dir = Path(config["results"]["output_directory"])
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def benchmark_database(name, runner):
    """Execute benchmark for a single database."""
    print(f"\n{'=' * 60}")
    print(f"Benchmarking {name}")
    print("=" * 60)

    start = time.perf_counter()

    runner.connect()
    runner.load_dataset()
    result = runner.run_queries()
    runner.close()

    elapsed = time.perf_counter() - start

    result["database"] = name
    result["total_runtime_seconds"] = round(elapsed, 3)

    return result


def save_results(config, results):
    """Save benchmark results to CSV and JSON."""
    output_dir = Path(config["results"]["output_directory"])

    df = pd.DataFrame(results)

    csv_path = output_dir / config["results"]["csv_file"]
    json_path = output_dir / config["results"]["json_file"]

    df.to_csv(csv_path, index=False)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"\nResults saved:")
    print(f"CSV : {csv_path}")
    print(f"JSON: {json_path}")


def main():
    config = load_config()
    create_output_directory(config)

    runners = []

    if config["neo4j"]["enabled"]:
        runners.append(
            (
                "Neo4j",
                Neo4jRunner(config),
            )
        )

    if config["memgraph"]["enabled"]:
        runners.append(
            (
                "Memgraph",
                MemgraphRunner(config),
            )
        )

    if config["tigergraph"]["enabled"]:
        runners.append(
            (
                "TigerGraph",
                TigerGraphRunner(config),
            )
        )

    if config["cognodb"]["enabled"]:
        runners.append(
            (
                "KognioDB",
                KognioDBRunner(config),
            )
        )

    if not runners:
        print("No databases enabled in config.yaml.")
        return

    results = []

    overall_start = time.perf_counter()

    for name, runner in runners:
        try:
            results.append(
                benchmark_database(name, runner)
            )
        except Exception as exc:
            print(f"{name} benchmark failed:")
            print(exc)

    overall_end = time.perf_counter()

    save_results(config, results)

    print("\nBenchmark completed successfully.")
    print(
        f"Total execution time: "
        f"{overall_end - overall_start:.2f} seconds"
    )


if __name__ == "__main__":
    main()
