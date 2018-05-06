$(document).ready(function() {
    console.log(document);
    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });
    
    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });
   
    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */
    
    // добавляем ajax-обработчик для обновления количества товара
    $(document).on('click', 'input[type="number"]', function () {
        var target_href = event.target;
        var url_ = "/basket/edit/" + target_href.name + "/" + target_href.value + "/";

        if (target_href) {
            $.ajax({
                url: url_,
                success: function (data) {
                    //$('.basket_list').html(data.result);
                    $('.basket_list').load('/basket/ .basket_list ');
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

    // remove product
    $(document).on('click', '.remove', function () {
        var target_href = event.target;
        var url_ = "/basket/remove/" + target_href.value + '/';

        if (target_href) {
            jQuery.ajax({
                url: url_,
                success: function(data, status, xhr) {
                    //$('.basket_list').html(data.result);
                    $('.basket_list').load('/basket/ .basket_list ');
                    console.log('ajax done');
                }
            });
        }
        event.preventDefault();
    });
});