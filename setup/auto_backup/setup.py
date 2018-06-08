import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo'],
    odoo_addon=True,
    odoo_addons={
        'external_dependencies_override': {
            'python': {
                'cryptography': 'cryptography==2.2.2',
                'paramiko': 'paramiko==2.4.1',
            }
        }
    }
)
