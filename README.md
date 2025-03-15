# Py IP Lookup Tool

## Overview
Py IP Lookup Tool is a Python-based command-line application for performing IP address lookups. It provides functionalities to check whether an IP belongs to a specific CIDR block and retrieve related network details.

## Features
- Lookup IP addresses against predefined CIDR blocks.
- Read and write IP data from CSV files.
- Easy integration into scripts for automated network analysis.

## Installation

### Clone the Repository
```sh
git clone https://github.com/nbutkowski/py-ip-lookup-tool.git
cd py-ip-lookup-tool
```

### Create a Virtual Environment
```sh
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

### Running the CLI Tool to check a single IP against a network
```sh
❯ python cli.py network-lookup 10.0.0.1 10.0.0.0/24
10.0.0.1 is in 10.0.0.0/24
❯ python cli.py network-lookup 10.0.0.1 10.0.1.0/24
10.0.0.1 is not in 10.0.1.0/24
```

### Bulk lookup
Reads in 2 files (see /in for examples) and outputs a third file where the list are joined.
```sh
python cli.py bulk-network-lookup data/in/hostname-ip-list.csv data/in/networkname-block-list.csv
```

## Running Tests
```sh
TBD
```

## License
This project is licensed under the MIT License.

