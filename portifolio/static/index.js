function togglenav() {
    $('nav').toggleClass('open')
}

var typed = new Typed(".auto-type", {
    strings: ["Lawyer", "Systems Developer", "Administrator", "Lawyer"],
    typeSpeed: 130,
    backSpeed: 100,
    loop: true
});

window.addEventListener('hashchange', () => {
    const path = location.hash.replace('#', '')
    console.log('location.hash change:', path)
    
    const element = $('.' + path).offset()

    $('html').animate({
        scrollTop: element.top
    }, 255)
});
