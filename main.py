from utils.data import parse_data
from utils.plotting import plot_all_data, plot_data, plot_several_data, print_category_names
from utils.computing import compute_average

### MODIFY VARIABLES HERE ###
DATA_FILE = 'data/graph.plot'
x_min = 1.0e-5
x_max = 2.0e+7
y_min = 1.0e-4
y_max = 1.0e+6

AVERAGE_MIN_ENERGY = 1.0e+5
AVERAGE_MAX_ENERGY = 1.0e+7
##############################

### MODIFY BELOW IF NECESSARY ###
df, y_value = parse_data(DATA_FILE).values()

print('Category names:')
print_category_names(df)

# Get a list of all unique categories
categories = df.index.get_level_values(0).unique()

# Loop over the categories and compute the average for each one
for category in categories:
    average = compute_average(df, category, AVERAGE_MIN_ENERGY, AVERAGE_MAX_ENERGY, y_value)
    print(f'Average of {y_value} for category {category} ({AVERAGE_MIN_ENERGY} to {AVERAGE_MAX_ENERGY}):', average)

plot_all_data(df, x_min, x_max, y_min, y_max, y_value)
