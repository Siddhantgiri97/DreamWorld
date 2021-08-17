
/*==================== SWIPER JS ====================*/



let galleryThumbs = new Swiper('.gallery-thumbs', {
    spaceBetween: 0,
    slidesPerView: 0,
})

let galleryTop = new Swiper('.gallery-top', {
    effect: 'fade',
    loop: true,

    thumbs: {
        swiper: galleryThumbs
    }
})



/*==================== POPUP ====================*/
const btnOpenVideo = document.querySelectorAll('.automobiles__video-content')
const automobilesPopup = document.getElementById('popup')

function poPup() {
    automobilesPopup.classList.add('show-popup')
}
btnOpenVideo.forEach(b => b.addEventListener('click', poPup))

const btnCloseVideo = document.getElementById('popup-close')

btnCloseVideo.addEventListener('click', () => {
    automobilesPopup.classList.remove('show-popup')
})

/*==================== GSAP ANIMATION ====================*/
const controlImg = document.querySelectorAll('.controls__img')

function scrollAnimation() {
    gsap.from('.automobiles__subtitle', { opacity: 0, duration: .2, delay: .2, y: -20 })
    gsap.from('.automobiles__title', { opacity: 0, duration: .3, delay: .3, y: -20 })
    gsap.from('.automobiles__description', { opacity: 0, duration: .4, delay: .4, y: -20 })
    gsap.from('.automobiles__button', { opacity: 0, duration: .5, delay: .5, y: -20 })
    gsap.from('.automobiles__video-content', { opacity: 0, duration: .6, delay: .6, y: -20 })

    automobilesPopup.classList.remove('show-popup')
}

controlImg.forEach(c => c.addEventListener('click', scrollAnimation))