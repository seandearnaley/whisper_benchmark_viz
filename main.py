"""Main script for the chart plotter."""
from pathlib import Path

from chart_plotter import plot_average_time_in_mins_chart, plot_price_performance_chart
from data_loader import load_test_data
from data_processing import (
    calculate_averages,
    calculate_price_performance_ratios,
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

# Process the data
averages = calculate_averages(test_data)


PRICE_WEIGHT = 1
PERFORMANCE_WEIGHT = 1

price_performance_ratios = calculate_price_performance_ratios(
    averages,
    power_usage_watts_per_computer,
    computer_rental_cost_per_hour,
    cost_per_kwh,
    PRICE_WEIGHT,
    PERFORMANCE_WEIGHT,
)

print("price_performance_ratios", price_performance_ratios)

log_ratios = log_transform_ratios(price_performance_ratios)
print("normalized_ratios", log_ratios)

plot_average_time_in_mins_chart(averages, computer_names, test_names)


# plot_chart(
#     averages,
#     computer_names,
#     test_names,
#     ylabel="Average Time in Mins",
#     conversion_func=convert_time_to_minutes,
# )

plot_price_performance_chart(log_ratios, computer_names, test_names)
