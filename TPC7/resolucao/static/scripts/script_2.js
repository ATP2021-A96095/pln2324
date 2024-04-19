function delete_conceito(designacao){

    $.ajax({
        url: "/conceitos/" + designacao,
        type: "DELETE",
        success: function(result){
            // do something with the result
            alert("delete")
            window.location.href = "/conceitos"
        } 
    });

}

$(document).ready( function () {
    $('#myTable').DataTable();
  
});
