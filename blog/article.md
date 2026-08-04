# Benchmarking Cloud Graph Databases: An Open and Reproducible Comparison

## Introduction

Graph databases have become a key technology for applications that rely on highly connected data, such as recommendation engines, fraud detection, social networks, cybersecurity, and knowledge graphs. As more organizations adopt managed cloud offerings, selecting the right platform requires objective performance evaluation rather than relying solely on vendor claims.

This project provides an open-source benchmark for comparing multiple graph database platforms under the same workload.

---

## Why This Benchmark?

Cloud graph databases often differ in:

- Query performance
- Data ingestion speed
- Resource consumption
- Scalability
- Cost
- Operational complexity

A standardized benchmark helps developers and architects evaluate these trade-offs using a consistent methodology.

---

## Benchmark Design

The benchmark follows several guiding principles:

- Identical synthetic dataset
- Identical logical query workload
- Configurable benchmark parameters
- Automated execution
- Automated result export
- Automated chart generation

All benchmark configuration is stored in a single `config.yaml` file.

---

## Dataset

The benchmark generates a synthetic social-network graph containing entities such as:

- Users
- Companies
- Products
- Cities
- Countries
- Categories

Relationships include:

- FRIEND_OF
- WORKS_AT
- PURCHASED
- LIVES_IN
- BELONGS_TO
- LOCATED_IN

The dataset size is configurable, allowing the benchmark to scale from small local tests to much larger experiments.

---

## Workload

Five representative graph workloads are included:

1. Direct neighbor lookup
2. Friends-of-friends traversal
3. Product recommendation
4. Shortest-path search
5. Aggregation by company

These operations reflect common graph database use cases while remaining easy to understand and reproduce.

---

## Metrics Collected

For each enabled database, the benchmark reports:

- Average latency
- Median latency
- P95 latency
- P99 latency
- Throughput
- Peak memory usage
- Peak CPU utilization
- Total benchmark execution time

Results are exported in both CSV and JSON formats for further analysis.

---

## Visualization

A companion analysis script reads benchmark results and produces charts illustrating:

- Average latency
- Throughput
- Memory usage
- CPU utilization

These visualizations simplify comparison across database platforms.

---

## Continuous Benchmarking

The repository includes a GitHub Actions workflow that can automatically:

- Generate a fresh dataset
- Execute benchmarks
- Produce visualizations
- Upload benchmark artifacts

This enables reproducible benchmarking as the project evolves.

---

## Limitations

Benchmark results should always be interpreted within the context of the tested environment.

Performance may vary due to:

- Hardware
- Cloud region
- Network latency
- Dataset characteristics
- Database version
- Vendor-specific optimizations

For meaningful comparisons, all benchmark conditions should be documented.

---

## Contributing

Contributions are welcome.

Possible future enhancements include:

- Larger datasets
- Concurrent client workloads
- Mixed read/write benchmarks
- Bulk import performance
- Cluster benchmarking
- Additional graph database platforms
- More advanced graph algorithms

---

## Conclusion

A transparent and reproducible benchmarking process helps the community evaluate graph databases using consistent criteria. By publishing the dataset generator, benchmark scripts, query workload, and analysis tools together, this project aims to make performance comparisons easier to verify, reproduce, and extend.
