# Stage 1: best guess with no model

1. **What price would I give the PE firm?** I would use **$322,240**, the mean sale price in this dataset. Without information about an individual house, the sample mean is my baseline prediction; it minimizes the sum of squared prediction errors for these 150 sales.

2. **How far off is that guess, typically?** The `std` row of `df.describe()` gives a sale-price standard deviation of **$151,075.77**, or about **$151,076**. This describes the spread of prices around the mean and is the lab's baseline measure of typical error. It is not the average absolute error and does not mean every prediction is off by this amount.

## Stage 0 checkpoint

- Data shape: **(150, 5)**; all five columns have 150 values.
- Mean sale price: **$322,240**.
- Square footage ranges from **816 to 3,084 sq ft**.
- `scatter.png` shows that larger houses generally sell for more, with a roughly linear upward trend and substantial spread around it.

Run the exploration in the Cursor terminal:

```bash
source .venv/bin/activate
python explore.py
```
