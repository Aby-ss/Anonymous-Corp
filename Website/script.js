document.addEventListener("DOMContentLoaded", function() {
    var button = document.createElement("button");
    button.innerHTML = "Click Me";
    button.addEventListener("click", function() {
      console.log("Button clicked!");
    });
    document.getElementById("button-container").appendChild(button);
  });