const change_img_btn = document.getElementById('change-pic');
const file_upload = document.getElementById('change-img');
const upload_btn = document.getElementById('upload-btn');
// const change_name_btn = document.getElementById('change-name');

change_img_btn.onclick = function(){
    file_upload.click()
}

file_upload.addEventListener('change', function(){
    upload_btn.click()
})

// change_name_btn.onclick = function() {
//     window.location.href = window.location.href + 'name/change'
// }