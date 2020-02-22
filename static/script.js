document.addEventListener('DOMContentLoaded', () => {

    var select = document.querySelectorAll("div[id^=category] > select[id$=product]");

    select.forEach(item => {
        const productId = item.selectedOptions[0].value;
        get_product_info(item, productId);

        item.onchange = () => {
            const productId = item.selectedOptions[0].value;
            get_product_info(item, productId);
        };
    });

    function get_product_info(item, productId) {
        $.get("/get_product_info", { productId: productId }, function (data) {
            console.log(data);
            var prices = data["prices"];
            prices = JSON.parse(prices);


            // add prices to select item
            if (prices.length > 0) {

                var price_selector = item.parentNode.querySelector("select[id$=price]");
                price_selector.innerHTML = "";

                for (const price of prices) {

                    var price_option = document.createElement("option");
                    price_option.value = price["pk"];
                    price_option.text = price["fields"]["name"] + "- $" + price["fields"]["value"];
                    price_selector.add(price_option);
                };
            };

            var toppings = data["toppings"];
            toppings = JSON.parse(toppings);

            //add toppings to select item
            if (data["number_of_toppings"] > 0) {

                var topping_selector = item.parentNode.querySelector("select[id$=topping]");
                topping_selector.innerHTML = "";

                if (data["number_of_toppings"] > 1) {
                    topping_selector.multiple = true;
                }

                for (const topping of toppings) {
                    var topping_option = document.createElement("option");
                    topping_option.value = topping["pk"];
                    topping_option.text = topping["fields"]["name"];

                    topping_selector.add(topping_option);
                };

                if (topping_selector.disabled) {
                    topping_selector.disabled = false;
                }

            } else {
                var topping_selector = item.parentNode.querySelector("select[id$=topping]");
                topping_selector.innerHTML = "";
                topping_selector.disabled = true;
            };

        });
        return false;
    };

    // add to cart button 
    const addButtons = document.querySelectorAll("input[name=add]");
    addButtons.forEach(button => {
        button.onclick = () => {

            // get csrf token from cookies
            for (item of document.cookie.split(';')) {
                splitted = item.split('=');
                if (splitted[0] == "csrftoken") {
                    var csrf = splitted[1];
                }
            };

            // set csrf token to request header
            $.ajaxSetup({
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrf);
                }
            });

            // get the item info and add it to request
            const product = button.parentElement.querySelector("select[id$=product]");
            const price = button.parentElement.querySelector("select[id$=price]");
            const toppings = button.parentElement.querySelector("select[id$=topping]");

            var data = { product: null, price: null, topping: new Array() };

            if (product.selectedOptions[0]) {
                data["product"] = product.selectedOptions[0].value;
            }

            if (price.selectedOptions[0]) {
                data["price"] = price.selectedOptions[0].value;
            }

            for (topping of toppings.selectedOptions) {
                data["topping"].push(topping.value);
            };

            console.log(data);
            // send ajax request to add item to the cart
            $.post("add_to_cart", data);

        }
    });

    return false;

});