# Stages 2 and 3: regression answers

Source: all 150 observations in `austin_home_sales.csv`. Models were fitted with `statsmodels.formula.api.ols` in `fit.py`. Full summaries and labeled results are saved in `regression_results.txt`.

## Stage 2

1. **Square footage and distance.** Holding bedrooms, home age, and distance constant, one more square foot increases predicted sale price by about **$176**. Holding the other predictors constant, one more mile from downtown lowers predicted sale price by about **$9,900**. These are associations in the fitted model, not proof of causal effects.

2. **Statistical significance.** Bedrooms is the only predictor that is not statistically significant at 0.05: its p-value is **0.1197**. After accounting for square footage, age, and distance, the data do not provide enough evidence to reject a zero bedroom coefficient. This does not prove that bedrooms have no effect, are unimportant to buyers, or have no relationship with price on their own.

3. **R-squared.** The full model explains about **89.4% of the variation in sale prices among these 150 homes**. That is an in-sample fit measure, not 89.4% accuracy for every future listing. Adjusted R-squared is **0.891**.

4. **Typical error versus Stage 1.** The residual standard error is **$49,926**, compared with the Stage 1 sale-price standard deviation of **$151,076**: roughly one-third as large, a reduction of about **67%**. Residual standard error is `sqrt(model.mse_resid)`, using 145 residual degrees of freedom. Standard statsmodels `summary()` does not show this as a separate labeled line, so `fit.py` prints it explicitly. The coefficient table's `std err` column measures coefficient uncertainty, not the typical dollar error of a house prediction. These are training-data measures; performance on new sales has not been tested.

## Stage 3: the listing

The listing has 2,000 sq ft, 3 bedrooms, an age of 12 years, a distance of 2.5 miles from downtown, and a list price of $380,000.

- **Full model:** predicted price **$371,047**; predicted minus list price **−$8,953**; `should_buy` returns **False**.
- **Without bedrooms:** predicted price **$384,822**; predicted minus list price **+$4,822**; `should_buy_2` returns **True**. R-squared is **0.892**, adjusted R-squared is **0.890**, and residual standard error is **$50,173**.

The functions use the lab's rule: return True only if list price is strictly below the fitted predicted price. Equal prices return False. Predictions use the full fitted coefficients, not the rounded coefficients printed for readability.

## Stage 3 interpretation

1. **Why the flip matters.** A $4,822 to $8,953 gap is small relative to the models' roughly $50,000 residual error. Two models with nearly identical overall fit give opposite decisions, so the apparent bargain is sensitive to model choice. The point predictions alone provide weak support for a firm purchase decision; prediction uncertainty and other costs would matter in a real evaluation.

2. **Why the square-footage coefficient changes.** Bedrooms and square footage share information: bedrooms take up space, and larger houses tend to have more bedrooms. In the full model, the square-footage coefficient measures additional area while holding the number of bedrooms fixed. Removing bedrooms lets square footage also capture some of the price association previously assigned to bedroom count, raising its coefficient from about **$176 to $200**. The two coefficients therefore describe different comparisons.

3. **Which model I would hand over.** For this lab, I would choose the simpler model without bedrooms because it uses fewer predictors while preserving almost the same fit, while explaining that its narrow positive price gap is uncertain and its predictions still need validation on new sales.

## Run in Cursor

```bash
source .venv/bin/activate
python fit.py
```
