from odoo import api, fields, models

class AddAttendees(models.TransientModel):
    _name = "academic.add_attendees"
    _description = "Wizard Add Attendees"

    session_ids = fields.Many2many('academic.session', string="Sessions")
    partner_ids = fields.Many2many('res.partner', string="Attendees")

    def confirm(self):
            Attendee = self.env['academic.attendee']
            for session in self.session_ids:
                for partner in self.partner_ids:
                    Attendee.create({
                        'session_id': session.id,
                        'partner_id': partner.id,
                    })
            return True
