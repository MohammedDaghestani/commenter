const post_overview = document.getElementsByClassName('post-overview');
const post_img = document.getElementsByClassName('post-img');
function reorder(){
    if(window.innerWidth <= 991){
        for(var i = 0; i < post_overview.length; i++){
            post_overview[i].classList.add('order-2');
            post_img[i].classList.add('order-1');

        }
    } else{
        for(var i = 0; i < post_overview.length; i++){
            post_overview[i].classList.remove('order-2');
            post_img[i].classList.remove('order-1');

        }
    }
}

document.onload = reorder();
window.addEventListener('resize', reorder);
window.addEventListener('resize', () => {
    console.log(window.innerWidth);
});