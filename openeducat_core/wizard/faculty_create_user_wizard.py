###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import fields, models


class WizardOpFaculty(models.TransientModel):
    _name = "wizard.op.faculty"
    _description = "Create User for selected Faculty(s)"

    def _get_faculties(self):
        if self.env.context and self.env.context.get('active_ids'):
            return self.env.context.get('active_ids')
        return []

    faculty_ids = fields.Many2many(
        'op.faculty', default=_get_faculties, string='Faculties')

    def create_faculty_user(self):
        user_group = self.env.ref('openeducat_core.group_op_faculty')
        active_ids = self.env.context.get('active_ids', []) or []
        records = self.env['op.faculty'].browse(active_ids)
        self.env['res.users'].create_user(records, user_group)
