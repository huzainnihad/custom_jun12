from odoo import api, fields, models


class HrPayslipInput(models.Model):
    _inherit = "hr.payslip.input"

    loan_line_id = fields.Many2one("hr.loan.line", string="Loan Installment", help="Loan installment")


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.depends("employee_id", "input_line_ids", "input_line_ids.code", "date_from", "date_to")
    def _compute_total_loan_amount(self):
        for vals in self:
            vals.total_loan_amount = 0.0
            loan_amt = 0.0
            if vals.input_line_ids:
                for each_line in vals.input_line_ids:
                    if each_line.code == "LOAN":
                        loan_amt += each_line.amount
            vals.total_loan_amount = loan_amt

    total_loan_amount = fields.Float("Total Loan Amount", compute="_compute_total_loan_amount")
