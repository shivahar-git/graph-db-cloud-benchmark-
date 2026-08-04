# Graph Database Cloud Benchmark

A reproducible benchmark comparing managed graph database cloud platforms using identical datasets, identical hardware assumptions, and identical query workloads.

## Objective

This project benchmarks multiple cloud-hosted graph databases using the same dataset and workload to provide a transparent comparison.

Platforms evaluated:

- CognoDB Cloud
- Neo4j AuraDB
- Memgraph Cloud
- TigerGraph Cloud

## Benchmark Goals

Measure:

- Data Loading Speed
- Query Latency
- Complex Traversal Performance
- Aggregation Performance
- Multi-hop Traversal
- Memory Consumption
- CPU Utilization
- Cost Efficiency

The benchmark is designed to be:

- Fair
- Repeatable
- Open Source
- Vendor Neutral

---

# Repository Structure

```
graph-db-cloud-benchmark/
├── benchmark.py
├── config.yaml
├── docker-compose.yml
├── requirements.txt
├── benchmarks/
├── datasets/
├── queries/
├── analysis/
├── docs/
├── results/
├── blog/
└── social/
```

---

# Dataset

Synthetic Social Network Dataset

Nodes

- User
- Company
- City
- Country
- Product
- Category

Relationships

- FRIEND_OF
- PURCHASED
- WORKS_AT
- LIVES_IN
- BELONGS_TO
- LOCATED_IN

Default size

100,000 Nodes

500,000 Relationships

The dataset generator is included in:

```
datasets/generate_dataset.py
```

---

# Benchmark Workload

## Query 1

Find direct friends.

## Query 2

Find friends-of-friends.

## Query 3

Recommend products based on purchase graph.

## Query 4

Shortest path.

## Query 5

Top companies by employee count.

---

# Metrics

Each benchmark records:

- Average latency
- Median latency
- P95 latency
- P99 latency
- Throughput (QPS)
- Data loading time
- Peak memory
- CPU usage

Results are exported to:

```
results/
```

---

# Requirements

Python 3.11+

Docker

Docker Compose

Neo4j Driver

Memgraph Driver

PyTigerGraph

Pandas

NumPy

Matplotlib

---

# Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/graph-db-cloud-benchmark.git

cd graph-db-cloud-benchmark
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Configuration

Edit

```
config.yaml
```

Provide credentials for each database.

Example

```yaml
neo4j:
  uri: bolt://localhost:7687
  username: neo4j
  password: password

memgraph:
  uri: bolt://localhost:7688

cognodb:
  endpoint: YOUR_ENDPOINT

tigergraph:
  host: YOUR_HOST
```

---

# Running Benchmarks

Generate dataset

```bash
python datasets/generate_dataset.py
```

Run benchmark

```bash
python benchmark.py
```

Generate graphs

```bash
python analysis/plot_results.py
```

---

# Output

CSV

```
results/benchmark_results.csv
```

JSON

```
results/benchmark_results.json
```

Charts

```
analysis/graphs/
```

---

# Methodology

The benchmark follows these rules:

- Same dataset
- Same queries
- Same warm-up
- Same repetitions
- Same measurement method
- No vendor-specific optimizations

This ensures a fair comparison.

---

# Reproducibility

Every benchmark can be reproduced using:

- Dataset generator
- Docker Compose
- Benchmark scripts
- Configuration file

No proprietary tools are required.

---

# License

MIT License.

---

# Contributions

Pull requests are welcome.

Please open an issue before making major changes.

---

# Author

Open-source benchmark created for evaluating managed graph database cloud services.
