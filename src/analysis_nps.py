import pandas as pd

# --------------------------------------------------
# Weekly NPS trend
# --------------------------------------------------

def weekly_nps(df, min_responses=100):
    """
    Calculates average NPS per execution week.
    Filters weeks with at least min_responses surveys.
    """

    df_nps = df.dropna(subset=["nps"]).copy()

    weekly = (
        df_nps.groupby("execution_week")
        .agg(
            avg_nps=("nps", "mean"),
            volume=("nps", "count")
        )
        .reset_index()
        .sort_values("execution_week")
    )

    weekly = weekly[weekly["volume"] >= min_responses]

    return weekly


# --------------------------------------------------
# NPS by work type
# --------------------------------------------------

def nps_by_work_type(df):
    """
    Calculates average NPS per work type.
    """

    df_nps = df.dropna(subset=["nps"]).copy()

    result = (
        df_nps.groupby("work_type")["nps"]
        .mean()
        .reset_index()
        .sort_values("nps", ascending=False)
    )

    return result


# --------------------------------------------------
# NPS by expert experience
# --------------------------------------------------

def nps_by_experience(df):
    """
    Calculates average NPS by years in service.
    """

    df_nps = df.dropna(subset=["nps", "years_in_service"]).copy()

    result = (
        df_nps.groupby("years_in_service")["nps"]
        .mean()
        .reset_index()
        .sort_values("years_in_service")
    )

    return result
