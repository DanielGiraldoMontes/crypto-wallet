
$(document).ready(function () {
    $('#trans').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            data: {
                address: $('#address').val(),
                opt: $('#opt').val(),
                value: $('#value').val(),
                secret: $('#secret').val(),
            },
            type: 'POST',
            url: '/transaccion/'
        })
            .done(function (data) {
                if (data.status === "error") {
                    alert(data.message);
                    if (data.message == "LA SESIÓN EXPIRÓ") {
                        window.location.href = data.location;
                    }
                } else {
                    $("#exampleModal").modal('hide');
                    alert(data.message);
                    window.location.href = data.location;
                }
            });
    });
});


$(document).ready(function () {
    $('#login').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            data: {
                email: $('#email').val(),
                password: $('#password').val(),
                remember: $('#remember').is(':checked') ? $('#remember').val() : 'False',
            },
            type: 'POST',
            url: '/login/'
        })
            .done(function (data) {
                if (data.status === "error") {
                    alert(data.message);
                } else {
                    window.location.href = data.location;
                }
            });
    });
});


$(document).ready(function () {
    $('#signup').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            data: {
                name: $('#name').val(),
                email: $('#email').val(),
                password: $('#password').val(),
            },
            type: 'POST',
            url: '/signup/'
        })
            .done(function (data) {
                if (data.status === "error") {
                    alert(data.message);
                } else {
                    window.location.href = data.location;
                }
            });
    });
});

