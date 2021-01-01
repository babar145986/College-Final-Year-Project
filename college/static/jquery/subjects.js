$("#id_select_semister").change(function () {
    var url = $("#SearchForm").attr("data-semister-url");
    var semisterId = $(this).val();

    $.ajax({
        url: url,
        data: {
            'select_semister': semisterId
        },
        success: function (data) {
            $("#id_select_subject").html(data);
        }
    });
});

