from pathlib import Path

import matplotlib.pyplot as plt


def create_line_chart(
    x: list[int | float],
    y: list[int | float],
    output_path: str | Path,
    *,
    title: str = "Line Chart",
    xlabel: str = "",
    ylabel: str = "",
    figsize: tuple[int, int] = (10, 5),
    dpi: int = 300,
    marker: str = "o",
    linewidth: float = 2.0,
    grid: bool = True,
    show: bool = False,
) -> Path:
    """
    Create a line chart and save it as a PNG.

    Args:
        x: X-axis values.
        y: Y-axis values.
        output_path: Path to save the PNG.
        title: Chart title.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        figsize: Figure size in inches.
        dpi: Image resolution.
        marker: Marker style.
        linewidth: Line width.
        grid: Show grid.
        show: Display chart in notebook.

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
        ax.plot(x, y, marker=marker, linewidth=linewidth)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if grid:
            ax.grid(True)

        fig.tight_layout()
        fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    finally:
        plt.close(fig)

    if show:
        plt.show()

    return output_path