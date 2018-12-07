# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrainingSubject(models.Model):
    _name = 'pscloud.training.subject'
    _description = u"科目"
    
    name=fields.char(u'名称',size=64,default=u'默认科目名称')
    
    
#  vim:et:si:sta:ts=4:sts=4:sw=4:tw=79: