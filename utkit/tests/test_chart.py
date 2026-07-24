"""Single test file for chart functionality."""
from pathlib import Path

from utkit.visualize.charts.line import create_line_chart
from utkit.visualize.charts.bar import create_bar_chart


def test_line_chart_creation_and_view() -> None:
    """Test line chart creation and view the PNG file."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    sales = [120, 145, 138, 172, 185, 210, 345]

    # Use current file path as base directory
    current_file_path = Path(__file__).parent
    output_path = current_file_path / "monthly_sales.png"
    
    # Create the line chart
    result_path = create_line_chart(
        x=months,
        y=sales,
        title="Monthly Sales",
        xlabel="Month",
        ylabel="Sales",
        output_path=output_path,
        show=False,  # Don't show in notebook for testing
    )
    
    
    
    print(f"Line chart created successfully at: {result_path}")
    print(f"File size: {output_path.stat().st_size} bytes")
    
    # Clean up
    # output_path.unlink()


def test_bar_chart_creation_and_view() -> None:
    """Test bar chart creation and view the PNG file."""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [120, 145, 138, 172, 185, 210]

    current_file_path = Path(__file__).parent
    output_path = current_file_path / "monthly_sales_bar.png"

    # Create the bar chart
    result_path = create_bar_chart(
        x=months,
        y=sales,
        title="Monthly Sales",
        xlabel="Month",
        ylabel="Sales",
        output_path=output_path,
        show=False,
    )

    print(f"Bar chart created successfully at: {result_path}")
    print(f"File size: {output_path.stat().st_size} bytes")


test_line_chart_creation_and_view()
test_bar_chart_creation_and_view()