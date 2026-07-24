---
icon: lucide/chart-bar
---

# Charts

The `utkit.visualize.charts` module provides chart creation utilities powered by [Matplotlib](https://matplotlib.org/). It supports bar charts and line charts with customizable styling, saved as high-resolution PNG images.

## Installation

`matplotlib` is part of the optional `vishualize` extras. Install `utkit` with the `vishualize` extra:

```bash
pip install "utkit[vishualize]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[vishualize]"
```

---

## Bar chart

Create a bar chart with `create_bar_chart`.

```python
from utkit.visualize.charts import create_bar_chart

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 145, 138, 172, 185, 210]

create_bar_chart(
    x=months,
    y=sales,
    output_path="monthly_sales.png",
    title="Monthly Sales",
    xlabel="Month",
    ylabel="Sales",
    color="steelblue",
    edgecolor="black",
    width=0.6,
    dpi=300,
    grid=True,
)
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `x` | `list[str \| int \| float]` | — | X-axis labels. |
| `y` | `list[int \| float]` | — | Bar values. |
| `output_path` | `str \| Path` | — | PNG output path. |
| `title` | `str` | `"Bar Chart"` | Chart title. |
| `xlabel` | `str` | `""` | X-axis label. |
| `ylabel` | `str` | `""` | Y-axis label. |
| `figsize` | `tuple[int, int]` | `(10, 5)` | Figure size in inches. |
| `dpi` | `int` | `300` | Image resolution. |
| `color` | `str` | `"steelblue"` | Bar fill color. |
| `edgecolor` | `str` | `"black"` | Bar border color. |
| `width` | `float` | `0.6` | Bar width. |
| `grid` | `bool` | `True` | Show horizontal grid lines. |
| `show` | `bool` | `False` | Display the chart interactively. |

### Returns

`Path` — The resolved path to the saved PNG file.

### Raises

- `ValueError` — If `x` and `y` have different lengths or are empty.

---

## Line chart

Create a line chart with `create_line_chart`.

```python
from utkit.visualize.charts import create_line_chart

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
sales = [120, 145, 138, 172, 185, 210, 345]

create_line_chart(
    x=months,
    y=sales,
    output_path="monthly_trend.png",
    title="Monthly Sales Trend",
    xlabel="Month",
    ylabel="Sales",
    marker="o",
    linewidth=2.0,
    dpi=300,
    grid=True,
)
```

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `x` | `list[int \| float]` | — | X-axis values. |
| `y` | `list[int \| float]` | — | Y-axis values. |
| `output_path` | `str \| Path` | — | Path to save the PNG. |
| `title` | `str` | `"Line Chart"` | Chart title. |
| `xlabel` | `str` | `""` | X-axis label. |
| `ylabel` | `str` | `""` | Y-axis label. |
| `figsize` | `tuple[int, int]` | `(10, 5)` | Figure size in inches. |
| `dpi` | `int` | `300` | Image resolution. |
| `marker` | `str` | `"o"` | Marker style. |
| `linewidth` | `float` | `2.0` | Line width. |
| `grid` | `bool` | `True` | Show grid. |
| `show` | `bool` | `False` | Display the chart interactively. |

### Returns

`Path` — The resolved path to the saved PNG file.

### Raises

- `ValueError` — If `x` and `y` have different lengths or are empty.