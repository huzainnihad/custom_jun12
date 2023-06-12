from odoo import fields,models,api
from datetime import datetime

class TruckWiseWizard(models.TransientModel):
    _name = "truck.wise.wizard"

    month_from = fields.Selection([('JAN', 'JAN'), ('FEB', 'FEB'), ('MAR', 'MAR'), ('APR', 'APR'),('MAY', 'MAY'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('AUG', 'AUG'),('SEP', 'SEP'), ('OCT', 'OCT'), ('NOV', 'NOV'), ('DEC', 'DEC'),], string='From',required=True)
    month_to = fields.Selection([('JAN', 'JAN'), ('FEB', 'FEB'), ('MAR', 'MAR'), ('APR', 'APR'),('MAY', 'MAY'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('AUG', 'AUG'),('SEP', 'SEP'), ('OCT', 'OCT'), ('NOV', 'NOV'), ('DEC', 'DEC'),], string='To',required=True)
   
    @api.model
    def year_selection(self):
        year = 2020 
        year_list = []
        while year != 2041: 
            year_list.append((str(year), str(year)))
            year += 1
        return year_list

    year = fields.Selection(year_selection, string="Year", default="2023")


    def action_print_excel(self):
        data = {
            'form':{
                'month_from': self.month_from,
                'month_to': self.month_to,
                'year': self.year
            }
        }
        return self.env.ref('bi_truckwise_report.truck_wise_report_card_xls').report_action(self, data=data)
