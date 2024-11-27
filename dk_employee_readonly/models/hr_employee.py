import json

from odoo import _, api, fields, models
from lxml import etree


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model
    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super()._get_view(view_id, view_type, **options)
        context = self.env.context
        record_id = context.get('active_id')
        if not self.env.user.has_group('base.group_system'):
            if not self.env.user.has_group('hr.group_hr_manager'):
                if view_type in ('search','form'):
                    for node in arch.xpath("//field"):
                        node.set('readonly', '1')
                        node.set('options', "{'no_open': True}")
        return arch, view
