"""Plot the line chart for the provided data."""
from typing import Any, Callable, List, Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def plot_chart(
    data: List[List[float]],
    computer_names: List[str],
    test_names: List[str],
    ylabel: str,
    conversion_func: Optional[Callable[..., Any]] = None,
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
