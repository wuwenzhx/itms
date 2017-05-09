/**************************************
    ajax function
**************************************/
function ajax_func(data, msg, callback) {
    var handle = arguments[3] ? arguments[3]: null;
    var async_flag = arguments[4] ? arguments[4]: true;
    var is_self_attr = arguments[5] ? arguments[5]: false;
    $.ajax({
        async: async_flag,
        type: "POST",
        data: data,
        beforeSend: function (xhr, settings) {
            console.log("beforeSend function!~");
            csrftokenFun(xhr, settings);
        },
        complete: function (jqXHR, status) {
            if ("success" == status) {
                console.log("success");
            } else if ("timeout" == status) {
                console.log("timeout");
            } else {
                console.log(status);
                show_error_dialog(msg);
            }
        },
        success: function (data) {
            if (check_status(data, is_self_attr) == false) {
                return;
            }
            if (callback) {
                callback(data, handle);
            }
        }
    });
}

/**************************************
    check status
**************************************/
function check_status(data, is_self_attr) {
    var $callback_status = null;
    if (is_self_attr) {
        $callback_status = $(data).find('.type_callback_status');
    } else {
        $callback_status = $(data).find('.callback_status');
    }

    if ($callback_status.data('status') == "ERROR") {
        show_error_dialog($callback_status.data('message'));
        return false;
    }
    return true;
}

/**************************************
    show detail info
**************************************/
function show_detail_info() {
    if (is_exist_unsaved()) {
        return;
    }
    var $cur_detail = $(this).next();
    // close the opened detail area
    $('.ui_detail_info').hide().removeClass('ui_detail_focus');
    $('.ui_list').show();

    // show clicked detail
    $(this).hide();
    $cur_detail.show().addClass('ui_detail_focus');

    // initialize the tab, tab on the overview
    $cur_detail.find('.ui_related_data_area').hide();
    $cur_detail.find('.ui_overview_area').show();
    $cur_detail.find('.ui_tab_focus').removeClass('ui_tab_focus');
    $cur_detail.find('#tab_0').addClass('ui_tab_focus');
}

/**************************************
    close detail info
**************************************/
function close_detail_info() {
    if (is_exist_unsaved()) {
        return;
    }
    var $detail = $(this).parent();
    $detail.hide();
    $detail.prev().show();
}

/**************************************
    switch tab to show detail area
**************************************/
function switch_tab() {
    var cur_index = $(this).parent().find('.ui_tab_focus').attr('id').split('tab_')[1];
    $(this).siblings().removeClass('ui_tab_focus');
    $(this).switchClass('', 'ui_tab_focus', 150);

    var click_index = $(this).attr('id').split('tab_')[1];
    var $detail_box = $(this).parent().next().children();
    var $specific_box = $detail_box.eq(click_index);
    $detail_box.eq(cur_index).hide();
    $specific_box.show();

    if (click_index != 0 && typeof(get_related_data) !== 'undefined') {
        var para = {
            'data': {
                'is_search': false,
                'related_obj': $(this).data('related_obj')
            }
        };
        get_related_data(para);
        $('.ui_loader_area').show();
    }
}

/**************************************
    filter button event
**************************************/
function show_filter_box() {
    $('.ui_edit_self_attr_area').hide('blind');
    $('.ui_filter_item_area').toggle('blind');
}

/**************************************
    edit type button event
**************************************/
function show_edit_self_box() {
    $('.ui_filter_item_area').hide('blind');

    var tpl = $.extend(true, {}, $('.ui_edit_self_attr_area'));
    $('.ui_detail_area').before(tpl);
    tpl.toggle('blind');
}

/**************************************
    close filter dialog
**************************************/
function close_filter_dialog() {
    var $filter_dialog = $('.ui_related_filter_dialog');
    $filter_dialog.hide();
    $('.ui_black_background').hide();

    // clear filter displayed data
    $filter_dialog.find('.filter').val('').change();
}

/**************************************
    close filter dialog
**************************************/
function close_filter_dialog_2() {
    var $filter_dialog = $('.ui_related_filter_dialog_2');
    $filter_dialog.hide();
    $('.ui_black_background').hide();

    // clear filter displayed data
    $filter_dialog.find('.filter').val('').change();
}

