# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import datetime

from odoo import fields, models


class NotifyMixin(models.AbstractModel):
    _name = "notify.mixin"
    _description = "Mixin for queued notification events"

    notified_model_name = None

    time_after_confirmation = fields.Float(
        name="Time After Confirmation (Hours)",
        help="Delay used to calculate the notification date",
    )
    reference_date_field_id = fields.Many2one(
        string="Reference date field",
        comodel_name="ir.model.fields",
        ondelete="cascade",
        domain=lambda self: [
            (
                "model_id.model",
                "=",
                self.notified_model_name,
            ),
            ("ttype", "=", "datetime"),
        ],
        help="""Field of the notified model used to calculate of the notification date.
        If not selected the default is the notification launch moment """,
    )
    trigger_state = fields.Selection(
        selection=[],
        # TODO: ADD DOMAIN, SIMILARLY TO AUTOMATIC ACTIONS
        # selection=[('scheduled_action', 'Scheduled Action')]
    )

    notified_model_id = fields.Many2one(
        comodel_name="ir.model",
        string="Notified Model",
        compute="_compute_notified_model_id",
    )

    def _compute_notified_model_id(self):
        for rec in self:
            rec.notified_model_id = (
                self.env["ir.model"]
                .search([("model", "=", self.notified_model_name)], limit=1)
                .id
                if self.notified_model_name
                else False
            )

    def is_to_notify(self, record):
        """Returns if a record is in a status to be notified"""
        raise NotImplementedError()

    def notify(self, record):
        """Generate que notification queue for a record"""
        self.ensure_one()
        record.ensure_one()
        self.with_delay(eta=self.get_notification_delay(record))._notify_thread(record)
        # TODO: After generating a new queue,
        # the previous ones of the same type should be cancelled

    def _notify_thread(self, record):
        if self.is_to_notify(record):
            self._notify(record)

    def _notify(self, record):
        """Notifies a record. Must be implemented given the notification type"""
        raise NotImplementedError()

    def get_notification_delay(self, record):
        """Returns notification delay in seconds"""
        self.ensure_one()
        record.ensure_one()
        if self.reference_date_field_id:
            return record[self.reference_date_field_id.name] + datetime.timedelta(
                hours=self.time_after_confirmation
            )
        else:
            return int(self.time_after_confirmation * 3600)
