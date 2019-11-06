# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Switzerland - PAIN Direct Debit",
    "summary": "Generate ISO 20022 direct debits",
    "version": "11.0.0.0.0",
    "category": "Finance",
    "author": "Akretion,Camptocamp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "l10n_ch_pain_base",                    # oca_addons/l10n_switzerland/
        "account_banking_sepa_direct_debit",    # oca_addons/bank-payment/
    ],
    'installable': True,
}
