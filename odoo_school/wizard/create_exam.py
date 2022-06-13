from odoo import models, fields, api


class CreateExamsWizard(models.TransientModel):
    _name = 'create.exam.wizard'
    _description = "Create Exam Wizard"

    sub = fields.Char("Subject")
    clas = fields.Integer("Class")
    name = fields.Char("Name")

    def action_create_exam(self):
        pass
    #self.env['odoo_school.exam'].create({"name": self.name.name})