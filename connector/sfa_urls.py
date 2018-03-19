from django.conf import settings

SFA_URL = settings.SFA_DOMAIN
PRODUCT_SYNC = "{}{}".format(SFA_URL, "/product-sync/")
DIVISION_SYNC = "{}{}".format(SFA_URL, "/division-sync/")
DEPO_SYNC = "{}{}".format(SFA_URL, "/depo-sync/")
MARKET_SYNC = "{}{}".format(SFA_URL, "/market-sync/")
CUSTOMER_SYNC = "{}{}".format(SFA_URL, "/customer-sync/")