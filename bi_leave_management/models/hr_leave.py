from odoo import models, fields, api, _

class HrLeave(models.Model):
    _inherit = "hr.leave"

    address_while_on_leave = fields.Text(string="Address While on leave")
    contact_on_leave = fields.Char(string="Contact on leave")
    duties_on_absence = fields.Text(string="Duties on absence")


    

    