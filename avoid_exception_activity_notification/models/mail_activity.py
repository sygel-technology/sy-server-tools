# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailActivity(models.AbstractModel):

    _inherit = "mail.activity"

    def action_notify(self):
        warning_activity = self.env.ref('mail.mail_activity_data_warning').id
        for sel in self:
            if sel.activity_type_id and sel.activity_type_id.id == warning_activity:
                return
            else:
                return super(MailActivity, sel).action_notify()
