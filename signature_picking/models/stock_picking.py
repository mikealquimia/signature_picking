# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    signature_picking = fields.Binary(string="Signature", tracking=True,)
    signature_in_picking = fields.Boolean(string="Signature in Picking", related="picking_type_id.signature_in_picking")