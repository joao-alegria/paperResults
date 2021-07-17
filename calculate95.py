#!/usr/bin/env python3
'''
@author: Vitor Cunha (vitorcunha@av.it.pt)
'''
import csv
import statistics
import sys
def __remove_outliers(values):
    values.sort()
    avg = statistics.mean(values)
    sigma = statistics.stdev(values)
    two_sigma = 2 * sigma
    lower_thr = avg - (2 * sigma)
    higher_thr = avg + (2 * sigma)
    out = list()
    for i in values:
        if i < lower_thr or i > higher_thr:
            continue
        out.append(i)
    return out
def __process_csv(path):
    # prepare the CSV reading
    csv_file = open(path, mode="r")
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()    # discard the header
    # read the CSV
    vals  = list()
    for row in csv_reader:
        # determine delta in ms
        val  = float(row[int(sys.argv[2])])
        vals.append(val)
    return vals
def main():
    vals = __process_csv(sys.argv[1])
    if len(vals) == 1:
        print(vals)
    elif len(vals) > 1:
        vals = __remove_outliers(vals)
        print(f"{[statistics.mean(vals), statistics.stdev(vals), vals[0], vals[-1]]}")
    else:
        print("error")
if __name__ == "__main__":
    main()