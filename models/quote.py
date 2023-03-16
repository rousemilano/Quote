# -*- coding: utf-8 -*-
from odoo import models, fields, _, api
from odoo.exceptions import  ValidationError, UserError
import logging

logger = logging.getLogger(__name__)



class Quote(models.Model):
    _name = 'quote'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Quote"
    _rec_name = 'contact_id'
    
    information = fields.Html("Information")
    contact_id = fields.Many2one('res.partner', string="Contact")
    user_id = fields.Many2one('res.users', string="Salesperson", compute="_compute_salesperson")
    product_id = fields.Many2one('product.product', string="Product")
    image = fields.Binary('Image')
    
    @api.depends('contact_id')
    def _compute_salesperson(self):
        for rec in self:
            rec.user_id = rec.contact_id.user_id

    
    @api.constrains('contact_id')
    def _validate_salesperson(self):
        for rec in self:
            if not rec.contact_id.user_id:
                raise UserError('Debe de agregar un contacto que tenga un vendedor asociaciado para poder registrar la cotización (Salesperson)')

    @api.onchange('product_id')
    def state_change(self):
        for rec in self:
            rec.image = rec.product_id.image_1920

