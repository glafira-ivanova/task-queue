$(document).ready(function(){
    $("#add_task").click(function(){
        $.ajax({url: "add_task"});
    });
});


