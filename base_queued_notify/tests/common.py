# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase

from odoo.addons.queue_job.tests.common import trap_jobs


class TestQueuedNotifyCommon(TransactionCase):
    def _get_mail_values(cls, notified_model_name):
        model_id = (
            cls.env["ir.model"]
            .search([("model", "=", notified_model_name)], limit=1)
            .id
        )
        return {
            "time_after_confirmation": 0,
            "mail_template_id": cls.env["mail.template"]
            .search([("model_id", "=", model_id)], limit=1)
            .id,
            "avoid_internal_users": True,
        }

    def _get_note_values(cls):
        return {
            "time_after_confirmation": 0,
            "note_text": "Funciona!",
        }

    def _get_activity_values(cls):
        return {
            "time_after_confirmation": 0,
            "summary": "Funciona",
            "note": "Funciona!",
            "user_id": False,
            "time_to_deadline": 1,
        }

    def _setUpCommon(cls, type_model, notificable_model, relation_field_name, prefix):
        cls.relation_field_name = relation_field_name
        cls.prefix = prefix

        cls.partner_id = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.type_record = type_model.create(
            {
                "name": "Test type",
                cls.prefix + "mail_notify_ids": [
                    (0, 0, cls._get_mail_values(notificable_model._name))
                ],
                cls.prefix + "log_note_notify_ids": [(0, 0, cls._get_note_values())],
                cls.prefix + "activity_notify_ids": [
                    (0, 0, cls._get_activity_values())
                ],
            }
        )
        if relation_field_name:
            cls.notificable_record = notificable_model.create(
                {
                    "partner_id": cls.partner_id.id,
                    relation_field_name: cls.type_record.id,
                }
            )

    def _create_queues(self):
        raise NotImplementedError()

    def _get_notify_ids(self):
        raise NotImplementedError()

    def assert_generated_queues(self):
        """Test that the jobs are created"""
        with trap_jobs() as trap:
            self._create_queues()
            for notify_ids in self._get_notify_ids():
                for notify_id in notify_ids:
                    trap.assert_jobs_count(1, only=notify_id._notify_thread)

    def assert_notifications(self):
        """Test the jobs functionality"""
        self._create_queues()

        # Syncronously Notify
        for notify_ids in self._get_notify_ids():
            for notify_id in notify_ids:
                if notify_id.is_to_notify(self.notificable_record):
                    notify_id._notify_thread(self.notificable_record)

        # Check activity created
        self.assertEqual(1, len(self.notificable_record.activity_ids))
        # Check email sent
        self.assertEqual(
            1,
            len(
                self.env["mail.mail"].search(
                    [
                        ("model", "=", self.notificable_record._name),
                        ("res_id", "=", self.notificable_record.id),
                    ]
                )
            ),
        )
        # Check note posted
        self.assertEqual(
            1,
            len(
                self.env["mail.message"].search(
                    [
                        ("id", "in", self.notificable_record.message_ids.ids),
                        (
                            "body",
                            "=",
                            self.type_record[
                                self.prefix + "log_note_notify_ids"
                            ].note_text,
                        ),
                    ]
                )
            ),
        )

    def setUp(cls):
        super().setUp()
        cls.partner_id = cls.env["res.partner"].create({"name": "Test Partner"})
