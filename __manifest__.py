# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Quote',
    'version': '1',
    'depends': [
        'base',
        'account',
        'contacts',
        'web'
    ],
    'author': 'Rouse Milano',
    'description': """
        Version: odoo15 Enterprise
        Is a module for create quote
    """,
    'category': 'Sales/Quote',
    'data': [
        'security/quote_group.xml',
        'security/ir.model.access.csv',
        
        'views/quote_view.xml',
        'views/menu_quote.xml',
        'report/quote_template.xml',
        'report/quote_report.xml'  
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}