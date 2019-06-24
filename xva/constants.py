DEFAULT_NUM_OF_LINES = 100
DEFAULT_NUM_OF_DATES = 20

# TABS
MAIN_TAB_EXPOSURE_RESULTS = "Exposure Results"
SUB_TAB_EXPOSURES = "Exposures"
SUB_TAB_EXPOSURES_PLOT = "Exposures Plot"
SUB_TAB_PAYMENT_MATRIX_PLOT = "Payment Matrix"

MAIN_TAB_XVA_RESULTS = "XVA Results"

# File Paths
OV_CAS_RES_DIR = r"~/work/python/python_projects/xva/sample_data"
# OV_CAS_RES_DIR = r"C:/tmp/cas/xva/rbl_output"
# OV_CAS_RES_DIR = r"sample_data"
# BULKSTORE_DOWNLOAD_DIR = r"C:/tmp/cas/xva/bulkstore/"
BULKSTORE_DOWNLOAD_DIR = r"sample_data"

# URLs
# OV_HOST = '192.168.130.52'
OV_HOST = 'localhost'
OV_PORT = 8080
OV_BASE_URL = "http://%s:%d" % (OV_HOST, OV_PORT)
OV_USER = 'nxadmin'
OV_PASS = 'd#demo'

EXPOSURE_DOWNLOAD_URL = OV_BASE_URL + "/oneview/rest/ag/cas/xva/exposure"
LOGIN_URL = OV_BASE_URL + "/oneview/rest/core/auth/token"
XVA_CALC_RUN = OV_BASE_URL + "/oneview/rest/core/analytics/calculation-run"
XVA_CALC_RESULT = OV_BASE_URL + "/oneview/rest/core/analytics/calculation-result/xva"

