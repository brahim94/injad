# -*- coding: utf-8 -*-

from odoo import models, fields, api


class teck_injad_report(models.Model):
    _inherit = "account.invoice"

    
    @api.depends('amount_total')
    def get_amount_in_words(self):
        amount_in_words = self.currency_id.amount_to_text(self.amount_total)
        return amount_in_words
