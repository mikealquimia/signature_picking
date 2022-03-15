# -*- coding: utf-8 -*-
{
    'name': "Signature in Stock Picking",
    'summary': """Field for signature in delivery note""",
    'description': """
        Add signature field in Alborán depending on validation in Stock Picking type, which is printed in Stock Picking report
    """,
    'author': "Gt Alchemy Development",
    'license': 'LGPL-3',
    'support': 'developmentalchemygx@gmail.com',
    'category': 'Warehouse Management',
    'version': '11.1.1',
    'price': 5.00,
    'currency': 'USD',
    'data': [
        'views/stock_picking_views.xml',
        'reports/report_picking.xml',
    ],
    'images': ['static/description/banner.png'],
    'depends': ['stock'],
}