import sys

from PyQt5.QtCore import QUrl

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWebKitWidgets import QWebView


class BaseWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.centralWidget = QWidget()
        self.resize(800, 500)
        self.setWindowTitle('Test')
        self.tabs = QTabWidget()

        self.tabs.blockSignals(True) #just for not showing the initial message
        self.tabs.currentChanged.connect(self.onChange) #changed!


        self.webview = QWebView()
        self.webview.load(QUrl("http://gmx.de"))

        self.webview2 = QWebView()
        self.webview2.load(QUrl("http://web.de"))

        centralLayout = QVBoxLayout()
        centralLayout.addWidget(self.tabs, 1)

        self.tabs.addTab(self.webview, "gmx")
        self.tabs.addTab(self.webview2, "web")
        self.centralWidget.setLayout(centralLayout)

        self.setCentralWidget(self.centralWidget)

        self.tabs.blockSignals(False) #now listen the currentChanged signal


    #@pyqtSlot()
    def onChange(self,i): #changed!
        QMessageBox.information(self,
                  "Tab Index Changed!",
                  "Current Tab Index: %d" % i ) #changed!

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BaseWindow()
    window.show()
    sys.exit(app.exec_())