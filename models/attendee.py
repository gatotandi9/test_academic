from odoo import api, fields, models

class Attendee(models.Model):
    _name = "academic.attendee"

    name = fields.Char("Name")

    session_id = fields.Many2one(
        comodel_name="academic.session",
        string="Session", required=True
    )

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner", required=True
    )

    course_id = fields.Many2one(
        comodel_name="academic.course",
        string="Course",
        related="session_id.course_id",
        store=True
    )

    _sql_constraints = [
        (
            'partner_session_unique',
            'UNIQUE(partner_id, session_id)',
            'You cannot insert the same attendee multiple times!'
        )
    ]

    @api.model
    def create(self, vals):
        if not vals.get('name') and vals.get('partner_id'):
            partner = self.env['res.partner'].browse(vals['partner_id'])
            vals['name'] = str(partner.id)
        return super(Attendee, self).create(vals)