/**************************************
    show confirmation alter
**************************************/
function show_confirm_dialog() {
    var $confirm_alert = $('.ui_confirm_alert');
    var starter = $(this).data('starter');

    if ($(this).hasClass('ui_save')) {
        $confirm_alert.find('.alert_content').text('Are you sure you want to save it ?');
    } else if ($(this).hasClass('ui_del')) {
        $confirm_alert.find('.alert_content').text('Are you sure you want to delete it ?');
    }
    $confirm_alert.show().data({
        'starter': starter,
        'start_dom': $(this)
    });
}

/**************************************
    close confirmation alter
**************************************/
function close_confirm_dialog() {
    var $confirm_alert = $('.ui_confirm_alert');
    $confirm_alert.hide();
    var starter = $confirm_alert.data('starter');
    var start_dom = $confirm_alert.data('start_dom');
    if ($(this).hasClass('ui_yes')) {
        switch (starter) {
            case 'del_self_attr':
                delete_attr();
                break;
            case 'save_self_attr':
                save_attr();
                break;
            case 'save_detail':
                save_detail();
                break;
            case 'delete_detail':
                delete_detail();
                break;
            case 'save_relation':
                var related_obj = $('.ui_detail_focus').find('.ui_tab_focus').data('related_obj');
                save_relation(related_obj);
                break;
            case 'save_appAttr':
                save_attr(start_dom);
                break;
            case 'delete_appAttr':
                delete_attr(start_dom);
                break;
            default:
                break;
        }
    }
}

/**************************************
    add item attr
**************************************/
function add_attr() {
    var $edit_attr_area = $('.ui_edit_self_attr_area');
    if ($edit_attr_area.find('.ui_attr_edit_flag').length > 0) {
        show_error_dialog('Please save the unsaved data !');
        return;
    }
    // clear selected flag
    $edit_attr_area.find('.ui_attr_selected_flag').removeClass('ui_attr_selected_flag');
    $edit_attr_area.find('.ui_attr_edit_flag').removeClass('ui_attr_edit_flag');

    var tpl = $('.ui_self_attr_tpl').clone(true);
    $(tpl).removeClass('.ui_self_attr_tpl').addClass('edit_self_attr_box').show();
    $edit_attr_area.find('input').removeAttr('checked');
    $edit_attr_area.append(tpl);
    var $new_attr = $edit_attr_area.find('.edit_self_attr_box').last();
    $new_attr.find('input').select();
}

/**************************************
    show error alter
**************************************/
function show_error_dialog(str) {
    $('.ui_error_alert').show().find('.alert_content').text(str);
}

/**************************************
    close confirmation alter
**************************************/
function close_error_dialog() {
    $('.ui_error_alert').hide();
}

/**************************************
    item link
**************************************/
function open_item_link() {
    if ($(this).css('cursor') == 'pointer') {
        window.open($(this).prev().val());
    }
}

/******************************************
    check whether there are no saved item
*******************************************/
function is_exist_unsaved() {
    if ($('.ui_detail_area').find('.ui_new_detail').length > 0) {
        show_error_dialog('Please save the unsaved data !');
        return true;
    }
    return false;
}

/**************************************
    new item
**************************************/
function new_item() {
    var $detail_area = $('.ui_detail_area');
    if (is_exist_unsaved()) {
        return;
    }

    // close the opened detail area
    $('.ui_detail_info').hide().removeClass('ui_detail_focus');
    $('.ui_list').show();

    var tpl = $('.ui_new_detail').clone();
    tpl.find('.app_select')
        .addClass('ui_select_disabled')
        .attr('disabled', 'disabled')
        .find('option').removeAttr('selected');

    tpl.find('.time').val(get_cur_datetime());
    $detail_area.find('.detail_area').prepend(tpl);
    $('.ui_detail_area .ui_new_detail').show().addClass('ui_detail_focus');

    bind_event();
}

