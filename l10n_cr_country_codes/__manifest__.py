{
    'name': 'Códigos País de Costa Rica para Facturación Electrónica',
    'version': '15.1.1.1.1',
    'author': 'Julio CRR',
    'license': 'AGPL-3',
    'website': 'https://www.facturaodoocr.com',
    'category': 'Account',
    'description': '''Códigos País Costa Rica para la Facturación Electrónica''',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'data/res_country_state.xml',
        'data/res.country.county.csv',
        'data/res.country.district.csv',
        'data/res.country.neighborhood.csv',
        'security/ir.model.access.csv',
        'views/res_country_county_views.xml',
        'views/res_country_district_views.xml',
        'views/res_country_neighborhood_views.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
    ],
    # "pre_init_hook": "pre_init_hook",
    'installable': True,
}
