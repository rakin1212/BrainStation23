from odoo import fields, models, _


class EmployeeCustomizations(models.Model):
    _inherit = 'hr.applicant'

    em_name = fields.Char(string="Name")
    em_address = fields.Char(string="Address")
    em_phone = fields.Char(string="Phone")

    institute = fields.Char(string="Institute")
    degree = fields.Char(string="Degree")
    passing_year = fields.Char(string="Passing Year")

    manager = fields.Many2one('hr.employee', 'Manager', store=True, readonly=False,
                              domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    check_department = fields.Boolean(string="Is same dept", compute="get_user_dept")

    def create_employee_from_applicant(self):
        data = {

            'default_em_name': self.em_name,
            'default_em_address': self.em_address,
            'default_em_phone': self.em_phone,
            'default_institute': self.institute,
            'default_degree': self.degree,
            'default_passing_year': self.passing_year,
            'default_parent_id': self.manager.id
        }
        res = super(EmployeeCustomizations, self).create_employee_from_applicant()
        res['context'].update(data)
        return res
