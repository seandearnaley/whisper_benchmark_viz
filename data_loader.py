"""Load test data from a JSON file."""
import json
from pathlib import Path
from typing import List, Tuple


def load_test_data(
    file_path: Path,
) -> Tuple[
    List[List[List[str]]], List[str], List[float], List[float], float, List[str]
]:
    """Load test data and related data from a JSON file."""
    with file_path.open("r") as file:
        data = json.load(file)

    test_data = data["test_data"]
    computer_names = data["computer_names"]
    power_usage_watts_per_computer = data["power_usage_watts_per_computer"]
    computer_rental_cost_per_hour = data["computer_rental_cost_per_hour"]
    cost_per_kwh = data["cost_per_kwh"]
    test_names = data["test_names"]

    return (
        test_data,
        computer_names,
        power_usage_watts_per_computer,
        computer_rental_cost_per_hour,
        cost_per_kwh,
        test_names,
    )
