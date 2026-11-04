"""Stage 0: inspect the Austin home sales data and save a scatterplot."""
from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

BASE_DIR = Path(__file__).resolve().parent

def main():
    df = pd.read_csv(BASE_DIR / "austin_home_sales.csv")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 160)
    pd.set_option("display.float_format", "{:,.2f}".format)
    print("Data shape:", df.shape)
    print("\nDescriptive statistics:")
    print(df.describe().to_string())

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["Sq_Footage"], df["Sale_Price"], alpha=0.75, color="steelblue")
    ax.set_title("Austin home sales: sale price vs. square footage")
    ax.set_xlabel("Square footage (sq ft)")
    ax.set_ylabel("Sale price ($)")
    ax.yaxis.set_major_formatter(StrMethodFormatter("${x:,.0f}"))
    ax.grid(alpha=0.2)
    fig.text(0.12, 0.01, "Source: austin_home_sales.csv | 150 sales; dates not supplied", fontsize=8)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(BASE_DIR / "scatter.png", dpi=160)
    plt.close(fig)
    print("\nSaved scatter.png")

if __name__ == "__main__":
    main()
