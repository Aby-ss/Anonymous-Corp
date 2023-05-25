document.addEventListener("DOMContentLoaded", function() {
    var button = document.createElement("button");
    button.innerHTML = "Click Me";
    button.style.fontSize = "24px";
    button.style.padding = "50px 100px";
    button.style.borderRadius = "6px";
    button.addEventListener("click", function() {
      console.log("Button clicked!");
    });
    document.getElementById("button-container").appendChild(button);
  });