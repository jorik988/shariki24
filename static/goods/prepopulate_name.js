document.addEventListener("DOMContentLoaded", function() {
    var nameField = document.getElementById("id_name");
    if (nameField && nameField.value === "") {
        nameField.value = "Набор №";  // Здесь укажите значение, которым хотите предзаполнить поле name
    }
});
//Автозаполнение name
