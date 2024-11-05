import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-server-tools",
    description="Meta package for sygel-technology-sy-server-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-avoid_assignation_notification',
        'odoo14-addon-avoid_exception_activity_notification',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
