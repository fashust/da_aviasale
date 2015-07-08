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
    result_item_tpl = '<div data-id={0}><span>{1}</span><span>{2}</span>' +
        '<span>{3}</span><span>{4}</span>' +
        '<a href="#" data-places={5} data-cost={6}>buy</a></div>';

function search_results(response) {
    $(search_results_holder).html();
    if (response.status) {
        console.log('build results');
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

$(document).ready(function() {
    $('#id_date').datepicker();
    $(document).on('click', form_selector + ' > input[type=submit]', function(evt) {
        evt.preventDefault();
        var data = {};
        $(form_selector).serializeArray().map(function(x){
            data[x.name] = x.value;
        });
        $.ajax({
            type: 'POST',
            url: $(form_selector).attr('action'),
            data: data,
            success: search_results,
            failure: function(errMsg) {
                console.log(errMsg);
            }
        });
    });
});