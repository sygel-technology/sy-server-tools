# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailThreadCustom(models.AbstractModel):

    _inherit = "mail.thread"
    
    def _message_auto_subscribe_notify(self, partner_ids, template):
        excluded_model_ids = self.env.company.excluded_models_assignation_notif_ids.ids
        for sel in self:
            no_notify = False
            if self.env['ir.model']._get(sel._name).id in excluded_model_ids:
                no_notify = True
            return super(
                MailThreadCustom,
                self.with_context(mail_auto_subscribe_no_notify=no_notify)
            )._message_auto_subscribe_notify(partner_ids, template)
