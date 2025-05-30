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


class WizardOpFacultyEmployee(models.TransientModel):
    _name = 'wizard.op.faculty.employee'
    _description = "Create Employee and User of Faculty"

    user_boolean = fields.Boolean("Want to create user too ?", default=True)

    def create_employee(self):
        for record in self:
            active_id = self.env.context.get('active_ids', []) or []
            faculty = self.env['op.faculty'].browse(active_id)
            faculty.create_employee()
            if record.user_boolean and not faculty.user_id:
                user_group = self.env.ref('openeducat_core.group_op_faculty')
                self.env['res.users'].create_user(faculty, user_group)
                faculty.emp_id.user_id = faculty.user_id
