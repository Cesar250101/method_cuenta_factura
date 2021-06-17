# -*- coding: utf-8 -*-
from odoo import http

# class MethodCuentaFactura(http.Controller):
#     @http.route('/method_cuenta_factura/method_cuenta_factura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_cuenta_factura/method_cuenta_factura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_cuenta_factura.listing', {
#             'root': '/method_cuenta_factura/method_cuenta_factura',
#             'objects': http.request.env['method_cuenta_factura.method_cuenta_factura'].search([]),
#         })

#     @http.route('/method_cuenta_factura/method_cuenta_factura/objects/<model("method_cuenta_factura.method_cuenta_factura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_cuenta_factura.object', {
#             'object': obj
#         })