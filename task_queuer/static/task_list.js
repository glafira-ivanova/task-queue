function get_task_list(){
    $.ajax({url: "task_query", success: function(response){
        response = $.parseJSON(response);
        var table_body = '';
        $(response).each(function(i, item){
                var create_time = new Date(item.create_time)
                var finish_time = item.finish_time ? new Date(item.finish_time): ''
                var tr = '<tr><td>' + item.id + '</td><td>' + create_time.toLocaleString() + '</td><td>'+
                 finish_time.toLocaleString() + '</td><td>' + item.status + '</td></tr>';
                table_body += tr
         });
        $('#task_table_body').html(table_body);
    }});
    setTimeout(function(){get_task_list()}, 1000);
};

$(document).ready(function(){get_task_list();});
