from os.path import isfile, isdir, join, basename
import json
from collections import OrderedDict


class Node:
    pass


class Measure:
    pass


def build_result_nodes(fn):
    nodes = list()

    if not fn or not isfile(fn):
        return nodes

    with open(fn, "r+") as f:
        data = json.load(f)
        results = data['results']
        # print("results length : ", len(results))
        for r in results:
            node = Node()
            node.resultType = r['resultType']
            print(r['resultKey'])
            node.calcType = r['calculationType']
            if 'tradeId' in r:
                node.tradeId = r['tradeId']
            if 'groupKey' in r:
                node.groupKey = r['groupKey']
            rk = r['resultKey']
            if '-' in rk and ':' in rk:
                node.params = rk.rsplit('-')[0].split(':')[1]
            else:
                node.params = ""
            node.measures = OrderedDict()
            for m in r['measures']:
                msr = Measure()
                msr.name = m['measureKey']
                msr.value = m['measureValue']
                msr.currency = m['currency'] if 'currency' in m else 'NA'
                node.currency = msr.currency
                node.measures[msr.name] = msr
            nodes.append(node)
    return nodes
