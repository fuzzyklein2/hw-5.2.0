$(function() {
    // Your code here
});

$("#loadBtn").click(function() {
    $.get("cgi-bin/index.py", function(response) {
        $("#output").html(response);
    });
});

