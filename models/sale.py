# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import datetime
import dateutil.parser
from odoo.exceptions import UserError
import ast
import logging


class SaleOrde(models.Model):
    _inherit = 'sale.order'

    fecha_evento = fields.Date('Fecha de evento')
    monto_deposito = fields.Monetary('Monto deposito')
    fecha_ajuste_vestido1 = fields.Char('Instrucciones para toma de medidas')
    fecha_ajuste_vestido2 = fields.Char('Fecha de tallaje y modista')
    fecha_ajuste_vestido3 = fields.Char('Numero de recibo de caja')
    fecha_entrega = fields.Date('Fecha de entrega a novia')
    fecha_devolucion = fields.Date('Fehca devolución')
    nombre_vestido = fields.Char('Nombre de vestido')
    primer_pago = fields.Char('Monto y fecha 1er pago')
    segundo_pago = fields.Char('Monto y fecha 2do pago')
