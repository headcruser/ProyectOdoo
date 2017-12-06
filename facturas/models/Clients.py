# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Clients(models.Model):
    _name = 'facturas.clients'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
