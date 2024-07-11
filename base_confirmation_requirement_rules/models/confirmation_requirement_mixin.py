# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval


class ConfirmationRequirementMixin(models.AbstractModel):
    _name = "confirmation.requirement.mixin"
    _description = "Confirmation Requirement Mixin"
    _type_field = {}

    def check_confirmation_requirements(self):
        if not self.user_has_groups(
            "base_confirmation_requirement_rules.group_skip_confirmation_requirement_rules"
        ):
            for rec in self.filtered(
                lambda a: a[self._type_field.get("type", False)]
                and a[self._type_field["type"]].use_requirement_rules
                and a[self._type_field["type"]].requirement_rule_ids
            ):
                for rule in rec[self._type_field["type"]].requirement_rule_ids:
                    domain = safe_eval(rule.domain) + [
                        ["id", "=", rec.id],
                    ]
                    if self.search_count(domain) != 1:
                        raise ValidationError(rule.error_description)
