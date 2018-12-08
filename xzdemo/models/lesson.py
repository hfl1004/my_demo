# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT

class Lesson(models.Model):
    _name = 'pscloud.xzdemo.lesson'
    _description = "课程信息"


    name = fields.Char(string='Name')
    teacher_id = fields.Many2one('res.partner', string='老师')
    student_ids = fields.Many2many('res.partner', string='学生', readonly=True)
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')
    continue_days = fields.Integer(string='持续天数', compute='_compute_days', store=True)
    state = fields.Selection([
        ('draft', '草稿'),
        ('confirm', '确认'),
        ], string='状态', readonly=True, copy=False, index=True, default='draft')
    seat_qty = fields.Integer(string='座位数')
    subject_id = fields.Many2one('pscloud.xzdemo.subject', string='科目')
    person_id = fields.Many2one('res.partner', related='subject_id.person_id', readonly=True)
    desc = fields.Text(string='描述')





#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79:
