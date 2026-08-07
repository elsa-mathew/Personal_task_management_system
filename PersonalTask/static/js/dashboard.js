

const createModal = document.getElementById("createTaskModal");

const openCreate = document.getElementById("openCreateModal");

const closeCreate = document.getElementById("closeCreateModal");

const cancelCreate = document.getElementById("cancelCreateTask");

openCreate.addEventListener("click", function(){

    createModal.style.display = "block";

});

closeCreate.addEventListener("click", function(){

    createModal.style.display = "none";

});

cancelCreate.addEventListener("click", function(){

    createModal.style.display = "none";

});

window.addEventListener("click", function(e){

    if(e.target === createModal){

        createModal.style.display = "none";

    }

});

