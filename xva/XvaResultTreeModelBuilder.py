import requests
import os, errno
import json

from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel


class XvaTreeModelBuilder:
    
    def __init__(self, result_nodes):
        self.model = QStandardItemModel()
        self.add_tree_items(self.model, result_nodes)

    def add_tree_items(self, parent, nodes):
        self.parsedData = nodes
        trade_id = ''
        for n in nodes:
            currency_node = self.get_currency_node(n)
            rt_node = self.find_or_append(currency_node, n.resultType)
            if hasattr(n, 'groupKey'):
                h_nodes = n.groupKey.split('|')
                trade_id = ''
            else:
                params = n.params.split(',')
                for p in params:
                    nvp = p.split('=')
                    if nvp[0] == 'MarginSet':
                        #print('Hierarchy Nodes : ', nvp[1])
                        h_nodes = nvp[1].rstrip('|').split('|')
                        trade_id = n.tradeId
                        #print('trade_id : ', trade_id)

            parent = rt_node
            for hn in h_nodes:
                if hn:
                    parent = self.find_or_append(parent, hn)
            if trade_id:
                parent = self.find_or_append(parent, str(trade_id))

            parent.setData(n)

    def get_currency_node(self, n):
        for r in range(self.model.rowCount(QModelIndex())):
            item = self.model.item(r, 0)
            if item.text() == n.currency:
                return item
        new_item = QStandardItem(n.currency)
        self.model.appendRow(new_item)
        return new_item

    def find_or_append(self, parent, child_name):
        for r in range(self.model.rowCount(self.model.indexFromItem(parent))):
            i = self.model.itemFromIndex(self.model.index(r, 0, parent.index()))
            if i.text() == child_name:
                return i
        new_item = QStandardItem(child_name)
        parent.appendRow(new_item)
        return new_item

    def get_model(self):
        return self.model

    def download_bulk_stores(self, file_name):
        locators = []
        if not self.parsedData:
            return locators
        for n in self.parsedData:
            rt = n.resultType
            #groupKey = n.groupKey
            if rt in ["CollateralAssetValues", "DiscountFactors", "FXDistributions", "HazardRateDFs", "PreMarginExposures"]:
                locator = n.measures['BulkStoreLocator'].value
                locators.append(locator)
        return locators

