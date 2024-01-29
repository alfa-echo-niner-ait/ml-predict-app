$(document).ready(function () {
    // Post data
    $("#submitData").click(function () {
        $("#resText").show()
        $("#resText").html("Loading....");
        hp = $("#hp").val();
        wt = $("#wt").val();
        $("#hp").val("");
        $("#wt").val("");

        $.ajax({
            type: "POST",
            url: predict_url,
            data: {
                hp: hp,
                wt: wt
            },
            success: function (response) {
                $("#resText").html(response);
            }
        });
    });
});