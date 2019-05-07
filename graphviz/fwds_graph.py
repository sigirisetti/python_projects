from os.path import isfile, isdir, join, basename
import json
from collections import OrderedDict
from graphviz import Digraph


class Node:
    pass


class Measure:
    pass


def build_result_nodes(fn):
    if not fn or not isfile(fn):
        print("Invalid filename given")
        return

    dot = Digraph(comment='Fwd Pricer Graph')
    with open(fn, "r+") as f:
        data = json.load(f)
        p = data['children'][0]
        dot.node(p['name'], p['name'])
        c = p['children']
        build_hierarchy(p, c, dot)

    print(dot.source)
    dot.render('fwds/' + p['name'] + '.gv', view=True)


def build_hierarchy(p, c, dot):
    for c1 in c:
        dot.node(c1['name'], c1['name'])
        dot.edge(p['name'], c1['name'], constraint='false')
        if len(c1['children']) > 0:
            build_hierarchy(c1, c1['children'], dot)


build_result_nodes(r'c:\temp\fwds\dataproviders\fwdpts.json')