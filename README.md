# Whisper Benchmark Viz

Article to accompany this code [Whisper Showdown @ Medium](https://seandearnaley.medium.com/427ce5f486ea)

This repository contains code for visualizing benchmarks comparing the execution time and cost for two different transcription models: [whisper.cpp](https://github.com/ggerganov/whisper.cpp) (CPU-based) and [openai-whisper](https://github.com/openai/whisper) (GPU-based using PyTorch). The code generates two charts: one for average execution time and the other for the log-transformed price/performance ratio.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/seandearnaley/whisper_benchmark_viz.git
cd whisper_benchmark_viz
```

2. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies using Poetry:

```bash
poetry install
```

## Usage

1. Activate the virtual environment:

```bash
poetry shell
```

2. Run the `main.py` script to generate the charts:

```bash
python main.py
```

This will display two charts: one for the average execution time (in minutes) and the other for the log-transformed price/performance ratio.

## Data

The benchmark data is stored in the `data.json` file. You can modify this file to include your own benchmark data for different computer configurations and test cases.

The JSON file contains the following fields:

- `test_data`: A list of lists containing the execution times for each computer and test.
- `computer_names`: A list of computer names.
- `power_usage_watts_per_computer`: A list of power usage in watts for each computer.
- `computer_rental_cost_per_hour`: A list of computer rental costs per hour.
- `cost_per_kwh`: The cost per kilowatt-hour for electricity.
- `test_names`: A list of test names.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements for this project.
