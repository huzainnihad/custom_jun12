{
    "name": "Employee Leave Management",
    "version": "16.0.1.1.0",
    "description": """
        Helps you to manage Leave Requests of your company's staff.
        """,
    "category": "Generic Modules/Human Resources",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "depends": [
        "base",
        "hr",
        "hr_holidays",

    ],
    "data": [
        "reports/paper_format.xml",
        "reports/leave_application_form.xml",
        "reports/report_action.xml",
        "views/hr_leave.xml",
        "views/hr_leave_type.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