/*******************************************
    set select item style on related box
*******************************************/
function selected_related_item() {
    var $title_box;
    if ($(this).parent().prev().hasClass('tool_bar')){
        // right_box 'select all'
        $title_box = $(this).parent().prev();
    } else {
        // left_box 'select all'
        $title_box = $(this).parent().parent().prev();
    }

     if($(this).hasClass('ui_selected_related_item')) {
         // if selected remove checked
         $(this).find("input").prop("checked", false);
         $(this).removeClass('ui_selected_related_item');
         // uncheck 'select all'
         $title_box.find('.title_check_box').removeClass(".select_all_items");
         $title_box.find('.title_check_box').attr("title", "select all");
     } else {
         // if unselected add checked
        $(this).addClass('ui_selected_related_item');
        $(this).find("input").prop("checked", true);

         // check 'select all' if all items are selected
         var selected_items = $(this).parent().find('.ui_selected_related_item').size();
         var all_items = $(this).parent().find('.ui_related_item').size();
         if (selected_items == all_items){
             $title_box.find('.title_check_box').addClass(".select_all_items");
             $title_box.find('.title_check_box').attr("title", "cancel all");
         }
     }
}

/*******************************************
    move item to right box on related box
*******************************************/
function move_to_right() {
    var $tooltip = $(this).parent();
    var $left_box = $tooltip.prev();
    var $right_box = $tooltip.next();
    var selected_dom = $left_box.find('.ui_selected_related_item');
    selected_dom.removeClass('ui_selected_related_item');

    selected_dom.each(function(){
        $(this).hasClass('ui_related_unsaved_item') ?
            $(this).removeClass('ui_related_unsaved_item'):
            $(this).addClass('ui_related_unsaved_item');
    });
    selected_dom.find("input").prop("checked", false);
    $right_box.find('.data_box').append(selected_dom);
    update_select_all_status($tooltip);
}

/*******************************************
    move item to left box on related box
*******************************************/
function move_to_left() {
    var $tooltip = $(this).parent();
    var $left_box = $tooltip.prev();
    var $right_box = $tooltip.next();
    var selected_dom = $right_box.find('.ui_selected_related_item');
    selected_dom.removeClass('ui_selected_related_item');

    selected_dom.each(function(){
        $(this).hasClass('ui_related_unsaved_item') ?
            $(this).removeClass('ui_related_unsaved_item'):
            $(this).addClass('ui_related_unsaved_item');
    });
    selected_dom.find("input").prop("checked", false);

    $left_box.find('.data_content').append(selected_dom);
    update_select_all_status($tooltip);
}

/*******************************************
    update 'select all' checkbox status
*******************************************/
function update_select_all_status($tooltip) {
    var $left_select_all = $tooltip.prev().find('.title_check_box');
    var $right_select_all = $tooltip.next().find('.title_check_box');
    // uncheck 'select all' in both boxes
    $right_select_all.attr("title", "select all")
        .removeClass('.select_all_items');
    $left_select_all.attr("title", "select all")
        .removeClass('.select_all_items');
}

/*******************************************
    filter items by the filter condition
*******************************************/
function filter_item() {
    var starter = $(this).data('starter');
    switch (starter) {
        case 'testcase':
            case_filter();
            break;
        case 'requirement':
            req_filter();
            break;
        case 'feature':
            feature_filter();
            break;
        case 'testsuite':
            suite_filter();
            break;
        case 'testplan':
            plan_filter();
            break;
        case 'app':
            app_filter();
            break;
        default:
            break;
    }
}

/*******************************************
    clear filter condition
*******************************************/
function cancel_filter_item() {
    var update_detailArea = arguments[0] ? arguments[0] : null;
    ajax_func(null, '', callback_filterArea, update_detailArea);
}

/*******************************************
    update detail area
*******************************************/
var callback_detailArea = function (data) {
    var func = arguments[1]?arguments[1]:null;
    $('.ui_detail_area').empty()
        .append($(data).find('.ui_detail_area').children());
    bind_event();
    if (func) {
        func(data);
    }
};

/***********************************************
    update related area after get related data
***********************************************/
var callback_relatedArea = function (data, para) {
    var $related_data_area = $('.ui_detail_focus').find('.ui_related_data_area');
    var tpl = null;

    switch (para.related_obj) {
        case 'requirement':
            tpl = $(data).find('.ui_requirement_related_box_tpl').clone();
            break;
        case 'feature':
            tpl = $(data).find('.ui_feature_related_box_tpl').clone();
            break;
        case 'testcase':
            tpl = $(data).find('.ui_testcase_related_box_tpl').clone();
            break;
        case 'testsuite':
            tpl = $(data).find('.ui_testsuite_related_box_tpl').clone();
            break;
        case 'testplan':
            tpl = $(data).find('.ui_testplan_related_box_tpl').clone();
            break;
        default:
            break;

    }

    $related_data_area.find('.ui_related_data_box').remove();
    $related_data_area.append(tpl.addClass('ui_related_data_box')
        .removeClass('.ui_related_box_tpl').show());

    if (para.is_search) {
        var filter_str = 'Filter: All';
        if (Object.keys(para.search_data).length) {
            filter_str = 'Filter: ' + JSON.stringify(para.search_data);
        }
        $related_data_area.find('.filer_content').text(filter_str).attr('title', filter_str);
    }
    bind_event();
    $('.ui_loader_area').hide();
};

