"""Plot the line chart for the provided data."""
from typing import Callable, List, Optional, Union

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# from matplotlib.cm import viridis
from data_processing import convert_time_to_minutes


def plot_average_time_in_mins_chart(
    data: List[List[str]], computer_names: List[str], test_names: List[str]
) -> None:
    """Plot the line chart for the provided data."""
    test_indices = np.arange(len(test_names))
    for i, comp_name in enumerate(computer_names):
        plt.plot(
            test_indices,
            [convert_time_to_minutes(time) for time in data[i]],
            label=comp_name,
        )

    plt.xticks(test_indices, test_names)
    plt.ylabel("Average Time in Mins")
    plt.legend()
    plt.show()


def plot_price_performance_chart(
    data: List[List[float]], computer_names: List[str], test_names: List[str]
) -> None:
    """Plot the price/performance ratio chart for the provided data."""
    test_indices = np.arange(len(test_names))

    # Set a custom color cycle
    colors = cm.get_cmap("viridis")(np.linspace(0, 1, len(computer_names)))
    plt.gca().set_prop_cycle(color=colors)

    for i, comp_name in enumerate(computer_names):
        plt.plot(
            test_indices, data[i], label=comp_name, marker="o"
        )  # Add markers to the data points

    plt.xticks(test_indices, test_names)
    plt.ylabel("Normalized Price/Performance Ratio")
    plt.legend()

    # Add a grid to the chart
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.show()


def plot_chart(
    data: List[List[Union[str, float]]],
    computer_names: List[str],
    test_names: List[str],
    ylabel: str,
    conversion_func: Optional[Callable[[Union[str, float]], Union[str, float]]] = None,
) -> None:
    """
    Plot the line chart for the provided data.

    Args:
        data: A list of lists containing the data for each computer and test.
        computer_names: A list of computer names.
        test_names: A list of test names.
        ylabel: The label for the y-axis.
        conversion_func: A function to convert data if needed.
        grid: A boolean flag to enable/disable grid in the chart.
    """
    test_indices = np.arange(len(test_names))
    colors = cm.get_cmap("viridis")(np.linspace(0, 1, len(computer_names)))
    plt.gca().set_prop_cycle(color=colors)

    for i, comp_name in enumerate(computer_names):
        current_data = data[i]
        if conversion_func:
            current_data = [conversion_func(time) for time in current_data]

        plt.plot(test_indices, current_data, label=comp_name, marker="o")

    plt.xticks(test_indices, test_names)
    plt.ylabel(ylabel)
    plt.legend()

    plt.grid(True, linestyle="--", alpha=0.6)

    plt.show()
