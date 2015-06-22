from openerp import models, fields, api

class raspberry_pi(models.Model):

    _name = 'settings.raspberry_pi'

    name = fields.Char(string='Name')
    ip = fields.Char(string='IP Address')

    webpage_url = fields.Char(string='Webpage to load')
    webpage_user = fields.Char(string='Webpage user')
    webpage_password = fields.Char(string='Webpage password')