/*******************************************
    update right box related area
    after saved related data
*******************************************/
var callback_relatedBoxArea = function () {
    $('.ui_detail_focus').find('.ui_related_data_box')
        .find('.ui_related_item')
        .removeClass('ui_related_unsaved_item');
};

/*******************************************
    update attr area
*******************************************/
var callback_selffAttrArea = function () {
    $.get(window.location.href, function(data) {
        // update self attr box
        var $self_attr_area = $('.ui_edit_self_attr_area');
        $self_attr_area.find('.edit_self_attr_box').remove();
        $self_attr_area.append($(data).find('.edit_self_attr_box'));

        // update detail area
        $('.ui_detail_area').empty()
            .append($(data).find('.ui_detail_area').children());

        // clear name search
        $('.ui_item_name_search').val('');

        // update filter box
        $('.ui_filter_item_area').empty()
            .append($(data).find('.ui_filter_item_area').children());

        // update .ui_new_detail tpl
        $('.ui_new_detail').empty()
            .append($(data).find('.ui_new_detail').children());

        // bind event
        bind_event();
        if (typeof(cascade_filter_event) !== 'undefined') {
            cascade_filter_event();
        }
    });
};

/*******************************************
    select self attr
*******************************************/
function set_selected_flag() {
    // Clear the selected but does not contain himself
    $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag')
        .not(this).removeClass('ui_attr_selected_flag');

    $(this).toggleClass('ui_attr_selected_flag');
}
function set_prev_selected_flag() {
    // Clear the selected but does not contain himself
    $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag')
        .not(this).removeClass('ui_attr_selected_flag');

    $(this).prev().toggleClass('ui_attr_selected_flag');
}

/*******************************************
    checked self attr (radio)
*******************************************/
function set_edit_flag() {
    $(this).addClass('ui_attr_edit_flag');
}

/*******************************************
    update cascade filter item box
*******************************************/
var callback_cascadeFilterBox = function (data, dom) {
    var $old_dom = $(dom);
    var $new_dom = $(data).find('.' + $old_dom.attr('name'));
    $old_dom.parent().next().empty()
        .append($new_dom.parent().next().children());
};

/*******************************************
    update filter area
*******************************************/
var callback_filterArea = function (data) {
    var update_detailArea = arguments[1] ? arguments[1] : null;
    var $filter_area = $('.ui_filter_item_area');
    $filter_area.find('.ui_filter_item').remove();
    $filter_area.append($(data).find('.ui_filter_item'));

    if (typeof(cascade_filter_event) !== 'undefined') {
         cascade_filter_event();
    }
    if (typeof(update_detailArea) === 'function') {
        update_detailArea(data);
    }
};

/*******************************************
    get current page number
*******************************************/
function get_current_page() {
    return $('.ui_paginator').find('.current').text();
}

/*******************************************
    clear all filter word
*******************************************/
function clear_all_filter() {
    var update_detailArea = arguments[0] ? arguments[0] : null;
    $('.ui_item_name_search').val('');
    cancel_filter_item(update_detailArea);
}

/*******************************************
    clear all filter word
*******************************************/
function get_cur_datetime() {
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();

    return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
}

/*******************************************
    change app selection whether can select
*******************************************/
function change_app_select() {
    if ($(this).val() === 'True') {
        $('.app_select')
            .removeClass('ui_select_disabled')
            .removeAttr('disabled');
    } else {
        $('.app_select')
            .addClass('ui_select_disabled')
            .attr('disabled', 'disabled')
            .find('option').removeAttr('selected');
    }
}

