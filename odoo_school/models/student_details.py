# -*- coding: utf-8 -*-

from odoo import models, fields


class Details(models.Model):
    _name = 'student.details'
    _description = 'Student detail '

    name = fields.Char('Name', required=True, help='Enter your name')
    age = fields.Integer('Age')
    roll_no = fields.Integer('Roll No.')
    phone = fields.Char('Phone no.')
    email = fields.Char('email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    student_dob = fields.Date('Date of Birth')

    subject_ids = fields.Many2many('subjects', string="Subject")
    class_id = fields.Many2one('student.class', 'class')
    # amount_ids = fields.One2many('fees.structure', 'fees_id', string='Fees')
    fees_id = fields.Many2one('fees.structure', string="id")
