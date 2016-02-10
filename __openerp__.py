# -*- coding: utf-8 -*-
{
    'name' : 'OdooERP Internal Training',
    'version': '1.0.0',
    'author' : 'Srinivas',
    'website' : 'http://www.sigmainfo.net/',
    'category': 'Learning & Development',
    'depends' : ['base', 'sale'],
    'description': """
Module to explain OdooERP Customization and UI Artifacts .
==========================================================

1) How to extend existing model 
2) How to create new database model or OdooERP object
3) Map OdooERP object to Form view, Tree view, Search view with Filters, Group By etc
4) New Menu, Sub-menu, Action window
5) Add custom button
6) Add work-flow ==> Definition, Activity, Transition, View etc
7) Add Search filter
8) Add Security features ==> Add new security group, Menu access etc
9) Add Demo data
10) Add module icon
11) Add custom CSS 

TODO:
----
12) Kanban view
13) Wizard
14) Reports: RML, OpenOffice, Jasper, Aeroo etc
15) Import/Export data through service
16) Webservice
17) Trigger or automated scripts
18) Add group restriction to field, specific menu, configuration access etc
19) Support for images : employee image, department image
20) Graph view
21) Calendar view
22) Configuration option: example manage active field
23) Enhance Search filter : Only active, inactive etc
24) Accept or reject : trigger a mail to employee
    """,
    'data': [
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
