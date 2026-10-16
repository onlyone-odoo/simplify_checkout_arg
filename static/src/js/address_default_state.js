/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import "@website_sale/js/address";

publicWidget.registry.websiteSaleAddress.include({
    /**
     * Select Buenos Aires when Argentina is chosen and the state is empty.
     *
     * The option is matched by its state code, not by list position.
     *
     * @param {boolean} init - True on the first load of the address form.
     */
    async _changeCountry(init = false) {
        await this._super(...arguments);
        const form = this.addressForm;
        const countryOption = form.country_id.selectedOptions[0];
        const stateSelect = form.state_id;
        if (
            countryOption
            && countryOption.getAttribute("code") === "AR"
            && stateSelect
            && !stateSelect.value
        ) {
            const buenosAires = [...stateSelect.options].find(
                (option) => option.dataset.code === "B"
            );
            if (buenosAires) {
                stateSelect.value = buenosAires.value;
            }
        }
    },

    /**
     * Scroll to the first missing field when the address cannot be saved.
     *
     * @param {Event} ev - Click on the save button.
     */
    async _onSaveAddress(ev) {
        const form = this.addressForm;
        if (!form.reportValidity()) {
            const invalid = form.querySelector(":invalid");
            invalid?.scrollIntoView({behavior: "smooth", block: "center"});
            invalid?.focus();
            return;
        }
        await this._super(...arguments);
        if (this.errorsDiv && this.errorsDiv.children.length) {
            this.errorsDiv.scrollIntoView({behavior: "smooth", block: "center"});
            form.querySelector(".is-invalid")?.focus();
        }
    },
});
