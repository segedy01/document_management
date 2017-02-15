# -*- coding: utf-8 -*-
{
    'name': "Document Management",

    'summary': """
        A document management system""",

    'description': """
        A document management system developed by GTS
    """,

    'author': "Guaranty Turnkey System",
    'website': "http://www.gtsng.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','hr'],

    # always loaded
    'data': [
        'security/file_security.xml',
        'security/ir.model.access.csv',
        'views/partner_document_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/button_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}