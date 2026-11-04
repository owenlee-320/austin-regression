# Regression lab walkthrough: Austin home prices

By the end of this lab you have a fitted regression model in Python and a function that uses it to answer the PE firm's question: is this listing a good deal?

**You need:** Cursor, Python, and the file `austin_home_sales.csv` from Brightspace (150 rows, 5 columns: `Sale_Price`, `Sq_Footage`, `Bedrooms`, `Home_Age_Years`, `Dist_Downtown_Mi`).

**Most common issues**

1. `ModuleNotFoundError: statsmodels` (or pandas, matplotlib). Your venv is not active or the install did not run. Activate the venv and run the pip install from Stage 0 again.
2. The agent uses `sklearn` instead of `statsmodels`. sklearn does not print p-values. Tell it: "use statsmodels, not sklearn."
3. The agent writes a Jupyter notebook. Tell it: "a plain `.py` script, not a notebook."
4. The scatterplot window opens and the script stops. Close the plot window and the script continues. Or ask the agent to save the plot to a file instead of showing it.
5. Numbers differ from the checkpoint in the last digit. Rounding. Numbers differ a lot: the agent dropped rows, renamed columns, or fit the wrong y. Ask it to print `df.shape` and `df.columns`.

---

## Stage 0: set up and look at the data
1. Make a new repo `austin-regression` in `Documents`. Put `austin_home_sales.csv` inside it. Open the folder in Cursor.
2. Open a terminal (File → New Terminal). Create and activate a venv (>> source venv/bin/activate for Mac) then:

```
>> pip install pandas statsmodels matplotlib openpyxl
```

3. Prompt the agent:

> Write `explore.py` in this folder. It loads `austin_home_sales.csv` with pandas into a DataFrame called `df`, prints `df.shape`, prints `df.describe()` with all columns visible and no scientific notation, and makes a scatterplot of `Sale_Price` (y axis) against `Sq_Footage` (x axis) saved as `scatter.png`. Plain script, not a notebook. Do not use sklearn.

4. Run it:

```
>> python explore.py
```

**Checkpoint 0**

- `df.shape` is `(150, 5)`.
- The `describe()` table shows mean `Sale_Price` of about 322,000 and `Sq_Footage` from 816 to 3,084.
- Open `scatter.png`. Price rises with square footage and the trend is roughly a straight line.

---

## Stage 1: your best guess with no model

- A PE firm asks you what any given Austin house in this dataset costs. You have not fit anything yet. What number do you give them?
- How far off is that guess, typically? Which row of `describe()` tells you?

---

## Stage 2: fit the multiple regression

Prompt the agent:

> Write `fit.py`. Load `austin_home_sales.csv` with pandas. Using `statsmodels.formula.api.ols`, fit the model `Sale_Price ~ Sq_Footage + Bedrooms + Home_Age_Years + Dist_Downtown_Mi` and print the full `summary()`. Then print, on their own lines with labels and rounded to whole numbers: each coefficient, each p-value to 4 decimals, R-squared, and adjusted R-squared.

```
>> python fit.py
```

**Checkpoint 2**

| Term | Coefficient | p-value |
|---|---|---|
| Intercept | 52,049 | 0.010 |
| Sq_Footage | 176 | < 0.001 |
| Bedrooms | 15,440 | 0.120 |
| Home_Age_Years | -4,538 | < 0.001 |
| Dist_Downtown_Mi | -9,900 | < 0.001 |

R-squared 0.894, adjusted R-squared 0.891.

The `summary()` block has these in the `coef` and `P>|t|` columns. Find them before reading the labeled lines.

**Answer in your own words**

1. Holding the other three constant, what does one more square foot do to the predicted price? One more mile from downtown?
2. Which predictor is not statistically significant at α = 0.05? What does that mean, and what does it not mean?
3. What does R-squared = 0.894 mean in one sentence for the PE firm?
4. Compare the model's typical error (`summary()` reports it; ask the agent which line if you cannot find it) to your Stage 1 number.

---

## Stage 3: predict and decide

The PE firm's listing: 2,000 sq ft, 3 bedrooms, 12 years old, 2.5 miles from downtown. Listed at $380,000.

Prompt the agent:

> Add to `fit.py`. Write a function `predict_price(sq_footage, bedrooms, home_age_years, dist_downtown_mi)` that returns the fitted model's predicted sale price for one house. Write a function `should_buy(list_price, sq_footage, bedrooms, home_age_years, dist_downtown_mi)` that returns `True` when the list price is below the predicted price and `False` otherwise. Call both for a house with 2,000 sq ft, 3 bedrooms, 12 years old, 2.5 miles from downtown, listed at 380000, and print the predicted price, the list price, the difference, and the decision.

```
>> python fit.py
```

**Checkpoint 3a**

Predicted price about $371,000. List price $380,000. `should_buy` returns `False`.

### Refit with fewer covariates

Bedrooms was not significant in Stage 2. Refit without it and see what changes.

Prompt the agent:

> Add a second model to `fit.py`: `Sale_Price ~ Sq_Footage + Home_Age_Years + Dist_Downtown_Mi`. Print its coefficients, p-values, R-squared, and adjusted R-squared the same way as the first model. Add `predict_price_2` and `should_buy_2` that use this second model (they do not take a bedrooms argument). Call them for the same listing and print the same four lines.

```
>> python fit.py
```

**Checkpoint 3b**

| Term | Coefficient | p-value |
|---|---|---|
| Intercept | 64,238 | 0.001 |
| Sq_Footage | 200 | < 0.001 |
| Home_Age_Years | -4,570 | < 0.001 |
| Dist_Downtown_Mi | -9,438 | < 0.001 |

R-squared 0.892, adjusted R-squared 0.890. Predicted price about $385,000. `should_buy_2` returns `True`.

**Answer in your own words**

1. The decision flipped. Both models fit the same data almost equally well. What does that tell you about a $5,000 to $9,000 gap between list and predicted price?
2. Why did the `Sq_Footage` coefficient change from 176 to 200 when Bedrooms was removed? What is a bedroom made of?
3. Which model would you hand the PE firm, and in one sentence, why? Choosing between models like this is a topic for a later class. For now, write down your reasoning.

---

## Output

- `fit.py`: a fitted model and a function, `should_buy`, that turns a new input into a decision.
