import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_all_data(df, x_min, x_max, y_min, y_max, y_value):
    """
    Plots all data from a DataFrame.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data to be plotted.
    - x_min (float): The minimum value for the x-axis.
    - x_max (float): The maximum value for the x-axis.
    - y_min (float): The minimum value for the y-axis.
    - y_max (float): The maximum value for the y-axis.
    - y_value (string): The name of the y-value to be plotted.

    Returns:
    None
    """
    categories = df.index.get_level_values(0).unique()
    fig, ax = plt.subplots()
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    ax.set_xlabel('energy (eV)')
    ax.set_ylabel(y_value)
    ax.grid(True, which="both", ls="-", color='gray')

    for category in categories:
        category_df = df.loc[category]
        ax.plot(category_df['energy (eV)'], category_df[y_value], label=category)

    ax.legend()
    plt.show()

def plot_data(df, x_min, x_max, y_min, y_max, category, y_value):
    """
    Plots the data from a DataFrame.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - x_min (float): The minimum value for the x-axis.
    - x_max (float): The maximum value for the x-axis.
    - y_min (float): The minimum value for the y-axis.
    - y_max (float): The maximum value for the y-axis.
    - category (str): The category of the data to plot.
    - y_value (string): The name of the y-value to be plotted.

    Returns:
    None
    """
    fig, ax = plt.subplots()
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    ax.set_xlabel('energy (eV)')
    ax.set_ylabel(y_value)
    ax.grid(True, which="both", ls="-", color='gray')

    category_df = df.loc[category]
    ax.plot(category_df['energy (eV)'], category_df[y_value], label=category)

    ax.legend()
    plt.show()

def plot_several_data(df, x_min, x_max, y_min, y_max, categories, y_value):
    """
    Plots the data from a DataFrame for several categories.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - x_min (float): The minimum value for the x-axis.
    - x_max (float): The maximum value for the x-axis.
    - y_min (float): The minimum value for the y-axis.
    - y_max (float): The maximum value for the y-axis.
    - categories (list): A list of categories to plot.
    - y_value (string): The name of the y-value to be plotted.

    Returns:
    None
    """
    fig, ax = plt.subplots()
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])

    ax.set_xlabel('energy (eV)')
    ax.set_ylabel(y_value)
    ax.grid(True, which="both", ls="-", color='gray')

    for category in categories:
        category_df = df.loc[category]
        ax.plot(category_df['energy (eV)'], category_df[y_value], label=category)

    ax.legend()
    plt.show()

def print_category_names(df):
    """
    Prints the names of the categories in the DataFrame.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    categories = df.index.get_level_values(0).unique()
    for category in categories:
        print(category)


