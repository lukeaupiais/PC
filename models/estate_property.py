from odoo import fields, models
from dateutil.relativedelta import relativedelta


class EstateProperty (models.Model):
    _name = "estate.property"
    _description = "Test Module Estate"

    name = fields.Char(string="Title", required=True, default="Unknown")
    state = fields.Selection(
        selection=[("new", "New"), ("offer_received", "Offer Received"), ("offer_accepted", "Offer Accepted"), ("sold", "Sold"), ("canceled", "Canceled")],
        required=True,
        copy=False,
        default="new")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From", copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    last_seen = fields.Datetime(string="Last Seen", default=lambda self: fields.Datetime.now())
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string ='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help='The orientation of the garden.')
    active = fields.Boolean(default=True)