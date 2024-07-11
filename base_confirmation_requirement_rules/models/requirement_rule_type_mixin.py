# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RequirementRuleTypeMixin(models.AbstractModel):
    _name = "requirement.rule.type.mixin"
    _description = "Requirement Rule Type Mixin"

    requirement_rule_ids = fields.Many2many(
        string="Requirement Rules",
        comodel_name="confirmation.requirement.rule.mixin",
        relation="confirmation_requirement_rule_type_rel",
    )
    use_requirement_rules = fields.Boolean(string="Use Requirement Rules")
