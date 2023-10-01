function loadTasks() {
    $.ajax({
        url: '/tasks',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            let taskList = $('#taskList');
            taskList.empty();
            data.forEach(function (task) {
                let listItem = $('<li>');
                listItem.append(task.title + ': ' + task.description);

                let updateButton = $('<button>')
                    .text('Update')
                    .click(function () {
                        updateTask(task.id);
                    });

                let deleteButton = $('<button>')
                    .text('Delete')
                    .click(function () {
                        deleteTask(task.id);
                    });

                listItem.append(' '); // Space between buttons
                listItem.append(updateButton);
                listItem.append(' '); // Space between buttons
                listItem.append(deleteButton);

                taskList.append(listItem);
            });
        },
    });
}

function deleteTask(taskId) {
    $.ajax({
        url: '/tasks/' + taskId,
        type: 'DELETE',
        success: function (data) {
            loadTasks();
        }
    });
}

function updateTask(taskId) {
    let newTitle = prompt("Enter new title: ");
    let newDescription = prompt("Enter new description: ");

    if (newTitle == null || newDescription == null) {
        return;
    }

    $.ajax({
        url: '/tasks/' + taskId,
        type: 'PUT',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ title: newTitle, description: newDescription }),
        success: function (data) {
            loadTasks();
        }
    });
}

function addTask() {
    let title = $('#title').val();
    let description = $('#description').val();
    $.ajax({
        url: '/tasks',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ title: title, description: description }),
        success: function (data) {
            loadTasks();
        }
    });
}

$(document).ready(function () {
    loadTasks();
});

