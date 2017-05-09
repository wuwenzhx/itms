function upload() {
    event.preventDefault();
    var data = new FormData($('form').get(0));
    $.ajax({
        data: data,
        type: 'POST',
        url: $(this).attr('action'),
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            upload_file_callback(data);
        }
    });
    return false;
}

var upload_file_callback = function(data) {

    $('.callback').empty()
        .append($(data).find('.callback').children());
}

$(function(){
    var uploadfiles = document.querySelector('#file_input');
    uploadfiles.addEventListener('change', function () {
        $('.callback').find('span').text("");
        var $file_list = $('.file_list'),
            files = this.files;
        $file_list.empty();

        if (files.length > 1) {
            $file_list.append('<div><span>The files you have chosen are: </span></div>');
        } else {
            $file_list.append('<div><span>The file you have chosen is: </span></div>');
        }
        for(var i=0; i<files.length; i++){
            var size = (parseFloat(files[i].size) / 1024).toFixed(1);
            $file_list.append('<div>'+this.files[i].name+' '+size+'kB </div>');
        }
        $file_list.show();
    }, false);
    $('#upload_form').submit(upload);
});
