from odoo import models, fields


class Fees(models.Model):
    _name = 'student.class'
    _description = 'Class'

    #student_id = fields.Many2one('student.class', 'class')
    class_name = fields.Char("Class")
    #class_ids = fields.One2many()