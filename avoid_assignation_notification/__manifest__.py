# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Avoid Assignation Notification",
    "summary": "Avoid Assignation Notification",
    "version": "15.0.1.0.0",
    "category": "Mail",
    "website": "https://www.sygel.es",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'base',
        'mail',
    ],
    "data": [
        'views/res_config_settings_views.xml',
    ],
}
