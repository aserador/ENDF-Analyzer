import pandas as pd

def compute_average(df, category, min_energy, max_energy, y_value):
    """
    Computes the average y-value for a given category and energy range.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - category (str): The category of the data to compute the average for.
    - min_energy (float): The minimum energy for the range.
    - max_energy (float): The maximum energy for the range.
    - y_value (string): The name of the y-value to be averaged.

    Returns:
    float: The average cross section for the given category and energy range.
    """
    category_df = df.loc[category]
    energy_range = category_df[(category_df['energy (eV)'] >= min_energy) & (category_df['energy (eV)'] <= max_energy)]
    average = energy_range[y_value].mean()
    return average
