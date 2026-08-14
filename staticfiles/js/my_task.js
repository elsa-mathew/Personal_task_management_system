// ================= Edit Task Modal =================

const editModal = document.getElementById("editModal");

const editButtons = document.querySelectorAll(".edit-btn");

const closeBtn = document.querySelector(".close-btn");

const cancelBtn = document.getElementById("cancelEdit");

const editForm = document.getElementById("editForm");

const taskId = document.getElementById("taskId");
const title = document.getElementById("editTitle");
const description = document.getElementById("editDescription");
const status = document.getElementById("editStatus");
const dueDate = document.getElementById("editDueDate");

const priorityHigh = document.getElementById("priorityHigh");
const priorityMedium = document.getElementById("priorityMedium");
const priorityLow = document.getElementById("priorityLow");

editButtons.forEach(button => {

    button.addEventListener("click", function () {

        editForm.action = "/update-task/" + this.dataset.id + "/";
        editModal.style.display = "block";

        taskId.value = this.dataset.id;

        title.value = this.dataset.title;

        description.value = this.dataset.description;

        status.value = this.dataset.status;

        dueDate.value = this.dataset.dueDate;

        // Set Priority Radio Button

        priorityHigh.checked = false;
        priorityMedium.checked = false;
        priorityLow.checked = false;

        if (this.dataset.priority === "High") {

            priorityHigh.checked = true;

        } else if (this.dataset.priority === "Medium") {

            priorityMedium.checked = true;

        } else {

            priorityLow.checked = true;

        }

    });

});




// Close Modal

closeBtn.addEventListener("click", function () {

    editModal.style.display = "none";

});

// Cancel Button

cancelBtn.addEventListener("click", function () {

    editModal.style.display = "none";

});

// Click Outside Modal

window.addEventListener("click", function (event) {

    if (event.target === editModal) {

        editModal.style.display = "none";

    }

});

const form = document.getElementById("filterForm");

const search = document.getElementById("searchInput");

const filterStatus = document.getElementById("statusFilter");

const filterPriority = document.getElementById("priorityFilter");

const filterSort = document.getElementById("sortFilter");

let timer;

search.addEventListener("keyup", function(){

    clearTimeout(timer);

    timer = setTimeout(function(){

        form.submit();

    },300);

});

filterStatus.addEventListener("change", function(){

    form.submit();

});

filterPriority.addEventListener("change", function(){

    form.submit();

});

filterSort.addEventListener("change", function(){

    form.submit();

});

const deleteModal = document.getElementById("deleteModal");

const deleteButtons = document.querySelectorAll(".delete-btn");

const deleteForm = document.getElementById("deleteForm");

const deleteTitle = document.getElementById("deleteTaskTitle");

const cancelDelete = document.getElementById("cancelDelete");

deleteButtons.forEach(button => {

    button.addEventListener("click", function(){

        deleteModal.style.display = "block";

        deleteTitle.textContent = this.dataset.title;

        deleteForm.action = "/delete-task/" + this.dataset.id + "/";

    });

});

cancelDelete.addEventListener("click", function(){

    deleteModal.style.display = "none";

});

window.addEventListener("click", function(e){

    if(e.target === deleteModal){

        deleteModal.style.display = "none";

    }

});