const form = document.getElementById("predictionForm");

form.addEventListener("submit", function () {

    const button = document.querySelector(".predict-btn");

    button.innerText = "Predicting...";
    button.disabled = true;

});