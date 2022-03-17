# -*- coding: utf-8 -*-

from logging import PlaceHolder
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move.line'

    @api.one
    def write(self, values):
        if self.partner_id.actualiza_cuenta:
            account_id=self.partner_id.cuenta_id.id
            new_rec=self.env['account.invoice.line'].search([('invoice_id','=',self.invoice_id.id)])
            values['account_id']=account_id
            for c in new_rec:
                c.write(values)
        else:
            domain=[('invoice_id','=',self.invoice_id.id),
                ('product_id','=',self.product_id.id)
                ]
            account_id=self.env['account.invoice.line'].search(domain,limit=1).account_id.id
        if account_id:
            values['account_id']=account_id
            if self.product_id:
                new_rec=self.search([('invoice_id','=',self.invoice_id.id),('product_id','=',self.product_id.id)])
                if new_rec:
                    return super(AccountMove,new_rec).write(values)


class ModuleName(models.Model):
    _inherit = 'res.partner'

    actualiza_cuenta = fields.Boolean(string='Cuenta y Produto por Defecto',
                                      PlaceHolder='Si se activa esta opción la cuenta seleccionada sera actualizada en las facturas de compras')
    cuenta_id = fields.Many2one(comodel_name='account.account', string='Cuenta por Defecto')
    product_id = fields.Many2one(comodel_name='product.product', string='Producto por Defecto')
    
    
    
