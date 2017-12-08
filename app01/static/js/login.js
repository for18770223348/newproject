$(document).ready(function () {
    $('.subBtn').click(function () {
        $.ajax({
            url:'/login/',
            type:'POST',
            headers:{"X-CSRFToken":$.cookie('csrftoken')},
            data:{
                name:$('.username').val(),
                password:$('.password').val()
            },
            success:function (data) {
                var response=JSON.parse(data);
                if(response.is_name){
                    if(response.is_password){
                        if(response.is_login){
                            alert(123);
                            location.href='/index/'
                        }
                        else{
                            $('.answer').html('账号密码错误')
                        }
                    }
                    else{
                        $('.answer').html('密码不能为空')
                    }
                }
                else if(response.is_name == null&&response.is_password == null){
                    $('.answer').html('账号和密码不能为空')
                }
                else{
                    $('.answer').html('账号不能为空')
                }

            }

        })

    })
})
