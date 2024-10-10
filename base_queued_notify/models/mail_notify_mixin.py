# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MailNotifyMixin(models.AbstractModel):
    _name = "mail.notify.mixin"
    _inherit = "notify.mixin"
    _description = "Mixin for queued mail notification events"

    mail_template_id = fields.Many2one(
        name="Mail Template",
        comodel_name="mail.template",
        domain=lambda self: [
            (
                "model_id.model",
                "=",
                self.notified_model_name,
            )
        ],
        required=True,
    )
    avoid_internal_users = fields.Boolean(default=False)

    def notify(self, record):
        """Generate notification queue for a record"""
        return super(
            MailNotifyMixin,
            self.with_context(avoid_internal_users=self.avoid_internal_users),
        ).notify(record)

    def _notify(self, record, mail_template_id=False):
        email_values = {}
        if self.avoid_internal_users:
            # TODO: Acortar
            partners_str = self.mail_template_id._render_field(
                "partner_to", record.ids
            )[record.id]
            partners_list = [int(x) for x in partners_str.strip("[]").split(",") if x]
            delete_partners = []
            for partner_id in partners_list:
                if self.env["res.users"].search(
                    [("partner_id", "=", partner_id), ("share", "=", False)], limit=1
                ):
                    delete_partners.append(partner_id)
            for r in delete_partners:
                partners_list.remove(r)
            email_values.update({"recipient_ids": [(4, id) for id in partners_list]})
        if not mail_template_id:
            mail_template_id = self.mail_template_id
        mail_template_id.send_mail(record.id, email_values=email_values)
