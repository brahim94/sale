# -*- coding: utf-8 -*-
# from odoo import http


# class TechSale(http.Controller):
#     @http.route('/tech_sale/tech_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_sale/tech_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_sale.listing', {
#             'root': '/tech_sale/tech_sale',
#             'objects': http.request.env['tech_sale.tech_sale'].search([]),
#         })

#     @http.route('/tech_sale/tech_sale/objects/<model("tech_sale.tech_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_sale.object', {
#             'object': obj
#         })
