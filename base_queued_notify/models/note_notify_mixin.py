# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class NoteNotifyMixin(models.AbstractModel):
    _name = "note.notify.mixin"
    _inherit = "notify.mixin"
    _description = "Mixin for queued note notification events"

    note_text = fields.Char(name="Note Text")

    def _notify(self, record):
        record.env["mail.message"].create(
            {
                "body": self.note_text,
                "model": record._name,
                "res_id": record.id,
                "message_type": "comment",
                "subtype_id": record.env.ref("mail.mt_note").id,
            }
        )
