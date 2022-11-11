function reloadFileList(){
    $("#fileList").html('');
    $.ajax({
        url: "/file/jFilesOut2S",
        type: "POST",
        async: false,
        dataType: "json",
        contentType: "application/json",
        success: function(res){
            for(let fileListLine of res.ret){
                let code = `<div class="fileListLine">${fileListLine}</div>`;
                $("#fileList").append(code);
            }
        }
    });
}

function deleteFile(){
    $("#deleteBtn").on("click", function(){
        $.ajax({
            url: "/file/aDeleteFiles",
            type: "POST",
            async: true,
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({fileName : $("#deleteInp").val()}),
            success: function(res){
            }
        });
        reloadFileList();
    });
}

$(document).ready(function(){
    history.pushState(null, null, location.href);
    window.onpopstate = function () {
        history.go(1);
    };
    reloadFileList();
    deleteFile();
});