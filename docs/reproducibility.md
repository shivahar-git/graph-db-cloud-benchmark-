# Reproducibility Guide

## Purpose

This guide explains how to reproduce the benchmark results from scratch using the contents of this repository.

The goal is to make every benchmark run transparent, repeatable, and comparable across environments.

---

# Prerequisites

Install the following software:

- Python 3.11 or newer
- Docker
- Docker Compose
- Git

Verify the installations:

```bash
python --version
docker --version
docker compose version
git --version
```

---

# Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/graph-db-cloud-benchmark.git

cd graph-db-cloud-benchmark
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure the Benchmark

Edit the configuration file:

```
config.yaml
```

Provide the correct connection details for each enabled database.

Example:

```yaml
neo4j:
  uri: bolt://localhost:7687
  username: neo4j
  password: password
```

Disable any database you are not benchmarking:

```yaml
enabled: false
```

---

# Start Local Databases (Optional)

If using the included Docker setup:

```bash
docker compose up -d
```

Wait until all services report healthy status before continuing.

---

# Generate the Dataset

Generate a fresh benchmark dataset:

```bash
python datasets/generate_dataset.py
```

The generated dataset will be written to:

```
datasets/sample_dataset.csv
```

---

# Execute the Benchmark

Run the benchmark:

```bash
python benchmark.py
```

The benchmark will:

1. Connect to each enabled database.
2. Verify the dataset.
3. Execute warm-up runs.
4. Execute timed benchmark runs.
5. Collect latency, throughput, CPU, and memory metrics.
6. Export the results.

---

# Benchmark Outputs

The benchmark produces:

### CSV

```
results/benchmark_results.csv
```

### JSON

```
results/benchmark_results.json
```

---

# Generate Charts

Create visualizations from the benchmark results:

```bash
python analysis/plot_results.py
```

Generated charts are saved in:

```
analysis/graphs/
```

---

# Reproducing Published Results

To reproduce previously published benchmark results, ensure that the following remain unchanged:

- Git commit or release tag
- Database versions
- Python version
- Dataset configuration
- Query workload
- Hardware configuration
- Cloud region (for managed services)

Any differences should be documented when reporting results.

---

# Troubleshooting

## Connection Errors

Verify:

- Database is running.
- Credentials are correct.
- Firewall rules allow access.
- Connection URI is correct.

## Missing Dataset

Generate the dataset:

```bash
python datasets/generate_dataset.py
```

## Missing Results

Run:

```bash
python benchmark.py
```

before generating charts.

---

# Reporting Results

When sharing benchmark results, include:

- Repository version
- Database version(s)
- Operating system
- CPU
- RAM
- Storage type
- Cloud region (if applicable)
- Configuration changes
- Dataset size

Providing this information helps others reproduce and compare your findings accurately.

---

# Version History

Update this guide whenever changes are made that affect reproducibility, such as:

- New benchmark queries
- Additional database platforms
- Dataset schema changes
- Metric calculations
- Configuration options
