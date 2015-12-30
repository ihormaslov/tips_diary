$(window).load(function(){
    var $grid = $('.grid').masonry({ itemSelector: '.grid-item' });
    var PAGE = 1
    var END = false

    $(window).scroll(function() {
        if($(window).scrollTop() == $(document).height() - $(window).height() && !END) {
            PAGE = PAGE + 1;
            $.get('', {'p':PAGE, 'json':1}, function(data){
                if (data.length == 0){
                    END = true;
                    return false;
                }
                $.each(data, function(index, value){
                    var new_item = '<div class="grid-item col-xs-6 col-sm-6 col-md-4 col-lg-3">' +
                                        '<h4 class="post-title">' +
                                            '<a href="'+ value.get_absolute_url +'">' +
                                                '<img alt="" src="'+ value.preview_image +'" class="preview-img img-responsive"/>' +
                                                value.title +
                                            '</a>' +
                                        '</h4>' +
                                        value.get_excerpt +
                                        '<p class="text-muted meta-info">'+ value.date
                    if (value.viewed > 0){
                        new_item += '<span class="glyphicon glyphicon-eye-open">'+ value.viewed +'</span>'
                    }
                    new_item +='</p></div>'
                    var $elem = $(new_item)
                    $grid.append($elem).masonry('appended', $elem)
                });
            }, 'json');
        }
    });
})


