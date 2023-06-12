from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    loan_id = fields.Many2one("hr.loan", string="Loan Installment", help="Loan installment")
