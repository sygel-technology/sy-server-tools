import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-server-tools",
    description="Meta package for sygel-technology-sy-server-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-html_fields_document_layout_configuration>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
