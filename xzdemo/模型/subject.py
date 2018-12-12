# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Subject(models.Model):
    _name = 'xzdemo.subject'
    _description = "科目"

    name = fields.Char(string='科目名称')
    person_id = fields.Many2one('res.partner', string='负责人')
    lessin_ids=fields.Char(string='课程')
    desc = fields.Text(string='描述')

#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
