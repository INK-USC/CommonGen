#!/usr/bin/env python
# encoding: utf-8

import os

def order_output(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    print(len(lines))
    results = {}

    for i in range(len(lines)):
        if lines[i].startswith("S"):
            prediction = lines[i+2].split('\t')[2]
            lineno = int(lines[i+2].split('\n')[0].split('-')[1])
            results[lineno] = prediction

    results_list = []
    for i in range(len(results)):
        results_list.append(results[i])

    with open("final."+filename, 'w') as f:
        f.write('\n'.join(results_list))
for method in ["leven"]:
    for data_type in ["alpha", "reason", "simple"]:
        for set_type in ["dev", "test"]:
            filename = "%s.%s.%s.txt"%(method, data_type, set_type)
            print(filename)
            order_output(filename)
