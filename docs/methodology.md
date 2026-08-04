# Benchmark Methodology

## Overview

This document describes the methodology used in the Graph Database Cloud Benchmark to ensure results are consistent, reproducible, and as fair as practical across supported graph database platforms.

---

# Objectives

The benchmark evaluates graph database performance across common graph workloads, including:

- Dataset loading
- Direct graph traversal
- Multi-hop traversal
- Recommendation queries
- Shortest path computation
- Aggregation queries

Performance metrics include:

- Average query latency
- Median latency
- P95 latency
- P99 latency
- Throughput (QPS)
- Peak memory usage
- Peak CPU utilization
- Total benchmark execution time

---

# Test Environment

All databases should be tested under equivalent conditions whenever possible.

Recommended configuration:

| Component | Recommendation |
|-----------|----------------|
| CPU | Same number of vCPUs |
| Memory | Same RAM allocation |
| Storage | SSD/NVMe |
| Operating System | Ubuntu LTS |
| Python | 3.11+ |
| Docker | Latest stable release |

---

# Dataset

The benchmark uses a synthetic social-network graph.

### Node Types

- User
- Company
- Product
- City
- Country
- Category

### Relationship Types

- FRIEND_OF
- PURCHASED
- WORKS_AT
- LIVES_IN
- BELONGS_TO
- LOCATED_IN

Dataset sizes are configurable through `config.yaml`.

---

# Benchmark Procedure

Each query follows the same execution process:

1. Connect to the database.
2. Load (or verify) the dataset.
3. Execute warm-up runs.
4. Execute timed benchmark runs.
5. Record latency for each execution.
6. Collect CPU and memory statistics.
7. Export results.

---

# Warm-up

Warm-up executions reduce the impact of:

- JIT compilation
- Query plan generation
- Cache initialization
- Connection startup overhead

Warm-up runs are **not** included in reported metrics.

---

# Timed Runs

Each benchmark query is executed multiple times.

The default configuration is:

- Warm-up runs: 5
- Measured runs: 30

These values can be changed in `config.yaml`.

---

# Metrics

## Average Latency

Arithmetic mean of measured execution times.

## Median Latency

50th percentile execution time.

## P95 Latency

95% of executions complete at or below this value.

## P99 Latency

99% of executions complete at or below this value.

## Throughput

Calculated as:

```
1000 / average_latency_ms
```

Approximate queries processed per second.

---

# Fairness Principles

To maximize fairness:

- Identical datasets
- Identical query logic
- Same benchmark script
- Same warm-up policy
- Same measurement methodology
- No vendor-specific query tuning unless explicitly documented

---

# Reproducibility

A benchmark run can be reproduced using:

- Repository source code
- Dataset generator
- Configuration file
- Docker Compose environment
- Query files
- Analysis scripts

---

# Limitations

This benchmark is intended as a comparative framework.

Results may vary depending on:

- Hardware
- Network latency
- Cloud region
- Database version
- Dataset size
- Vendor-specific optimizations

All benchmark reports should include the environment in which they were executed.

---

# Versioning

Benchmark methodology changes should be tracked through version control.

Significant methodology updates should be documented in release notes to preserve result comparability across benchmark versions.
