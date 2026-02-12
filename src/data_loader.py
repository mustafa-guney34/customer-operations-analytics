import pandas as pd

DATA_PATH = "data/"

def load_full_dataset():

    # Load raw data
    serviceappointments = pd.read_csv(DATA_PATH + "serviceappointments.csv")
    experts = pd.read_csv(DATA_PATH + "experts.csv")
    nps = pd.read_csv(DATA_PATH + "nps.csv")

    # Merge experts
    df = serviceappointments.merge(
        experts,
        on="serviceresource_id",
        how="left"
    )

    # Merge NPS
    df = df.merge(
        nps,
        on="serviceappointment_id",
        how="left"
    )

    return df
