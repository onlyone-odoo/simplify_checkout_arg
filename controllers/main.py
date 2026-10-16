from odoo import _

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleCheckoutArg(WebsiteSale):
    def _validate_address_values(self, *args, **kwargs):
        """Use this module's translation for the empty-fields message.

        ``website_sale`` owns the original string. Replacing it here lets
        ``es_AR`` come from this addon.

        Returns:
            tuple: Invalid fields, missing fields, and error messages.
        """
        invalid_fields, missing_fields, error_messages = super()._validate_address_values(
            *args, **kwargs
        )
        source = "Some required fields are empty."
        error_messages = [
            _("Some required fields are empty.") if message == source else message
            for message in error_messages
        ]
        return invalid_fields, missing_fields, error_messages
