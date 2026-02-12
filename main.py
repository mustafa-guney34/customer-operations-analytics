from src.data_loader import load_full_dataset
from src.feature_engineering import add_features
from src.analysis_nps import weekly_nps, nps_by_work_type
from src.analysis_lateness import (
    overall_lateness_rate,
    impact_on_customer_not_home
)
from src.regression_models import nps_regression


def main():

    print("\nCustomer Operations Analytics")
    print("-" * 40)

    # Load & prepare data
    df = load_full_dataset()
    df = add_features(df)

    print(f"Dataset loaded: {df.shape[0]} appointments")

    # -----------------------------
    # NPS Analysis
    # -----------------------------
    weekly = weekly_nps(df)
    worktype_nps = nps_by_work_type(df)

    print("\nNPS Insights")
    print("-" * 20)
    print("Lowest weekly NPS:",
          weekly.loc[weekly["avg_nps"].idxmin(), "execution_week"])

    print("NPS by Work Type:")
    for _, row in worktype_nps.iterrows():
        print(f"  {row['work_type']}: {round(row['nps'], 2)}")

    # -----------------------------
    # Lateness Analysis
    # -----------------------------
    lateness = overall_lateness_rate(df)
    impact = impact_on_customer_not_home(df)

    print("\nOperational Insights")
    print("-" * 20)
    print(f"Overall lateness rate: {lateness}%")

    late_no_show = impact.loc[impact["late"] == 1, "customer_not_home"].values[0]
    ontime_no_show = impact.loc[impact["late"] == 0, "customer_not_home"].values[0]

    print(f"Customer not home (on time): {round(ontime_no_show, 1)}%")
    print(f"Customer not home (late): {round(late_no_show, 1)}%")

    # -----------------------------
    # Regression Validation
    # -----------------------------
    model = nps_regression(df)

    repair_effect = model.params.get("work_type_repair", None)

    if repair_effect is not None:
        print("\nModel Validation")
        print("-" * 20)
        print(f"Repair appointments reduce NPS by ~{round(repair_effect, 2)} points (controlled).")

    print("\nAnalysis completed successfully.\n")


if __name__ == "__main__":
    main()
