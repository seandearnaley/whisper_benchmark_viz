"""Main script for the chart plotter."""
from pathlib import Path

from chart_plotter import plot_chart
from data_loader import load_test_data
from data_processing import (
    PricePerformanceArgs,
    calculate_averages,
    calculate_price_performance_ratios,
    convert_seconds_to_minutes,
    log_transform_ratios,
)

# Load the data from the JSON file
data_file = Path("data.json")
(
    test_data,
    computer_names,
    power_usage_watts_per_computer,
    computer_rental_cost_per_hour,
    cost_per_kwh,
    test_names,
) = load_test_data(data_file)

averages = calculate_averages(test_data)

print("averages", averages)

plot_chart(
    averages,
    computer_names,
    test_names,
    ylabel="Average Time in Mins",
    conversion_func=convert_seconds_to_minutes,
)


price_performance_args = PricePerformanceArgs(
    power_usage_watts_per_computer=power_usage_watts_per_computer,
    computer_rental_cost_per_hour=computer_rental_cost_per_hour,
    cost_per_kwh=cost_per_kwh,
)

price_performance_ratios = calculate_price_performance_ratios(
    averages, price_performance_args
)

log_ratios = log_transform_ratios(price_performance_ratios)

print("price_performance_ratios", price_performance_ratios)
print("normalized_ratios", log_ratios)

plot_chart(
    log_ratios,
    computer_names,
    test_names,
    ylabel="Log Transformed Price/Performance Ratio",
)
