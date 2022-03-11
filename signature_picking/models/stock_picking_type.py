# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    signature_in_picking = fields.Boolean(string="Signature in Picking")