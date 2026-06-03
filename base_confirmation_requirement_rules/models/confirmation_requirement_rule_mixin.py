# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ConfirmationRequirementRuleMixin(models.AbstractModel):
    _name = "confirmation.requirement.rule.mixin"
    _description = "Confirmation Requirement Rule Mixin"

    name = fields.Char(required=True)
    domain = fields.Char(required=True, default="[]")
    error_description = fields.Text(required=True, translate=True)
