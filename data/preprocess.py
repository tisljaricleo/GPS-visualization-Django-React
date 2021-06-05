import os
import pandas as pd


def add_time(x):
    """Adds '0' to the begining of string

    When hour is less than 10, time will be represented as 95320 (9h 53m 20s).
    In this case '0' must be added infront for formating purposes.

    Args:
        x (str): Input time

    Returns:
        str: Original time or with '0' in first index
    """
    if len(str(x)) == 5:
        return "0" + str(x)
    return x


def clean_data(data_path, save_path, min_rows):
    """Cleans provided dataset

    Args:
        data_path (str): Path to folder with CSVs.
        save_path (str): Path to folder with preprocessed data.
        min_rows (int): Minimal number of GPS records in one file.

    Returns:
        None: If something went wrong, void instead.
    """
    for file_name in os.listdir(data_path):

        # For debugging
        # print(file_name)

        if file_name.endswith("CSV"):

            file_path = data_path + str(file_name)

            headers = [
                "TAG",
                "DATE",
                "TIME",
                "LATITUDE",
                "LONGITUDE",
                "HEIGHT",
                "SPEED",
                "HEADING",
                "FIX MODE",
                "VALID",
                "PDOP",
                "HDOP",
                "VDOP",
                "VOX",
            ]

            try:
                data = pd.read_csv(
                    file_path, sep=",", index_col=0, skiprows=1, names=headers
                )
            except Exception as ex:
                print("Failed to read CSV file! Error: {0}".format(str(ex)))
                return None

            # Checks if number of rows is larger than min_rows
            row_count = data.shape[0]
            if row_count < min_rows:
                print("Skipping CSV with rowcount < {0}".format(min_rows))
                continue

            # Adds '0' to timestrings that are too short
            data["TIME"] = data["TIME"].map(add_time)

            # Combine date and time into one column
            data["DATETIME"] = pd.to_datetime(
                data["DATE"].astype("str") + " " + data["TIME"].astype("str"),
                yearfirst=True,
            )

            # Drop unused columns
            data = data.drop(["DATE", "TIME", "VOX"], axis=1)

            # Clean latitude column
            data["LATITUDE"] = (
                data["LATITUDE"].map(lambda x: x.rstrip("N"))
            ).astype("float")

            # Clean longitude column
            data["LONGITUDE"] = (
                data["LONGITUDE"].map(lambda x: x.rstrip("E").lstrip("0"))
            ).astype("float")

            data.drop_duplicates(keep=False, inplace=True)

            data.to_pickle(save_path + file_name.split(".")[0] + ".pkl")


data_folder = r"./original/"
save_folder = r"./preprocessed/"
# clean_data(data_folder, save_folder, min_rows=20)


for file_name in os.listdir(save_folder):

    file_path = save_folder + str(file_name)

    data = pd.read_pickle(file_path)
    print()
