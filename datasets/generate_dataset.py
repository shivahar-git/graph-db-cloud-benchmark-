#!/usr/bin/env python3
"""
Synthetic Graph Dataset Generator

Generates a CSV containing nodes and relationships for benchmarking
graph databases.

Output:
    datasets/sample_dataset.csv
"""

from pathlib import Path
import csv
import random

from faker import Faker
import yaml


CONFIG_FILE = "config.yaml"
OUTPUT_FILE = "datasets/sample_dataset.csv"


def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def generate_users(count, fake):
    return [
        {
            "id": f"U{i}",
            "type": "User",
            "name": fake.name(),
        }
        for i in range(1, count + 1)
    ]


def generate_companies(count, fake):
    return [
        {
            "id": f"C{i}",
            "type": "Company",
            "name": fake.company(),
        }
        for i in range(1, count + 1)
    ]


def generate_products(count):
    return [
        {
            "id": f"P{i}",
            "type": "Product",
            "name": f"Product_{i}",
        }
        for i in range(1, count + 1)
    ]


def write_csv(users, companies, products):
    output_path = Path(OUTPUT_FILE)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(
            [
                "source_id",
                "relationship",
                "target_id",
            ]
        )

        # FRIEND_OF
        for _ in range(len(users) * 5):
            u1 = random.choice(users)["id"]
            u2 = random.choice(users)["id"]

            if u1 != u2:
                writer.writerow([u1, "FRIEND_OF", u2])

        # WORKS_AT
        for user in users:
            company = random.choice(companies)["id"]
            writer.writerow(
                [user["id"], "WORKS_AT", company]
            )

        # PURCHASED
        for _ in range(len(users) * 3):
            user = random.choice(users)["id"]
            product = random.choice(products)["id"]

            writer.writerow(
                [user, "PURCHASED", product]
            )


def main():
    random.seed(42)
    fake = Faker()
    Faker.seed(42)

    config = load_config()

    users = generate_users(
        config["dataset"]["nodes"]["users"],
        fake,
    )

    companies = generate_companies(
        config["dataset"]["nodes"]["companies"],
        fake,
    )

    products = generate_products(
        config["dataset"]["nodes"]["products"],
    )

    write_csv(users, companies, products)

    print(f"Dataset written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
