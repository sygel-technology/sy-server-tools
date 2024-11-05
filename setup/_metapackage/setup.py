import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-server-tools",
    description="Meta package for sygel-technology-sy-server-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-base_confirmation_requirement_rules>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
