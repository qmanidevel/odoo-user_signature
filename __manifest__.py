{
    'name' : 'Signature templates for user emails',
    'version' : '1.0.0',
    'author' : 'Rachman Chavik',
    'license': 'LGPL-3',
    'category' : 'Social Network',
    'website' : 'https://github.com/qmanidevel/odoo-user_signature',
    'depends' : ['base'],
    'data':[
        'views/views.xml',
        'security/res_users_signature_security.xml',
        'security/ir.model.access.csv',
    ]
}
