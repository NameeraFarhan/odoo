from odoo import models, fields

class Project(models.Model):
    _inherit = 'project.project'

    assign_functional = fields.Many2one(comodel_name='hr.employee', string="Functional Assign")
    assign_technical = fields.Many2one(comodel_name='hr.employee', string="Technical Assign")
    add_logo = fields.Binary(string="Logo")


