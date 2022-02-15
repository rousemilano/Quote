# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import  ValidationError
import logging

logger = logging.getLogger(__name__)



class Quote(models.Model):
    _name = 'quote'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Quote"
    _rec_name = 'contact_id'
    
    information = fields.Html("Information")
    contact_id = fields.Many2one('res.partner', string="Contact")
    user_id = fields.Many2one('res.users', string="User")
    product_id = fields.Many2one('product.product', string="Product")
    
