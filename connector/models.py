from __future__ import unicode_literals

from django.db import models

from connector import base_models


class ProductCategory(base_models.AuditModel):
    code = models.IntegerField(primary_key=True, db_column='GRPCODE')
    name = models.CharField(max_length=55, db_column='GRPNAME')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Categories"
        db_table = "GCP_SM23_PDT_GRP"


class ProductSubCategory(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    code = models.IntegerField(db_column='SUBGRP')
    category = models.ForeignKey(ProductCategory, db_column='GRPCODE')
    description = models.CharField(max_length=55, db_column='SGRPDESC')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Product SubCategories"
        db_table = "GCP_SM25_PDT_SUG"
        unique_together = ['code', 'category']


class TariffHeader(base_models.AuditModel):
    category = models.OneToOneField(ProductCategory, primary_key=True, db_column='GRPCODE')
    name = models.CharField(max_length=150, db_column='GRPNAME')
    type = models.CharField(max_length=2, db_column='GRPTYPE')

    class Meta:
        verbose_name_plural = "Tariff Header"
        db_table = "GCP_SM27_TARIFF_HDR"


class TariffMaster(base_models.AuditModel):
    tariff_id = models.IntegerField(primary_key=True, db_column='TARIFFID')
    tariff_head = models.CharField(max_length=10, db_column='TARIFFHD')
    description = models.CharField(max_length=80, db_column='TARIFF_DES')
    hsn_code = models.CharField(max_length=8, db_column='HSNCODE')
    gst = models.DecimalField(max_length=5, decimal_places=2, db_column='GSTPER')

    def __str__(self):
        return self.tariff_id

    class Meta:
        verbose_name_plural = "Tariff Master"
        db_table = "GCP_SM27_TARIFF_MAS"


class ProductMaster(base_models.AuditModel):
    product_code = models.IntegerField(primary_key=True, db_column='PRODCODE')
    description = models.CharField(max_length=60, db_column='PRODDESC')
    size = models.CharField(max_length=10, db_column='PSIZE')
    length = models.CharField(max_length=10, db_column='PRODLENG')
    count = models.IntegerField(db_column='PRODCNT')
    unit = models.CharField(max_length=5, db_column='UNIT')
    category = models.ForeignKey(ProductCategory, db_column='GRPCODE')
    sub_category = models.ForeignKey(ProductSubCategory, db_column='SUBGRP')
    tariff = models.ForeignKey(TariffMaster, db_column='TARIFFID')

    def __str__(self):
        return self.product_code

    class Meta:
        verbose_name_plural = "Product Master"
        db_table = "GCP_SM22_PDT"


class Price(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    price_code = models.IntegerField(db_column='PRICECODE')
    with_effect_from = models.DateField(db_column='WEFDATE')
    product_code = models.ForeignKey(ProductMaster, db_column='PRODCODE')
    price = models.IntegerField(db_column='PRODCNT')

    def __str__(self):
        return self.product_code

    class Meta:
        verbose_name_plural = "Price"
        db_table = "GCP_SM62_PRI_DTL"


class User(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    user_id = models.IntegerField(db_column='USERID')
    user_name = models.CharField(max_length=40, db_column='USERNAME')
    dept_code = models.IntegerField(db_column='DEPTCODE')

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name_plural = "User"
        db_table = "GCP_AM03_USR_HDR"


class DivisionMaster(base_models.AuditModel):
    division_code = models.IntegerField(primary_key=True, db_column='DIVNCODE')
    division_name = models.CharField(max_length=25, db_column='DIVNNAME')
    division_add1 = models.CharField(max_length=35, db_column='DIVNADD1')
    division_add2 = models.CharField(max_length=35, db_column='DIVNADD2')
    division_add3 = models.CharField(max_length=35, db_column='DIVNADD3')
    division_pincode = models.CharField(max_length=35, db_column='DIVNPIN')
    division_phonenumber = models.CharField(max_length=10, db_column='DIVNPHNO')
    division_fax = models.CharField(max_length=60, db_column='DIVNFAX')
    division_mail = models.CharField(max_length=25, db_column='DIVNMAIL')

    def __str__(self):
        return self.division_code

    class Meta:
        verbose_name_plural = "Division Master"
        db_table = "GCP_DIVNCODE"


class DepoMaster(base_models.AuditModel):
    depo_code = models.IntegerField(primary_key=True, db_column='DEPOCODE')
    division_code = models.ForeignKey(DivisionMaster, db_column='DIVNCODE')
    depo_name = models.CharField(max_length=25, db_column='DEPONAME')
    state_code = models.CharField(max_length=2, db_column='STATCODE')
    depo_add1 = models.CharField(max_length=55, db_column='DEPOADD1')
    depo_add2 = models.CharField(max_length=55, db_column='DEPOADD2')
    depo_add3 = models.CharField(max_length=55, db_column='DEPOADD3')
    depo_pincode = models.IntegerField(max_length=6, db_column='DEPOPIN')
    depo_phonenumber = models.CharField(max_length=60, db_column='DEPOPHNO')
    depo_fax = models.CharField(max_length=60, db_column='DEPOFAX')
    depo_mail = models.CharField(max_length=35, db_column='DEPOMAIL')
    gst_registered_date = models.DateField(db_column='GSTREGDT')
    price_code = models.IntegerField(max_length=4, db_column='PRICECOD')
    gstin = models.CharField(max_length=15, db_column='GSTIN')

    def __str__(self):
        return self.depo_code

    class Meta:
        verbose_name_plural = "Depo Master"
        db_table = "GCP_SM06_DEP"


class Market(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    market_code = models.IntegerField(max_length=3, db_column='MKTCODE')
    depo_code = models.ForeignKey(DepoMaster, db_column='DEPOCODE')
    market_name = models.CharField(max_length=25, db_column='MKTNAME')
    price_code = models.IntegerField(max_length=4, db_column='PRICECOD')

    def __str__(self):
        return "{} - {}".format(self.market_code, self.depo_code)

    class Meta:
        verbose_name_plural = "Market"
        db_table = "GCP_SM03_MKT"
        unique_together = ['market_code', 'depo_code']


class CustomerMaster(base_models.AuditModel):
    customer_code = models.IntegerField(primary_key=True, db_column='CUSTCODE')
    depo_code = models.ForeignKey(DepoMaster, db_column='DEPOCODE')
    customer_name = models.CharField(max_length=50, db_column='CUSTNAME')
    customer_add1 = models.CharField(max_length=55, db_column='CUSTADD1')
    customer_add2 = models.CharField(max_length=55, db_column='CUSTADD2')
    customer_city = models.CharField(max_length=35, db_column='CUSTCITY')
    customer_pincode = models.IntegerField(max_length=10, db_column='CUSTPIN')
    state_code = models.CharField(max_length=2, db_column='STATCODE')
    customer_phonenumber = models.CharField(max_length=60, db_column='CUSTPHNO')
    customer_mail = models.CharField(max_length=35, db_column='CUSTMAIL')
    mobile_phonenumber = models.CharField(max_length=20, db_column='MOBPHNO')
    credit_days = models.IntegerField(max_length=3, db_column='CRDAYS')
    credit_limit = models.IntegerField(max_length=11, db_column='CRLIMIT')
    market_code = models.ForeignKey(Market, db_column='MKTCODE')
    designation = models.CharField(max_length=25, db_column='DESIG')
    mobile = models.CharField(max_length=25, db_column='MOBILE')
    landline = models.CharField(max_length=25, db_column='LANDLINE')
    mail = models.CharField(max_length=30, db_column='EMAIL')
    short_name = models.CharField(max_length=12, db_column='SHORTNAME')
    depot = models.IntegerField(max_length=2, db_column='DEPOT')
    customer_id = models.IntegerField(max_length=12, db_column='CUSTID')
    pan = models.CharField(max_length=15, db_column='PAN')
    gstin = models.CharField(max_length=15, db_column='GSTIN')

    def __str__(self):
        return "{} - {}".format(self.market_code, self.depo_code)

    class Meta:
        verbose_name_plural = "Customer Master"
        db_table = "GCP_SM17_CUS"


class OrderHeader(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    order_number = models.IntegerField(max_length=3, db_column='OPNO')
    order_date = models.DateField(db_column='OPDT')
    customer_code = models.ForeignKey(CustomerMaster, db_column='CUSTCODE')
    depo_code = models.ForeignKey(DepoMaster, db_column='DEPOCODE')
    customer_reference_number = models.CharField(max_length=50, db_column='CUSREFNO')
    customer_reference_date = models.DateField(db_column='CUSREFDT')
    fs_code = models.CharField(max_length=3, db_column='FSCODE')
    order_value = models.IntegerField(max_length=12, db_column='ORDVAL')
    status = models.CharField(max_length=1, db_column='STATUS')
    order_created_date = models.DateField(db_column='CRETDATE')
    discount = models.IntegerField(max_length=12, db_column='DISCTOT')
    order_value_rs = models.IntegerField(max_length=12, db_column='ORDVALRS')
    shipped_date = models.DateField(db_column='SHIPDT')

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name_plural = "Order Header"
        db_table = "GCP_ST05_ORD_HDR"
        unique_together = ['order_number', 'order_date']


class OrderDetails(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    order_number = models.IntegerField(max_length=3, db_column='OPNO')
    order_date = models.DateField(db_column='OPDT')
    product_code = models.ForeignKey(ProductMaster, db_column='PRODCODE')
    order_quantity = models.IntegerField(max_length=13, db_column='ORDQTY')
    adjust_quantity = models.IntegerField(max_length=13, db_column='ADJQTY')
    adjust_value = models.IntegerField(max_length=12, db_column='ADJVALUE')
    discount = models.IntegerField(max_length=6, db_column='DISCOUNT')
    all_quantity = models.IntegerField(max_length=11, db_column='ALLQTY')
    sent_quantity = models.IntegerField(max_length=12, db_column='SENTQTY')
    hold_quantity = models.IntegerField(max_length=11, db_column='HOQTY')
    status = models.CharField(max_length=1, db_column='STATUS')
    amount = models.IntegerField(max_length=12, db_column='AMOUNT')
    order_created_date = models.DateField(db_column='CRETDATE')
    order_detail_id = models.IntegerField(max_length=12, db_column='OPDTLID')

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name_plural = "Order Details"
        db_table = "GCP_ST06_ORD_DTL"
        unique_together = ['order_number', 'order_date', 'product_code']


class StockMaster(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    product_code = models.ForeignKey(ProductMaster, db_column='PRODCODE')
    month = models.DateField(db_column='MONTH')
    depo_code = models.ForeignKey(DepoMaster, db_column='DEPOCODE')
    stock_flag = models.CharField(max_length=1, db_column='STKFLG')
    order_part_number = models.IntegerField(max_length=8, db_column='OPNO')
    order_date = models.DateField(db_column='OPDT')
    order_stock = models.IntegerField(max_length=13, db_column='OPSTK')
    quantity_received = models.IntegerField(max_length=13, db_column='QTYRECD')
    all_quantity = models.IntegerField(max_length=13, db_column='ALLQTY')
    clear_stock = models.IntegerField(max_length=13, db_column='CLSTK')
    free_stock = models.IntegerField(max_length=23, db_column='FREESTOCK')

    def __str__(self):
        return "{} - {} - {}".format(self.product_code, self.month, self.depo_code)

    class Meta:
        verbose_name_plural = "Stock Master"
        db_table = "GCP_ST06_ORD_DTL"
        unique_together = ['product_code', 'month', 'depo_code',
                           'stock_flag', 'order_part_number', 'order_date']


class InvoiceHeader(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    invoice_number = models.IntegerField(max_length=14, db_column='INVNO')
    invoice_date = models.DateField(db_column='INVDT')
    invoice_type = models.CharField(max_length=1, db_column='INVTYPE')
    allocation_number = models.IntegerField(max_length=8, db_column='ALLOCNO')
    allocation_date = models.DateField(db_column='ALLOCDT')
    cancel = models.CharField(max_length=1, db_column='CANCEL')
    depo_code = models.ForeignKey(DepoMaster, db_column='DEPOCODE')
    bank_code = models.IntegerField(max_length=50, db_column='BNKCODE')
    bank_document_date = models.DateField(db_column='BNKDOCDT')
    customer_code = models.ForeignKey(CustomerMaster, db_column='CUSTCODE')
    balance_amount = models.IntegerField(max_length=12, db_column='BALAMT')
    total = models.IntegerField(max_length=12, db_column='TOT')
    total_discount = models.IntegerField(max_length=12, db_column='TOT_DISC')
    remarks = models.CharField(max_length=100, db_column='REMARKS')
    roundoff = models.IntegerField(max_length=7, db_column='ROUNDEDOFF')
    total_product_value = models.IntegerField(max_length=21, db_column='TOT_PRODVAL')
    total_discount_value = models.IntegerField(max_length=21, db_column='TOT_DISCOUNT')
    total_tax_value = models.IntegerField(max_length=21, db_column='TOT_TAXABLE_VALUE')
    net_amount = models.IntegerField(max_length=21, db_column='NETAMT')
    total_tax_amount = models.IntegerField(max_length=21, db_column='TOT_TAXAMT')
    advance_amount = models.IntegerField(max_length=21, db_column='ADVAMT')
    credit_amount = models.IntegerField(max_length=21, db_column='CRAMT')
    dr_amount = models.IntegerField(max_length=21, db_column='DRAMT')
    paid_amount = models.IntegerField(max_length=21, db_column='PAIDAMT')
    invoice_amount = models.IntegerField(max_length=21, db_column='INVAMT')
    other_charges = models.IntegerField(max_length=14, db_column='OTHER_CHGS')
    gross_weight = models.IntegerField(max_length=18, db_column='GROSSWT')
    total_cgst_amount = models.IntegerField(max_length=14, db_column='TOT_CGSTAMT')
    total_sgst_amount = models.IntegerField(max_length=14, db_column='TOT_SGSTAMT')
    total_igst_amount = models.IntegerField(max_length=14, db_column='TOT_IGSTAMT')
    invoice_gstin = models.CharField(max_length=15, db_column='INV_GSTIN')

    def __str__(self):
        return self.invoice_number

    class Meta:
        verbose_name_plural = "Invoice Header"
        db_table = "GCP_ST16_INV_HDR"


class InvoiceDetails(base_models.AuditModel):
    id = models.IntegerField(primary_key=True, db_column='ID')
    invoice_header = models.ForeignKey(InvoiceHeader, db_column='INVHDR')
    product_code = models.ForeignKey(ProductMaster, db_column='PRODCODE')
    product_quantity = models.IntegerField(max_length=12, db_column='PRODQTY')
    product_rate = models.IntegerField(max_length=10, db_column='PRODRATE')
    amount = models.IntegerField(max_length=12, db_column='AMT')
    discperc = models.IntegerField(max_length=6, db_column='DISCPERC')
    discount_amount = models.IntegerField(max_length=10, db_column='DISCAMT')
    tax_amount = models.IntegerField(max_length=10, db_column='TAXAMT')
    net_amount = models.IntegerField(max_length=14, db_column='NETAMT')
    ret_quantity = models.IntegerField(max_length=15, db_column='RETQTY')
    order_number = models.IntegerField(max_length=8, db_column='ORDNO')
    order_date = models.DateField(db_column='ORDDT')
    total = models.IntegerField(max_length=12, db_column='TOT')
    cgst_per = models.IntegerField(max_length=7, db_column='CGSTPER')
    cgst_amount = models.IntegerField(max_length=16, db_column='CGSTAMT')
    sgst_per = models.IntegerField(max_length=7, db_column='SGSTPER')
    sgst_amount = models.IntegerField(max_length=16, db_column='SGSTAMT')
    igst_per = models.IntegerField(max_length=7, db_column='IGSTPER')
    igst_amount = models.IntegerField(max_length=16, db_column='IGSTAMT')
    item_type = models.CharField(max_length=1, db_column='ITEMTYPE')
    tarrifid = models.ForeignKey(TariffMaster, db_column='TARIFFID')

    def __str__(self):
        return self.invoice_number

    class Meta:
        verbose_name_plural = "Invoice Details"
        db_table = "GCP_ST17_INV_DTL"
