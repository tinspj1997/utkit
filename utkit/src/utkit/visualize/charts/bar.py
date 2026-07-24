from pathlib import Path

import matplotlib.pyplot as plt


def create_bar_chart(
    x: list[str | int | float],
    y: list[int | float],
    output_path: str | Path,
    *,
    title: str = "Bar Chart",
    xlabel: str = "",
    ylabel: str = "",
    figsize: tuple[int, int] = (10, 5),
    dpi: int = 300,
    color: str = "steelblue",
    edgecolor: str = "black",
    width: float = 0.6,
    grid: bool = True,
    show: bool = False,
) -> Path:
    """
    Create a bar chart and save it as a PNG.

    Args:
        x: X-axis labels.
        y: Bar values.
        output_path: PNG output path.
        title: Chart title.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        figsize: Figure size.
        dpi: Image resolution.
        color: Bar color.
        edgecolor: Border color.
        width: Bar width.
        grid: Show horizontal grid.
        show: Display chart.

    Returns:
        Path to the saved PNG.

    Raises:
        ValueError: If x and y have different lengths or are empty.
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")

    if len(x) == 0:
        raise ValueError("x and y must not be empty.")

    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=figsize)
    try:
        ax.bar(x, y, color=color, edgecolor=edgecolor, width=width)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if grid:
            ax.grid(axis="y", linestyle="--", alpha=0.4)

        fig.tight_layout()
        fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    finally:
        plt.close(fig)

    if show:
        plt.show()

    return output_path