from odoo import models, fields


class Fees(models.Model):
    _name = 'fees.structure'
    _description = 'Fees Structure of school'

    name = fields.Char('Student Name')
    amount = fields.Integer('Total Fees')
    fees_date = fields.Date('Submit Date', required=True, default=fields.Datetime.now, copy=False)
    fees_id = fields.Many2one('student.details', string="id")
