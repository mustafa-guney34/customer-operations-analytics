import pandas as pd
import statsmodels.api as sm


# --------------------------------------------------
# Regression 1: Operational drivers of NPS (OLS)
# --------------------------------------------------

def nps_regression(df):
    """
    OLS regression:
    Impact of operational variables on NPS
    """

    # Select relevant columns
    df_model = df[
        [
            "nps",
            "late",
            "work_type",
            "years_in_service",
            "skill_level"
        ]
    ].copy()

    # Drop missing values
    df_model = df_model.dropna()

    # Create dummy variables for categorical columns
    df_model = pd.get_dummies(
        df_model,
        columns=["work_type", "skill_level"],
        drop_first=True
    )

    # Define X and y
    X = df_model.drop(columns="nps").astype(float)
    y = df_model["nps"].astype(float)

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    return model


# --------------------------------------------------
# Regression 2: Lateness → Customer Not Home (Logit)
# --------------------------------------------------

def lateness_customer_home_logit(df):
    """
    Logistic regression:
    Impact of lateness on customer_not_home
    """

    df_model = df[["customer_not_home", "late"]].copy()
    df_model = df_model.dropna()

    X = sm.add_constant(df_model[["late"]])
    y = df_model["customer_not_home"]

    model = sm.Logit(y, X).fit(disp=False)

    return model
