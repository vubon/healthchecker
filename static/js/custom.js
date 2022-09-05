$('.nav li a').click(function () {
    localStorage.setItem('active-menu-item', $(this).attr("href"));
});

$(document).ready(function () {
    const activeMenuItem = $('.nav [href="' + localStorage.getItem('active-menu-item') + '"]').first();
    console.log(activeMenuItem);
    activeMenuItem && setActiveLink(activeMenuItem);
});

function setActiveLink($el) {
    $(".nav li").removeClass("active");
    $el.parent().addClass('active');
    $el.click();
}
