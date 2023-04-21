"""Data processing functions for the benchmarking project."""
import math
from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class PricePerformanceArgs:
    """Dataclass for the price/performance arguments."""

    power_usage_watts_per_computer: List[float]
    computer_rental_cost_per_hour: List[float]
    cost_per_kwh: float
    price_weight: float = 1
    performance_weight: float = 1


def convert_time_to_seconds(time: str) -> float:
    """Convert a time string in the format [h]:mm:ss.000 to seconds."""
    minutes, seconds, milliseconds = map(
        float, time.split(":")[-2:] + time.split(".")[-1:]
    )
    return minutes * 60 + seconds + milliseconds / 1000


def convert_seconds_to_minutes(seconds: float) -> float:
    """Convert seconds to minutes."""
    return seconds / 60


def calculate_averages(data: List[List[List[str]]]) -> List[List[float]]:
    """Calculate the averages for the provided data."""
    data_seconds = [
        [[convert_time_to_seconds(time) for time in run] for run in comp]
        for comp in data
    ]

    averages_seconds = np.mean(data_seconds, axis=2)

    averages_time = [[avg for avg in comp] for comp in averages_seconds]

    return averages_time


def calculate_price_performance_ratios(
    averages: List[List[float]],
    args: PricePerformanceArgs,
) -> List[List[float]]:
    """Calculate the price/performance ratios for the provided data."""
    price_performance_ratios: List[List[float]] = []
    for i, comp_averages in enumerate(averages):
        comp_ratios: List[float] = []
        for avg_time in comp_averages:
            time_in_hours = convert_seconds_to_minutes(avg_time) / 60
            energy_cost = (
                args.power_usage_watts_per_computer[i]
                * time_in_hours
                * args.cost_per_kwh
                / 1000
            )
            rental_cost = args.computer_rental_cost_per_hour[i] * time_in_hours
            total_cost = (args.price_weight * energy_cost) + (
                args.performance_weight * rental_cost
            )
            performance = 1 / avg_time
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
