const passwordModal = document.getElementById("passwordModal");

const changePasswordBtn = document.getElementById("changePasswordBtn");

const closePassword = document.querySelector(".close-password");

const cancelPassword = document.getElementById("cancelPassword");

changePasswordBtn.addEventListener("click", function(){

    passwordModal.style.display = "block";

});

closePassword.addEventListener("click", function(){

    passwordModal.style.display = "none";

});

cancelPassword.addEventListener("click", function(){

    passwordModal.style.display = "none";

});

window.addEventListener("click", function(e){

    if(e.target == passwordModal){

        passwordModal.style.display = "none";

    }

});