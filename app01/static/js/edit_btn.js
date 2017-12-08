$(document).ready(function () {
    $('.list-group').on('change', '.list-group-item #id_question_choice', function () {
    if ($(this).children('option:selected').val() == 2) {
        $(this).parent().next().removeClass('hide');
        $(this).next().removeClass('hide');
    }else{
        $(this).parent().next().addClass('hide');
        $(this).next().addClass('hide');
    }
});

    $('.list-group').on('click','.list-group-item .x' ,function () {
        $(this).parent().remove()

    });

    $('.list-group').on('click','.list-group-item .innerX' ,function () {
        $(this).parent().remove()

    });


    $('.add_btn').click(function () {
        var ele_li =$('ol>li').last().clone();
        ele_li.find('#id_title').val('');
        ele_li.find('div').removeAttr('id');

        // ele_li.find('select option').first().alert(123);
        ele_li.find('ul li').removeAttr('id');
        $('ol').append(ele_li)
    });
    
    $('.list-group').on('click','.add_choice',function () {
        var inner_li=$('ol ul>li').first().clone();
        $('#id_captions').val('');
        $('#id_score').val('');
        $('ol ul').append(inner_li)
    });
    
    
    $('.btn_save').click(function () {
        lst=[];
        $('ol>li').each(function () {

            var quest_id=$(this).find($('div')).first().attr('id');
            var quest_name=$(this).find($("[name = 'title']")).val();
            var type_name=$(this).find($("[name = 'question_choice']")).val();

             option = [];
            lst.push({'quest_id':quest_id,'quest_name':quest_name,'type_name':type_name,'option':option});

            $(this).find("ul>li").each(function () {
                if (type_name === "2"){
                    var option_id= $(this).attr('id');
                     var option_content=$(this).find($("[name='captions']")).val();
                     var option_score=$(this).find($("[name='score']")).val();
                    option.push({'option_id':option_id,'option_content':option_content,'option_score':option_score})
                }
            })
        });
        console.log(lst);
        $.ajax({
            url:'/save/',
            type:'post',
            headers:{"X-CSRFToken":$.cookie('csrftoken')},
            data: {'lst':JSON.stringify(lst)},
            // contentType:'json',
            success:function (data) {
                console.log(data)
            }

        })
    })
});







