# -*- coding: utf-8 -*-
{
    'name' : 'OpenERP Internal Training',
    'version': '1.0.0',
    'author' : 'Srinivas',
    'website' : 'http://www.sigmainfo.net/',
    'category': 'Learning & Development',
    'depends' : ['base', 'sale'],
    'description': """
Module to explain OpenERP Customization and UI Artifacts .
==========================================================

a) How to extend existing model 
b) How to create new database model or OpenERP object
c) Map OpenERP object to Form view, Tree view, Search view with Filters, Group By etc
d) New Menu, Sub-menu, Action window
e) Add custom button
f) Add work-flow ==> Definition, Activity, Transition, View etc
g) Add Search filter
h) Add Security features ==> Add new security group, Menu access etc
i) Add Demo data
j) Add module icon
k) Add custom CSS 

TODO:
=====
a) Kanban view
b) Wizard
c) Reports: RML, OpenOffice, Jasper, Aeroo etc
d) Import/Export data through service
e) Webservice
f) Trigger or automated scripts
g) Add group restriction to field, specific menu, configuration access etc

    """,
    'data': [
        'security/demo_security.xml',
        'security/ir.model.access.csv',
        'view/sigma_view.xml',
        'view/company_view.xml',
        'workflow/employee_workflow.xml',
        'demo/employee_data.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
