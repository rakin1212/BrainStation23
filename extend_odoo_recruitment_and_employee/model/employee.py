from odoo import fields, models


class EmployeeCustomizations(models.Model):
    _inherit = 'hr.employee'

    em_name = fields.Char(string="Name")
    em_address = fields.Char(string="Address")
    em_phone = fields.Char(string="Phone")

    institute = fields.Char(string="Institute")
    degree = fields.Char(string="Degree")
    passing_year = fields.Char(string="Passing Year")

    emergency_id = fields.Many2one('hr.employee', string='Emergency', index=True)
    emergency_contact_id = fields.One2many('hr.employee', 'emergency_id', string='Emergency Contact')

    leave_type1 = fields.Selection([('sick', 'Sick Leave'), ('casual', 'Casual Leave')], string="Leave Type 1")
    leave_type2 = fields.Selection([('sick', 'Sick Leave'), ('casual', 'Casual Leave')], string="Leave Type 2")
    leave_type1_days = fields.Integer(string="Days")
    leave_type2_days = fields.Integer(string="Days")
