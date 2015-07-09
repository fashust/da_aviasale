/**
 * Created by fashust on 08.07.15.
 */
String.prototype.format = function() {
    var formatted = this;
    for (var i = 0; i < arguments.length; i++) {
        var regexp = new RegExp('\\{'+i+'\\}', 'gi');
        formatted = formatted.replace(regexp, arguments[i]);
    }
    return formatted;
};

var form_selector = '#search-form',
    search_results_holder = '.results',
    buy_btn = '.buy',
    popup_selector = '#orderPopup',
    result_selector = 'div[data-id="{0}"]',
    order_btn = '#order',
    order_form = 'form[name=order]',
    result_item_tpl = '<div data-id={0}><span>{1}</span><span>{2}</span>' +
        '<span>{3}</span><span>{4}</span>' +
        '<a class="buy" href="#" data-places={5} data-cost={6}>buy</a></div>';

function search_results(response) {
    $(search_results_holder).html();
    if (response.status) {
        var data = response.data.results,
            user_data = response.data.user_data,
            html = '';
        if (data.length != 0) {
            $(search_results_holder).html(_.map(data, function(item) {
                return result_item_tpl.format(
                    item.id,
                    item.code_name,
                    item.date,
                    item.dispatch__name,
                    item.arrival__name,
                    user_data.places,
                    item.total_cost
                );
            }).join(''));
        } else {
            $(search_results_holder).html('<h3>no results</h3>');
        }
    } else {
        console.log('show form errors')
    }
}

function show_order_popup(flight_id) {
    console.log('show popup');
    console.log(flight_id);
    var result = $(result_selector.format(flight_id)).find('a').data();
    $(popup_selector).find('input[name=flight]').val(flight_id);
    $(popup_selector).find('input[name=places]').val(result.places);
    $(popup_selector).find('input[name=cost]').val(result.cost / result.places);
    $(popup_selector).find('input[name=total_cost]').val(result.cost);
    $(popup_selector).modal();
}

function success_lock(response) {
    if (response.status) {
        show_order_popup(response.data);
    }
}

$(document).ready(function() {
    $('#id_date').datepicker();

    $(document).on('click', form_selector + ' > input[type=submit]', function(evt) {
        evt.preventDefault();

        $.ajax({
            type: 'POST',
            url: $(form_selector).attr('action'),
            data: $(form_selector).serialize(),
            success: search_results,
            failure: function(errMsg) {
                console.log(errMsg);
            }
        });
    });

    $(document).on('click', buy_btn, function (evt) {
        evt.preventDefault();
        $.ajax({
            type: 'GET',
            url: '/search/lock/?lock={0}'.format($(this).parent().data('id')),
            success: success_lock,
            failure: function(errMsg) {
                console.log(errMsg);
            }
        })
    });

    $(document).on('hide.bs.modal', popup_selector, function () {
        console.log('clear popup');
    });

    $(document).on('click', order_btn, function(evt) {
        evt.preventDefault();
        console.log('order form');
        $.ajax({
            type: 'POST',
            url: $(order_form).attr('action'),
            data: $(order_form).serialize(),
            success: function(response) {
                console.log(response);
            },
            failure: function(errMsg) {
                console.log(errMsg);
            }
        });
    });
});