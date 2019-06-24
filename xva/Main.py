"""
Oneview Platform XVA output json viewer

From menu click file and selected xva output json. 

Result tree is generated for each currencies. Expand tree and select netting set or 
leaf node to see non-vector measures  
"""

import locale
import sys

from PyQt5.QtCore import QDir

from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtGui import QIcon

from constants import *
from XvaResultTreeViewBuilder import XvaResultTreeViewBuilder
from ExposureViewBuilder import ExposureViewBuilder
from LoginDialog import LoginDialog
from XvaCalcResultDownloaderViewBuilder import XvaCalcResultDownloaderViewBuilder

# Set Locale
# locale.setlocale(locale.LC_NUMERIC, 'English')


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        # QCoreApplication.setAttribute(Qt.AA_DontUseNativeMenuBar)
        # Main Window Settings
        self.setWindowTitle('Counterparty Risk Results Viewer')
        # Menus
        self.build_cpty_risk_menu()
        # Tool Bar
        self.build_toolbar()
        # Tab Widget
        self.tabs = QTabWidget()
        # Widgets
        self.exposure_widget_builder = ExposureViewBuilder()
        self.expTabIdx = self.tabs.addTab(self.exposure_widget_builder, MAIN_TAB_EXPOSURE_RESULTS)
        self.xva_widget_builder = XvaResultTreeViewBuilder()
        self.xvaTabIdx = self.tabs.addTab(self.xva_widget_builder, MAIN_TAB_XVA_RESULTS)
        # Dialogs
        self.login_dialog = LoginDialog()
        self.xva_calc_runs = XvaCalcResultDownloaderViewBuilder()
        # Set main widget to window
        self.setCentralWidget(self.tabs)
        self.showMaximized()

    def build_cpty_risk_menu(self):
        self.setStyleSheet("""QMenuBar {background-color: silver;}""")
        # self.menuBar().setNativeMenuBar(False)
        cpty_risk_menu = self.menuBar().addMenu('Counterparty Risk')
        exposure_json_file_menu_item = QAction(QIcon('open.png'), 'Open Exposure Results', self)
        exposure_json_file_menu_item.setShortcut('Ctrl+O')
        exposure_json_file_menu_item.setStatusTip('Open Exposure Results JSON file')
        exposure_json_file_menu_item.triggered.connect(self.open_exposure_json)
        cpty_risk_menu.addAction(exposure_json_file_menu_item)
        xva_json_file_menu_item = QAction(QIcon('open.png'), 'Open XVA Results', self)
        xva_json_file_menu_item.setShortcut('Ctrl+O')
        xva_json_file_menu_item.setStatusTip('Open XVA Results JSON file')
        xva_json_file_menu_item.triggered.connect(self.open_xva_json)
        cpty_risk_menu.addAction(xva_json_file_menu_item)

    def build_toolbar(self):
        self.toolbar = self.addToolBar('Default')
        # MI
        xva_calc_results_btn = QAction(QIcon('icons/results.png'), 'XVA Calc Results', self)
        xva_calc_results_btn.setShortcut('Ctrl+R')
        xva_calc_results_btn.triggered.connect(self.download_xva_calc_results)
        self.toolbar.addAction(xva_calc_results_btn)
        self.toolbar.addSeparator()
        # MI
        open_exposure_action = QAction(QIcon('icons/exposure.png'), 'Open exposure json file', self)
        open_exposure_action.setShortcut('Ctrl+E')
        open_exposure_action.triggered.connect(self.open_exposure_json)
        self.toolbar.addAction(open_exposure_action)
        # MI
        download_bulk_stores_btn = QAction(QIcon('icons/download.png'), 'Download Bulk Stores', self)
        download_bulk_stores_btn.setShortcut('Ctrl+D')
        download_bulk_stores_btn.triggered.connect(self.download_bulk_stores)
        self.toolbar.addAction(download_bulk_stores_btn)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        # MI
        open_xva_action = QAction(QIcon('icons/xva.png'), 'Open xva json file', self)
        open_xva_action.setShortcut('Ctrl+X')
        open_xva_action.triggered.connect(self.open_xva_json)
        self.toolbar.addAction(open_xva_action)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        # MI
        exit_action = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)
        self.toolbar.addAction(exit_action)
        self.toolbar.addSeparator()

    def open_exposure_json(self):
        #f_name = QFileDialog.getOpenFileName(self, 'Select Exposure Results JSON', QDir.homePath() + "/AppData/Local/Temp/ov/xva/cas_exposure", "Json Files (*.json)")
        f_name = QFileDialog.getOpenFileName(self, 'Select Exposure Results JSON', BULKSTORE_DOWNLOAD_DIR, "Json Files (*.json)")
        if f_name[0]:
            print(f_name[0])
            try:
                self.exposure_widget_builder.build_model(f_name[0])
                self.tabs.setCurrentIndex(self.expTabIdx)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                print("Unexpected error:", sys.exc_info()[1])

    def open_xva_json(self):
        f_name = QFileDialog.getOpenFileName(self, 'Select XVA Results JSON', OV_CAS_RES_DIR, "Json Files (*.json)")
        if f_name[0]:
            print(f_name[0])
            self.xva_widget_builder.build_model(f_name[0])
            self.tabs.setCurrentIndex(self.xvaTabIdx)

    def download_bulk_stores(self):
        self.xva_widget_builder.download_bulk_stores()

    def download_xva_calc_results(self):
        if self.login_dialog.get_token() is None:
            token = self.login_dialog.exec_()
        if self.login_dialog.get_token() is not None:
            self.xva_calc_runs.exec_(self.login_dialog.get_token())


# Invoke main Window
if __name__ == "__main__":
    # Every PyQt5 application must create an application object
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

