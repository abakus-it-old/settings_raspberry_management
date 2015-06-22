{
    'name': "AbAKUS Control Room PIs Management",
    'version': '1.0',
    'depends': [],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Settings',
    'description': 
    """
    This modules adds a management of Raspberry PIs that are installed in the Control Room at AbAKUS Eupen.

    A PI is a model and some info can be set in it. The PIs are then responsible of connecting to Odoo and get the info they need (mainly the web page they have to load).
    """,
    'data': ['view/settings_pis_management.xml','security/ir.model.access.csv'],
}
