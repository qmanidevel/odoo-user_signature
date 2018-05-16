This module was based on https://github.com/yelizariev/addons-yelizariev/
ported to version 11.

Allows create signature templates for users. For example,

    ---

    <p>${user.name}, ${user.function} of ${user.partner_id.company_id.name}</p>

    <p>${user.phone},

    % if user.mobile

    ${user.mobile},

    % endif

    ${user.email}</p>

Will be converted to

    ---

    <p>Bob, sale manager of You Company</p>

    <p>+123456789, sales@example.com</p>

Tested on 11.0 5bb65170724dcd86cebd41a5b37509c6ed145ae6

Original Author post: https://yelizariev.github.io/odoo/module/2015/03/17/email-signature-template.html
