import csv
import datetime
import argparse
import statistics


def generate_tree(line, output):
    """
        Fucntion that split data an put on different leaves and branches of tree where branches it's a part timeline
    :param line: raw line from csv files
    :param output: updated dictionary tree
    :return: return dictionary tree dates of values
    """
    if line[1] == '':
        return

    date = datetime.datetime.strptime(line[0], '%m/%d/%Y')
    if output.get(date.year) is None:
        output[date.year] = {date.month: [{date.day: line[1]}]}
    else:
        if output[date.year].get(date.month) is None:
            output[date.year][date.month] = [{date.day: line[1]}]
        else:
            output[date.year][date.month].append({date.day: line[1]})


def grouping(data, separator='day'):
    """
        Function which we grouping our data from tree by separator.
    :param data: dictionary tree that we want grouping
    :param separator: group type: "day", "month", "year"
    :return: list of tuples date and mean for year or month grouping, or just value for day
    """
    output = []
    results = dict(sorted(data.items()))

    if separator == 'year':

        for years in results:

            months = dict(sorted(results[years].items()))
            year_mean = []
            first_day_date = None
            first_month = None

            for month in months:
                if first_day_date is None:
                    first_day_date = list(months[month][::-1][0].items())[0][0]
                    first_month = month
                year_mean += [float(day.popitem()[1]) for day in months[month]]

            date = '{}/{}/{}'.format(first_day_date, first_month, years)
            output.append((date, '{0:.2f}'.format(statistics.mean(year_mean))))

    elif separator == 'month':

        for years in results:
            months = dict(sorted(results[years].items()))

            for month in months:
                first_day_date = list(months[month][::-1][0].items())[0][0]
                mean = "{0:.2f}".format(statistics.mean([float(day.popitem()[1]) for day in months[month]]))
                date ='{}/{}/{}'.format(first_day_date,month,years)
                output.append((date,mean))

    elif separator == 'day':
        for years in results:
            months = dict(sorted(results[years].items()))
            for month in months:
                for day_data in months[month][::-1]:
                    day = day_data.popitem()
                    date = '{}/{}/{}'.format(day[0],month,years)
                    output.append((date,day[1]))
    return output, separator


def extract(args, work_dir):
    """
        Main function that reead, run transformation function and write data
    :param args: Params that use which file load, and how group information
    :return:
    """
    with open(work_dir+'/IN_DATA/'+args.file_name) as f:
        results = {}
        raw_data = csv.reader(f)

        [next(raw_data,None) for _ in range(4)]
        header = next(raw_data)
        for line in raw_data:
            generate_tree(line, results)

    group_results, group_type = grouping(results, args.group)
    f_name = group_type + '_grouping.csv'

    with open(work_dir+'/OUT_DATA/'+f_name, 'w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(header)
        for line in group_results:
            csv_writer.writerow(line)


if __name__ == "__main__":
    import os
    work_dir = os.path.abspath(os.curdir)
    parser = argparse.ArgumentParser(description='Get some filename for data proceed')
    parser.add_argument('group', metavar='group_name', type=str, nargs='?',
                        default='day',
                        help='Type of grouping data')
    parser.add_argument('file_name', metavar='fname', type=str, nargs='?',
                        default='Henry_Hub_Natural_Gas_Spot_Price.csv',
                        help='use file for input')

    args = parser.parse_args()

    extract(args, work_dir)
