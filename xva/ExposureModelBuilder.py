from os.path import isfile, isdir, join, basename
import json
import numpy as np


class ExposureModelBuilder:

    def __init__(self):
        super().__init__()
        # Models
        self.matrix = None
        self.payment_matrix = None
        self.dates = None
        self.payment_dates = None
        self.expiries = None
        self.payment_expiries = None

    def read_exposure_matrix(self, fn):

        if not fn or not isfile(fn):
            return

        with open(fn, "r+") as f:
            data = json.load(f)["data"]
            #print(data.keys())
            self.matrix = np.array(data["matrix"])
            self.payment_matrix = np.array(data["paymentMatrix"])
            self.dates = np.array(data["dates"])
            self.payment_dates = np.array(data["paymentDates"])
            self.expiries = np.array(data["expiries"])
            self.payment_expiries = np.array(data["paymentExpiries"])

# m = ExposureModelBuilder()
# m.read_exposure_matrix(r"C:\Users\skiran\AppData\Local\Temp\ov\xva\cas_exposure\ExposureOutput.json")