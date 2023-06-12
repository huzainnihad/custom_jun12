from odoo import models, fields, api, _

class HrLeaveType(models.Model):
    _inherit = "hr.leave.type"

    is_paid = fields.Boolean(string="Is paid")
    