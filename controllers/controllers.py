# -*- coding: utf-8 -*-
# from odoo import http


# class TeckInjadReport(http.Controller):
#     @http.route('/teck_injad_report/teck_injad_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/teck_injad_report/teck_injad_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('teck_injad_report.listing', {
#             'root': '/teck_injad_report/teck_injad_report',
#             'objects': http.request.env['teck_injad_report.teck_injad_report'].search([]),
#         })

#     @http.route('/teck_injad_report/teck_injad_report/objects/<model("teck_injad_report.teck_injad_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('teck_injad_report.object', {
#             'object': obj
#         })
