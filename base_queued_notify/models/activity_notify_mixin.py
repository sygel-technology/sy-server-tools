# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import datetime

from odoo import fields, models


class ActivityNotifyMixin(models.AbstractModel):
    _name = "activity.notify.mixin"
    _inherit = "notify.mixin"
    _description = "Mixin for queued activity notification events"

    time_to_deadline = fields.Integer(name="Days to Deadline")
    summary = fields.Char(name="Summary")
    note = fields.Char(name="Note")
    user_id = fields.Many2one(string="User", comodel_name="res.users")

    def _notify(self, record):
        deadline = fields.Datetime.to_string(
            datetime.datetime.now() + datetime.timedelta(days=self.time_to_deadline)
        )
        self.env["mail.activity"].create(
            {
                "activity_type_id": self.env.ref("mail.mail_activity_data_todo").id,
                "date_deadline": deadline,
                "summary": self.summary,
                "note": self.note,
                "user_id": self.user_id.id or self.env.user.id,
                "res_id": record.id,
                "res_model_id": self.notified_model_id.id,
            }
        )
