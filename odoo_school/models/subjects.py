from odoo import models, fields, api


class Subjects(models.Model):
    _name = 'subjects'
    _description = 'Subjects'

    name = fields.Char('name')

