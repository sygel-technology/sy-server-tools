# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Base Queue Notify",
    "summary": "Base module for queued notifications",
    "version": "17.0.1.0.0",
    "category": "Generic Modules",
    "website": "https://github.com/sygel-technology/sy-server-tools",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "queue_job",
    ],
    "data": [
        "views/base_queued_notify_views.xml",
    ],
}
