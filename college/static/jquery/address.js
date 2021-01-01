$("#id_select_course").change(function() {
    var url = $("#SearchForm").attr("data-semister-url");
    var courseId = $(this).val();

    $.ajax({
        url:url,
            data: {
                'select_course': courseId
                },
            success: function (data) {
            $("#id_select_semister").html(data);
                        }
                    });
                });