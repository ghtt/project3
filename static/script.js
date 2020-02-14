document.addEventListener('DOMContentLoaded', () => {



    var select = document.querySelectorAll('select');

    select.forEach(item => {
        item.onclick = () => {
            var max_selected = item.name;
            var count = $(`#${item.id} option:selected`).length;
            if (count > max_selected) {
                alert("123");
            };
        };
    });

    function toppings_selected() {

    };

});