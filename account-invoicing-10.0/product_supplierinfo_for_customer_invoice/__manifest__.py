# -*- coding: utf-8 -*-
# Copyright 2013-2017 Agile Business Group sagl
#     (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Product Customer code for account invoice",
    "summary": """Based on product_customer_code, this module loads in every
                account invoice the customer code defined in the product,""",
    "version": "10.0.1.0.0",
    "author": "Agile Business Group,Odoo Community Association (OCA)",
    "website": "http://www.agilebg.com",
    "category": "Account",
    "license": "AGPL-3",
    "depends": [
        "product",
        "account",
        "product_supplierinfo_for_customer"
    ],
    "data": [
        "views/account_invoice_view.xml",
    ],
    "installable": True,
}
