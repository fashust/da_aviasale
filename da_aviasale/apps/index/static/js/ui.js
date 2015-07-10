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

var search_form_selector = '#search-form',
    search_results_holder = '.results',
    buy_btn = '.buy',
    popup_selector = '#orderPopup',
    result_selector = 'div[data-id="{0}"]',
    order_btn = '#order',
    order_form = 'form[name=order]',
    result_item_tpl = '<div class="results_row" data-id={0}><span>{1}</span><span>{2}</span>' +
        '<span>{3}</span><span>{4}</span>' +
        '<a class="buy" href="#" data-places={5} data-cost={6}>buy</a></div>',
    error_msg_tpl = '<span class="{0}_error" style="color: red;">{1}</span>';

function show_form_errors(selector, messages, clear) {
    var form = $(selector);

    if (clear) {
        _.each(form.find('input, select'), function(item) {
            var field_name = $(item).attr('name');
            if (field_name != undefined) {
                $('.' + field_name + '_error').remove();
            }
        });
    } else {
        _.each(_.keys(messages), function(key) {
            var field_messages = _.map(messages[key], function(message) {
                return error_msg_tpl.format(key, message.message);
            }).join(', ');
            console.log(field_messages);
            console.log();
            if (form.find('.' + key + '_error').length > 0) {
                form.find('.' + key + '_error').replaceWith(field_messages);
            } else {
                form.find('[name=' + key + ']').after(field_messages);
            }
        });
    }
}

function search_results(response) {
    show_form_errors(search_form_selector, null, true);
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
        show_form_errors(search_form_selector, response.errors, false);
    }
}

function show_order_popup(flight_id) {
    var result = $(result_selector.format(flight_id)).find('a').data();

    $(popup_selector).find('input[name=flight]').val(flight_id);
    $(popup_selector).find('input[name=places]').val(result.places);
    $(popup_selector).find('input[name=cost]').val((result.cost / result.places).toFixed(2));
    $(popup_selector).find('input[name=total_cost]').val(result.cost);
    $(popup_selector).modal();
}

function success_lock(response) {
    if (response.status) {
        show_order_popup(response.data);
    }
}

function success_order(response) {
    show_form_errors(order_form, null, true);
    if (response.status) {
        alert('THNX');
    } else {
        show_form_errors(order_form, response.errors, false);
    }
}

function clear_popup() {
    var order_popup = $(popup_selector);
    _.each(order_popup.find('input').not('[name=csrfmiddlewaretoken]'), function(item) {
        $(this).val('');
    });
}

$(document).ready(function() {
    $('#id_date').datepicker();

    $(document).on('click', search_form_selector + ' > input[type=submit]', function(evt) {
        evt.preventDefault();

        $.ajax({
            type: 'POST',
            url: $(search_form_selector).attr('action'),
            data: $(search_form_selector).serialize(),
            success: search_results,
            failure: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus);
            }
        });
    });

    $(document).on('click', buy_btn, function (evt) {
        evt.preventDefault();
        $.ajax({
            type: 'GET',
            url: '/search/lock/?lock={0}'.format($(this).parent().data('id')),
            success: success_lock,
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus);
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
            success: success_order,
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus);
            }
        });
    });
});