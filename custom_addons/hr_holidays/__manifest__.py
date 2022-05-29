# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Time Off',
    'version': '1.5',
    'category': 'Human Resources/Time Off',
    'sequence': 2,
    'summary': 'Allocate time off and follow time off requests',
    'website': '',
    'description': """""",
    'author': 'danik',
    'depends': ['hr', 'calendar', 'resource'],
    'data': [
        'data/report_paperformat.xml',
        'data/mail_data.xml',
        'data/hr_holidays_data.xml',
        'data/ir_cron_data.xml',

        'security/hr_holidays_security.xml',
        'security/ir.model.access.csv',

        'views/resource_views.xml',
        'views/hr_leave_views.xml',
        'views/hr_leave_type_views.xml',
        'views/hr_leave_allocation_views.xml',
        'views/mail_activity_views.xml',

        'wizard/hr_holidays_summary_employees_views.xml',
        'wizard/hr_departure_wizard_views.xml',

        'report/hr_holidays_templates.xml',
        'report/hr_holidays_reports.xml',
        'report/hr_leave_reports.xml',
        'report/hr_leave_report_calendar.xml',

        'views/hr_views.xml',
        'views/hr_leave_template.xml',
        'views/hr_holidays_views.xml',
    ],
    'demo': [
        'data/hr_holidays_demo.xml',
    ],
    'qweb': [
        'static/src/bugfix/bugfix.xml',
        'static/src/components/partner_im_status_icon/partner_im_status_icon.xml',
        'static/src/components/thread_icon/thread_icon.xml',
        'static/src/components/thread_view/thread_view.xml',
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
