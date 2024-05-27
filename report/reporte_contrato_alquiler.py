# -*- coding: utf-8 -*-

from odoo import api, models
import re
import logging
from datetime import date
import time
from datetime import datetime
import dateutil.parser
import calendar
from dateutil.relativedelta import *

class ReporteContratoAlquiler(models.AbstractModel):
    _name = 'report.lovestory.reporte_contrato_alquiler'

    nombre_reporte = ''

    def lineas(self,o):
        vestido1 = False
        vestido2 = False
        vestido3 = False
        fustan = False
        corse = False
        abrigo = False
        liga = False
        cincho = False
        cojin = False
        otro = False
        contador = 0
        for linea in o.order_line:
            logging.warn('a')
            if linea.product_id.default_code == 'vestido' and contador == 0:
                logging.warn('si')
                vestido1 = {'nombre': linea.product_id.name, 'precio': linea.price_total}
                contador += 1
            elif linea.product_id.default_code == 'vestido' and contador == 1:
                logging.warn('si')
                vestido2 = {'nombre': linea.product_id.name, 'precio': linea.price_total}
                contador += 1
            elif linea.product_id.default_code == 'vestido' and contador == 2:
                logging.warn('si')
                vestido3 = {'nombre': linea.product_id.name, 'precio': linea.price_total}
                contador += 1
            else:
                contador += 1

            if linea.product_id.default_code == 'fustan' and linea.price_total == 0:
                fustan = True
            if linea.product_id.default_code == 'corne' and linea.price_total == 0:
                corse = True
            if linea.product_id.default_code == 'abrigo' and linea.price_total == 0:
                abrigo = True
            if linea.product_id.default_code == 'liga' and linea.price_total == 0:
                liga = True
            if linea.product_id.default_code == 'cincho' and linea.price_total == 0:
                cincho = True
            if linea.product_id.default_code == 'cojin' and linea.price_total == 0:
                cojin = True
            if linea.product_id.default_code not in ['fustan','corne','abrigo','liga','cincho','cojin']:
                otro = {'nombre': linea.product_id.name, 'precio': linea.price_total}
        return {'vestido1': vestido1,'vestido2': vestido2,'vestido3': vestido3,'fustan': fustan,'corse': corse,'abrigo': abrigo,'liga': liga,'cojin': cojin,'cincho': cincho,'otro': otro}

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = 'sale.order'
        docs = self.env[self.model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
            'lineas': self.lineas
        }
