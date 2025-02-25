from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    assign_functional = fields.Many2one(
        comodel_name='hr.employee',
        string="Functional Assign",
        related='project_id.assign_functional',
        store=True,
        readonly=True
    )

    assign_technical = fields.Many2one(
        comodel_name='hr.employee',
        string="Technical Assign",
        related='project_id.assign_technical',
        store=True,
        readonly=True
    )
