/**************************************
    save detail data
**************************************/
function save_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var $cur_detail = $detail_focus.find('.ui_overview_area');
    var detail_id = $detail_focus.data('id');
    var itec_ip = $cur_detail.find('.itec_ip').val();

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = "So sorry, add iTEC failed !";
        data["itec_method"] = "_add_itec";
    } else {
        msg = "So sorry, modify iTEC failed !";
        data["itec_method"] = "_modify_itec";
        para['id'] = detail_id;
    }

    if (itec_ip == "") {
        show_error_dialog("Server IP cannot be null.");
        return;
    } else {
        para["itec_ip"] = itec_ip;
    }
    para['itec_name'] = $cur_detail.find('.itec_name').val();
    data["itec_para"] = JSON.stringify(para);

    /**************************************
     1. Add item:
        a. clear filter area.
        b. show all item.
        c. and stay on first page.
     2. Modify item:
        a. combined with filter to show item.
        b. stay on current page.
    **************************************/
    if (typeof(detail_id) == 'undefined') {
        ajax_func(data, msg, callback_detailArea);
        clear_all_filter();
    } else {
        var save_callback = function() {
            var page = get_current_page();
            itec_filter(!!page ? page : 1);
        };
        ajax_func(data, msg, save_callback);
    }
}

/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete app failed !';
    var itec_id = $detail_focus.data('id');

    if (typeof(itec_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }
    var para = {
        id: itec_id
    };
    var data = {
        'itec_method': '_delete_itec',
        'itec_para': JSON.stringify(para)
    };

    /**************************************
     DELETE Item:
        a. combined with filter to show item.
        b. stay on current page.
    **************************************/
    var delete_callback = function() {
        var page = get_current_page();
        itec_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    itec filter
**************************************/
function itec_filter() {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var itec_name = $('.ui_item_name_search').val();

    if (itec_name != '') {
        para['itec_name'] = itec_name;
    }

    var data = {
        'itec_method': '_search_itec',
        'itec_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, iTEC filter failed !';
    ajax_func(data, msg, callback_detailArea);
}

/*******************************************
    change page
*******************************************/
function change_page(e) {
    var page = 1,
        $clickDom = $(e.target);

    if ($clickDom.hasClass("page")) {
        page = $clickDom.text();
    } else if($clickDom.hasClass("previous") || $clickDom.hasClass("next")) {
        page = $clickDom.data("page");
    } else {
        return;
    }

    itec_filter(page);
}

/*******************************************
    get worker info callback
*******************************************/
var callback_workerArea = function(data) {
    var $ui_detail_focus = $('.ui_detail_focus');
    var index = $('.ui_detail_info').index($ui_detail_focus);
    var $new_item = $(data).find('.ui_detail_info').eq(index);
    $ui_detail_focus.find(".worker_area").empty()
        .append($new_item.find('.worker_area').children());

    var $detail = $ui_detail_focus.find('.worker_area').find('#detail');
    resize_table($detail);
    $('.ui_loader_area').hide();
}