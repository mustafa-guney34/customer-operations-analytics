
import pandas as pd

def add_features(df):

    # -----------------------------
    # Datetime conversions
    # -----------------------------
    df["arrival_window_start_time"] = pd.to_datetime(df["arrival_window_start_time"])
    df["arrival_window_end_time"] = pd.to_datetime(df["arrival_window_end_time"])
    df["on_site"] = pd.to_datetime(df["on_site"])
    df["submitted_at"] = pd.to_datetime(df["submitted_at"])

    # -----------------------------
    # Lateness flag
    # -----------------------------
    df["late"] = (df["on_site"] > df["arrival_window_end_time"]).astype(int)

    # -----------------------------
    # Delay in minutes
    # -----------------------------
    df["delay_minutes"] = (
        (df["on_site"] - df["arrival_window_end_time"])
        .dt.total_seconds() / 60
    )

    # Negative delays (on time) set to 0
    df.loc[df["delay_minutes"] < 0, "delay_minutes"] = 0

    # -----------------------------
    # Execution week (Monday start)
    # -----------------------------
    df["execution_week"] = (
        df["on_site"]
        .dt.to_period("W-MON")
        .dt.start_time
    )

    # -----------------------------
    # Customer not at home flag
    # -----------------------------
    df["customer_not_home"] = (df["customer_home"] == 0).astype(int)

    return df
