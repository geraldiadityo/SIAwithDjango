$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-pengguna").modal("show");
            },
            success:function(data){
                $("#modal-pengguna .modal-content").html(data.html_form);
            },
        });
    };
    
    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url:form.attr("action"),
            type:form.attr("method"),
            data:form.serialize(),
            dataType:"JSON",
            success:function(data){
                if (data.form_is_valid){
                    alert("data action success!");
                    $("#table-pengguna tbody").html(data.html_pengguna_list);
                    $("#modal-pengguna").modal("hide");
                }
                else{
                    $("#modal-pengguna .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $("#table-pengguna tbody").on("click",".js-pengguna-delete",loadForm);
    $("#modal-pengguna").on("submit",".js-pengguna-delete-form",saveForm);
});