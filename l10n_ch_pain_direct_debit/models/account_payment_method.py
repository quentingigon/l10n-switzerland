# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    pain_version = fields.Selection(selection_add=[
        ('pain.008.001.02.ch.01',
         'pain.008.001.02.ch.01 (direct debit in Switzerland)'),
        ])

    @api.multi
    def get_xsd_file_path(self):
        self.ensure_one()
        painv = self.pain_version
        if painv == 'pain.008.001.02.ch.01':
            path = f'l10n_ch_pain_direct_debit/data/{painv}.xsd'
            return path
        return super().get_xsd_file_path()
