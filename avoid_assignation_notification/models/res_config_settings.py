# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    excluded_models_assignation_notif_ids = fields.Many2many(
        comodel_name="ir.model",
        related="company_id.excluded_models_assignation_notif_ids",
        readonly=False,
        string="Do not notify assignations models"
    )
