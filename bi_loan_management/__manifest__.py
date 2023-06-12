{
    "name": "Employee Loan Management",
    "version": "16.0.1.1.0",
    "summary": "Manage Loan Requests",
    "description": """
        Helps you to manage Loan Requests of your company's staff.
        """,
    "category": "Generic Modules/Human Resources",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "depends": [
        "base",
        "om_hr_payroll",
        "hr",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/hr_loan_seq.xml",
        "data/salary_rule_loan.xml",
        "reports/paper_format.xml",
        "reports/loan_advanced_form_report.xml",
        "reports/report_action.xml",
        "views/hr_loan.xml",
        "views/hr_payroll.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
