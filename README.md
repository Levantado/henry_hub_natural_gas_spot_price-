# Henry Hub Natural Gas Spot Price 
### since  01.07.1997 - 03.17.2020

henry_hub_natural_gas_spot_price
## Data

Data comes from the [EIA U.S. Energy Information Administration](https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm)

We extract this data and normalize into 3 files:
*days date format (dd/mm/YYYY)*

* day_grouping.csv - the main file

* month_grouping.csv - the normalizing and grouping data by months 

* year_grouping.csv - the normalizing and grouping data by years

## Preparation

*Script didn't use and external libs or modules that not include in common Python3 and can runs in any environment without installation requirements like Pandas, Numpy or other DataScience libs.*

**USAGE:**
`python script/pretty_csv_group.py`

Args for script by default doesn't neccessery needen.

positional arguments:
  group_name  Type of grouping data
  fname       use file for input

* group_name - day, month, year *(by default day)*

* fname - any csv files *(by default Henry_Hub_Natural_Gas_Spot_Price.csv)*

##  License
This Data Package is licensed by its maintainers under the [Public Domain Dedication and License (PDDL).](https://opendatacommons.org/licenses/pddl/1.0/)