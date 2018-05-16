from odoo import api,models,fields,tools
from odoo.addons.mail.models.mail_template import mako_template_env
import logging

_logger = logging.getLogger(__name__)

class res_users(models.Model):
    _inherit = 'res.users'

    signature_id = fields.Many2one('res.users.signature', string='Signature template', help='Keep empty to edit signature manually')


    @api.onchange('signature_id')
    @api.multi
    def render_signature_id(self):
        for rec in self:
            if not rec.signature_id:
                continue
            mako = mako_template_env.from_string(tools.ustr(rec.signature_id.template))
            html = mako.render({'user': rec})
            if html != rec.signature:
                rec.signature = html

    @api.multi
    def write(self, vals):
        res = super(res_users, self).write(vals)
        for rec in self:
            if any([k in vals for k in ['signature_id']]):
                rec.render_signature_id()
        return res


class res_users_signature(models.Model):
    _name = 'res.users.signature'

    name = fields.Char('Name')
    comment = fields.Text('Internal note')
    template = fields.Html('Template', sanitize=False, help='''You can use variables:
* ${user.name}
* ${user.function} (job position)
* ${user.partner_id.company_id.name} (company in a partner form)
* ${user.company_id.name} (current company)
* ${user.email}
* ${user.phone}
* ${user.mobile}
* etc. (contact your administrator for further information)

You can use control structures:

% if user.mobile
    Mobile: ${user.mobile}
% endif

''')
    user_ids = fields.One2many('res.users', 'signature_id', string='Users')

    @api.one
    def write(self, vals):
        res = super(res_users_signature, self).write(vals)
        self.action_update_signature()
        return res

    @api.one
    def action_update_signature(self):
        self.user_ids.render_signature_id()

class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.one
    def write(self, vals):
        res = super(res_partner, self).write(vals)
        if self.user_ids:
           self.user_ids.render_signature_id()
        return res

