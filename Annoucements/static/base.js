window.onload = function () {
    var dropdown = document.getElementsByClassName("dropdown-btn");
    var i;

    for (i = 0; i < dropdown.length; i++) {
        dropdown[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === "block") {
                dropdownContent.style.display = "none";
            } else {
                dropdownContent.style.display = "block";
            }
        });
    }


    $(window).scroll(function () {
        if ($(this).scrollTop() >= 100) {        // If page is scrolled more than 50px
            $('#myBtn').fadeIn(200);    // Fade in the arrow
        } else {
            $('#myBtn').fadeOut(200);   // Else fade out the arrow
        }
    });
    $('#myBtn').click(function () {      // When arrow is clicked
        $('body,html').animate({
            scrollTop: 0                       // Scroll to top of body
        }, 'fast');
    });

    var colors = ["#f9b394", "#3997a7", "#c91417", "#b84f96", "#7de0a5", "#525ed4", "#166ad0", "#1ca6c1", "#d97706", "#b48dcd"]

    $('.exampleBox td').each(function (index) {
        $(this).css("background-color", colors[index]);
    })

}

function menu(fctName) {

    $('html, body').animate({ scrollTop: 0 }, 'fast');
    $(".sidebar").each(function () {
        temp = $(this).attr('href');
        temp1 = String(temp);
        temp1 = temp1.substring(1);
        $("#" + temp1).hide();

        temp = String(temp)
        temp2 = temp.substring(1);
        $("#id" + temp2).css('textShadow', 'none');
    });

    $("#" + fctName).show();
    $("#id" + fctName).css('textShadow', '2px 2px 4px #b3cce6');

}
