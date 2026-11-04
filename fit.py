"""Stages 2 and 3: fit two OLS models and evaluate the lab listing."""
from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "austin_home_sales.csv")
model = smf.ols("Sale_Price ~ Sq_Footage + Bedrooms + Home_Age_Years + Dist_Downtown_Mi", data=df).fit()
model_2 = smf.ols("Sale_Price ~ Sq_Footage + Home_Age_Years + Dist_Downtown_Mi", data=df).fit()


def predict_price(sq_footage, bedrooms, home_age_years, dist_downtown_mi):
    house = pd.DataFrame({"Sq_Footage": [sq_footage], "Bedrooms": [bedrooms],
                          "Home_Age_Years": [home_age_years], "Dist_Downtown_Mi": [dist_downtown_mi]})
    return float(model.predict(house).iloc[0])


def should_buy(list_price, sq_footage, bedrooms, home_age_years, dist_downtown_mi):
    return list_price < predict_price(sq_footage, bedrooms, home_age_years, dist_downtown_mi)


def predict_price_2(sq_footage, home_age_years, dist_downtown_mi):
    house = pd.DataFrame({"Sq_Footage": [sq_footage], "Home_Age_Years": [home_age_years],
                          "Dist_Downtown_Mi": [dist_downtown_mi]})
    return float(model_2.predict(house).iloc[0])


def should_buy_2(list_price, sq_footage, home_age_years, dist_downtown_mi):
    return list_price < predict_price_2(sq_footage, home_age_years, dist_downtown_mi)


def print_model(label, fitted):
    print("\n" + label)
    print(fitted.summary())
    print("\nLabeled results:")
    for term in fitted.params.index:
        print(f"Coefficient ({term}): {fitted.params[term]:,.0f}")
        print(f"p-value ({term}): {fitted.pvalues[term]:.4f}")
    print(f"R-squared: {fitted.rsquared:.3f}")
    print(f"Adjusted R-squared: {fitted.rsquared_adj:.3f}")
    print(f"Residual standard error: ${fitted.mse_resid ** 0.5:,.0f}")


def print_listing(predicted, decision):
    list_price = 380000
    print(f"Predicted price: ${predicted:,.0f}")
    print(f"List price: ${list_price:,.0f}")
    print(f"Difference (predicted minus list): ${predicted - list_price:,.0f}")
    print(f"Should buy: {decision}")


def main():
    print("Data shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print_model("Model 1: all four predictors", model)
    print_listing(predict_price(2000, 3, 12, 2.5), should_buy(380000, 2000, 3, 12, 2.5))
    print_model("Model 2: without Bedrooms", model_2)
    print_listing(predict_price_2(2000, 12, 2.5), should_buy_2(380000, 2000, 12, 2.5))


if __name__ == "__main__":
    main()
