$(function(){
    var loadTable = function(){
       var btn = $(this);
       var akun = btn.attr("data-id");
       var nama = btn.attr("data-nama");
       $.ajax({
           url:btn.attr("data-url"),
           type:"GET",
           data:{akun_id:akun,nama:nama},
           dataType:"JSON",
           success:function(data){
               $("#nama_akun").text(nama);
               $("#table-bukubesar tbody").html(data.html_buku_akun_list);
           },
           
       });

        
    };
    $(".js-load-table").click(loadTable);
});