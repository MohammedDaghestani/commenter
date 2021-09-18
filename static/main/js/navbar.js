const nav_toggler  = document.getElementById('nav-toggler');
const nav = document.getElementById('nav');
const nav_container = $('#nav-container')
// console.log(nav)
let nav_open = false;
nav_toggler.addEventListener('click', () => {
    if(nav_open){
        nav_toggler.classList.remove('open');
        // nav.classList.remove('nav-open')
        nav_container.slideUp(200)
        nav_open = false;
        
    }
    else{
        nav_toggler.classList.add('open');
        // nav.classList.add('nav-open')
        nav_container.slideDown(200)
        nav_open = true
    }
})