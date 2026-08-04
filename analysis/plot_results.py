#!/usr/bin/env python3
"""
Benchmark Results Visualization

Reads benchmark results from CSV and generates comparison charts.

Output:
    analysis/graphs/
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


RESULTS_FILE = "results/benchmark_results.csv"
OUTPUT_DIR = Path("analysis/graphs")


def load_results():
    """Load benchmark results."""
    csv_path = Path(RESULTS_FILE)

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Benchmark results not found: {RESULTS_FILE}"
        )

    return pd.read_csv(csv_path)


def save_bar_chart(df, metric, filename, title, ylabel):
    """Generate a bar chart for a given metric."""
    plt.figure(figsize=(8, 5))

    plt.bar(df["database"], df[metric])

    plt.title(title)
    plt.xlabel("Database")
    plt.ylabel(ylabel)

    plt.tight_layout()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plt.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.close()


def main():
    df = load_results()

    save_bar_chart(
        df,
        metric="average_latency_ms",
        filename="average_latency.png",
        title="Average Query Latency",
        ylabel="Milliseconds",
    )

    save_bar_chart(
        df,
        metric="throughput_qps",
        filename="throughput.png",
        title="Throughput",
        ylabel="Queries / Second",
    )

    save_bar_chart(
        df,
        metric="peak_memory_mb",
        filename="memory_usage.png",
        title="Peak Memory Usage",
        ylabel="MB",
    )

    save_bar_chart(
        df,
        metric="peak_cpu_percent",
        filename="cpu_usage.png",
        title="Peak CPU Usage",
        ylabel="CPU %",
    )

    print(f"Charts saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
