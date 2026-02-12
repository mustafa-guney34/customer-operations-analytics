# --------------------------------------------------
# Overall Lateness Rate
# --------------------------------------------------

def overall_lateness_rate(df):
    """
    Calculates overall percentage of late appointments.
    """
    lateness_rate = df["late"].mean() * 100
    return round(lateness_rate, 2)


# --------------------------------------------------
# Lateness by Work Type
# --------------------------------------------------

def lateness_by_work_type(df):
    """
    Calculates lateness percentage per work type.
    """
    result = (
        df.groupby("work_type")["late"]
        .mean()
        .reset_index()
    )

    result["late"] = result["late"] * 100

    return result.sort_values("late", ascending=False)


# --------------------------------------------------
# Impact of Lateness on Customer Not Home
# --------------------------------------------------

def impact_on_customer_not_home(df):
    """
    Calculates percentage of customers not at home
    depending on lateness.
    """

    result = (
        df.groupby("late")["customer_not_home"]
        .mean()
        .reset_index()
    )

    result["customer_not_home"] = result["customer_not_home"] * 100

    return result
