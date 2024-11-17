from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student Table'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    guardian = fields.Char(string='Guardian')
    section_class = fields.Char(string='Section of Class')
    active = fields.Boolean('Active', default=True)