/*******************************************
    get filter item data
*******************************************/
function get_filter_dialog_data() {
    var data = {};
    var $self = $(this);
    var plugin_name = $self.data('plugin');
    var plugin_method = plugin_name + '_method';
    var plugin_para = plugin_name + '_para';
    var related_obj = $('.ui_detail_focus').find('.ui_tab_focus').data('related_obj');
    var msg = 'So sorry, get related filter data failed !';

    data[plugin_method] = '_get_related_filter_data';
    data[plugin_para] = JSON.stringify({'related_obj': related_obj});

    var dialog_class = '.ui_related_filter_dialog';
    if ($self.hasClass('find_icon_2')) {
        dialog_class = '.ui_related_filter_dialog_2';
    }

    ajax_func(data, msg, callback_updateRelatedFilterDialog, dialog_class);
}

/*******************************************
    update and show related filter dialog
*******************************************/
function callback_updateRelatedFilterDialog(data, dialog_class) {
    var $dialog = $(dialog_class);
    $dialog.find('.filter_group').remove();
    $dialog.find('hr').after($(data).find(dialog_class).find('.filter_group'));
    $dialog.show();
    $('.ui_black_background').show();
    if (typeof (related_cascade_filter_event) !== 'undefined') {
        related_cascade_filter_event();
    }
}

/*******************************************
    set all item style on related box
*******************************************/
function select_all_related_data() {
    var $related_item = $(this).parent().parent().next().find('.ui_related_item');
    if ($(this).hasClass('.select_all_items')) {
        //if selected remove checked
        $(this).attr("title", "select all");
        $(this).removeClass('.select_all_items');
        $related_item.find("input").prop("checked", false);
        $related_item.removeClass('ui_selected_related_item');
    } else {
        // if unselected add checked
        $(this).attr("title", "cancel all");
        $(this).addClass('.select_all_items');
        $related_item.find("input").prop("checked", true);
        $related_item.addClass('ui_selected_related_item');
    }
}

/*******************************************
    bind event
*******************************************/
function bind_event() {
    $('.ui_list').off().on('click', show_detail_info);
    $('.ui_detail_header').off().on('click', close_detail_info);
    $('.ui_detail_tab').off().on('click', switch_tab);
    $('.ui_filter_btn').off().on('click', show_filter_box);
    $('.ui_edit_type_btn').off().on('click', show_edit_self_box);
    $('.ui_filter_dialog_search_btn').off().on('click',
        {'is_search':true},
        typeof(get_related_data) !== 'undefined' ? get_related_data: null
    );
    var $ui_related_data_box = $('.ui_related_data_box');
    $ui_related_data_box.find('.find_icon').off().on('click', get_filter_dialog_data);
    $ui_related_data_box.find('.title_check_box').off().on('click', select_all_related_data);
    $('.ui_save, .ui_del').off().on('click', show_confirm_dialog);
    $('.ui_confirm_alert button').off().on('click', close_confirm_dialog);
    $('.ui_error_alert button').off().on('click', close_error_dialog);
    $('.item_link').off().on('click', open_item_link);
    $('.ui_add_btn').off().on('click', new_item);
    $('.ui_related_item').off().on('click', selected_related_item);
    var $related_data_area = $('.ui_related_data_area');
    var $edit_self_attr_area = $('.ui_edit_self_attr_area');
    $related_data_area.find('.arrows_r').off().on('click', move_to_right);
    $related_data_area.find('.arrows_l').off().on('click', move_to_left);
    $('.ui_self_attr_tpl').find('.attr_img').off().on('click', set_selected_flag);
    $edit_self_attr_area.find('.attr_img').off().on('click', set_selected_flag);
    $edit_self_attr_area.find('.attr_name')
        .off().on({'change': set_edit_flag, 'click': set_prev_selected_flag});
    $edit_self_attr_area.find('.ui_add').off().on('click', add_attr);
    $('.ui_filter, .ui_item_name_search_icon').off().on('click', filter_item);
    $('.ui_cancel_filter').off().on('click', cancel_filter_item);
    $('.ui_paginator').off().on('click', change_page);
    $('.perf_select').off().on('change', change_app_select);
    $('.ui_related_filter_dialog').find('.ui_filter_dialog_close_btn')
        .off().on('click', close_filter_dialog);
    $('.ui_related_filter_dialog_2').find('.ui_filter_dialog_close_btn')
        .off().on('click', close_filter_dialog_2);

}

if ($('.callback_status').data("request-method") == "GET") {
    clear_all_filter();
}

bind_event();