# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    excluded_models_assignation_notif_ids = fields.Many2many(
        comodel_name="ir.model",
        string="Do not notify assignations models"
    )
