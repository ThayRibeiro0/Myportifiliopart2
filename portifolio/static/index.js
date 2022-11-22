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

var swiper = new Swiper(".move-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
      0:{
        slidesPerView: 1,
      },
      520:{
        slidesPerView: 2,
      },
      950:{
        slidesPerView: 3,
      },
    },
  });

