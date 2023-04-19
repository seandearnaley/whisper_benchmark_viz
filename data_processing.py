"""Data processing functions for the benchmarking project."""
import math
from typing import List

import numpy as np


def convert_time_to_minutes(time: str) -> float:
    """Convert a time string in the format mm:ss:msmsms to minutes."""
    minutes, seconds, milliseconds = map(
        float, time.split(":")[-2:] + time.split(".")[-1:]
    )
    return minutes + seconds / 60 + milliseconds / 60_000


def convert_time_to_seconds(time: str) -> float:
    """Convert a time string in the format mm:ss:msmsms to seconds."""
    minutes, seconds, milliseconds = map(
        float, time.split(":")[-2:] + time.split(".")[-1:]
    )
    return minutes * 60 + seconds + milliseconds / 1000


def convert_seconds_to_time(seconds: float) -> str:
    """Convert seconds to a time string in the format mm:ss:msmsms."""
    minutes, remainder = divmod(seconds, 60)
    seconds, milliseconds = divmod(remainder, 1)
    return f"{int(minutes):02d}:{int(seconds):02d}.{int(milliseconds * 1000):03d}"


def calculate_averages(data: List[List[List[str]]]) -> List[List[str]]:
    """Calculate the averages for the provided data."""
    data_seconds = [
        [[convert_time_to_seconds(time) for time in run] for run in comp]
        for comp in data
    ]

    averages_seconds = np.mean(data_seconds, axis=2)

    averages_time = [
        [convert_seconds_to_time(avg) for avg in comp] for comp in averages_seconds
    ]

    return averages_time


def calculate_price_performance_ratios(
    averages: List[List[str]],
    power_usage_watts_per_computer: List[float],
    computer_rental_cost_per_hour: List[float],
    cost_per_kwh: float,
    price_weight: float,
    performance_weight: float,
) -> List[List[float]]:
    """Calculate the price/performance ratios for the provided data."""
    price_performance_ratios = []
    for i, comp_averages in enumerate(averages):
        comp_ratios = []
        for avg_time in comp_averages:
            time_in_hours = convert_time_to_minutes(avg_time) / 60
            energy_cost = (
                power_usage_watts_per_computer[i] * time_in_hours * cost_per_kwh / 1000
            )
            rental_cost = computer_rental_cost_per_hour[i] * time_in_hours
            total_cost = (price_weight * energy_cost) + (
                performance_weight * rental_cost
            )
            performance = 1 / convert_time_to_seconds(avg_time)
            ratio = performance / total_cost
            comp_ratios.append(ratio)
        price_performance_ratios.append(comp_ratios)
    return price_performance_ratios


def log_transform_ratios(
    ratios: List[List[float]], base: float = 10
) -> List[List[float]]:
    """Log transform the provided ratios."""
    log_transformed_ratios = [
        [math.log(ratio, base) if ratio > 0 else 0 for ratio in comp_ratios]
        for comp_ratios in ratios
    ]
    return log_transformed_ratios
