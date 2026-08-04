# Benchmark Assumptions

This document records the assumptions made when designing and executing the Graph Database Cloud Benchmark. These assumptions help ensure transparency and improve the reproducibility of benchmark results.

---

## General Assumptions

- All databases are deployed using stable production releases.
- Each database is configured according to vendor recommendations unless otherwise documented.
- Identical benchmark datasets are used for every database.
- Identical benchmark queries are executed for each platform.
- No manual intervention occurs during benchmark execution.

---

## Hardware Assumptions

To ensure fair comparisons, benchmarks should be executed on equivalent hardware.

Recommended baseline:

| Component | Recommended Configuration |
|----------|----------------------------|
| CPU | Equal number of vCPUs |
| RAM | Equal memory allocation |
| Storage | SSD or NVMe |
| Network | Stable low-latency connection |
| Operating System | Ubuntu LTS |

Differences in hardware may significantly affect benchmark results.

---

## Dataset Assumptions

The generated dataset assumes:

- Randomly generated users
- Random companies
- Random products
- Random friendship graph
- Random purchases
- Random employment assignments

The synthetic dataset is intended to provide repeatable workloads rather than accurately model a real-world social network.

---

## Query Assumptions

Queries are designed to represent common graph operations:

1. Neighbor lookup
2. Multi-hop traversal
3. Recommendation
4. Shortest path
5. Aggregation

Where a database uses a language other than Cypher, queries should be translated to preserve equivalent logical behavior.

---

## Performance Assumptions

The benchmark assumes:

- Database caches are warmed after the configured warm-up runs.
- Query execution times include result retrieval.
- CPU and memory measurements represent the benchmark process and may not fully capture database server resource usage when running remotely.

---

## Cloud Deployment Assumptions

When benchmarking managed cloud services:

- All databases should be deployed in the same geographic region whenever possible.
- Similar compute tiers should be selected.
- Background maintenance operations are assumed to be minimal during benchmarking.

---

## Configuration Assumptions

The benchmark uses values defined in `config.yaml` for:

- Dataset size
- Number of warm-up runs
- Number of benchmark runs
- Query timeout
- Enabled databases
- Output locations

Changing these values may affect benchmark comparability.

---

## Result Interpretation

Benchmark results should be interpreted as comparative indicators under the tested configuration.

Performance observed in production environments may differ due to:

- Workload characteristics
- Data distribution
- Concurrent users
- Network latency
- Hardware differences
- Vendor-specific optimizations

---

## Reproducibility

To reproduce published results:

1. Use the same Git commit.
2. Use the same dataset generation parameters.
3. Use the same configuration file.
4. Use equivalent hardware.
5. Use the same database versions.
6. Execute the benchmark without modifying the query workload.

---

## Future Enhancements

Future versions of the benchmark may include:

- Larger datasets
- Concurrent client workloads
- Bulk import benchmarks
- Update and delete operations
- Mixed read/write workloads
- Distributed cluster benchmarking
- Additional graph database platforms

Any such changes should be documented to maintain consistency across benchmark versions.
