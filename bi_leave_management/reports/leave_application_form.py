from odoo import api, models,fields


class HrLeaveForm(models.AbstractModel):
    _name = "report.bi_leave_management.leave_application_form_template"
    _description = "Hr Leave Form"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["hr.leave"].browse(docids)
        paid_leave_type = self.env["hr.leave.type"].search([("is_paid",'=',True)])
        paid_allocation = self.env["hr.leave.allocation"].search([("holiday_status_id",'=',paid_leave_type.id),("employee_id",'=',docs.employee_id.id)])
        max_leaves = paid_allocation.max_leaves
        leaves_taken = paid_allocation.leaves_taken
        current_leave = max_leaves - leaves_taken

        return {
            "doc_ids": docs.ids,
            "doc_model": "hr.leave",
            "data": data,
            "docs": docs,
            "max_leaves":max_leaves,
            "leaves_taken":leaves_taken,
            "current_leave":current_leave
        }
