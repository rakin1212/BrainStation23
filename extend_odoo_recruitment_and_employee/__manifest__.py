{
    "name": "EXTEND ODOO RECRUITMENT AND EMPLOYEE",
    "summary": "",
    "version": "14.0.1.0.1",
    "author": "Karim Ullah Chowdhury",
    "website": "",
    "category": "Tools",
    "depends": [
        "base", "hr", "hr_recruitment"
    ],
    "license": "LGPL-3",
    "data": [
        'security/manager_approve.xml',
        'views/employee.xml',
        'views/recruit.xml'
    ],
    'sequence': 1,
    "installable": True,
    "auto_install": False,
    "application": True,
}
