# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Simplify Checkout Argentina",
    "summary": "Simplifica el checkout estableciendo valores por defecto",
    "description": "Módulo para establecer valores por defecto en el checkout del ecommerce usando solo vistas.",
    "category": "Website",
    "depends": ["website_sale", "l10n_ar_website_sale"],
    "data": [
        "views/website_sale_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "simplify_checkout_arg/static/src/js/address_default_state.js",
        ],
    },
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "18.0.1.2.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
}
