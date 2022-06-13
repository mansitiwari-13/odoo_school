from odoo import models, fields


class Exam(models.Model):
    _name = 'exam'
    _description = 'Exams'

    name = fields.Char('Student Name')
    subject = fields.Char('Subject')
    marks = fields.Integer('Marks')
    # student_id = fields.Many2one('student.details', "Name")
    # subject_id = fields.Many2one('subjects', "Subjects")
