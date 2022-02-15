# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Quote',
    'version': '1',
    'depends': [
        'base',
        'sale',
        'contacts'
    ],
    'author': 'Routh Milano',
    'description': """
        Version: odoo14 Enterprise
        Is a module for create quote
    """,
    'category': 'Sales/Quote',
    'website': 'http://www.odoo.com/',
    'data': [
        'security/quote_group.xml',
        'security/ir.model.access.csv',
        
        'views/quote_view.xml',
        'views/menu_quote.xml'
        
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}