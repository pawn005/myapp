const container = document.getElementById("buttonContainer");

buttons.forEach(function (btn) {
  const b = document.createElement("button");
  b.id = btn.id;
  b.textContent = btn.id.replace("btn", "").padStart(3, "0");
  b.className = "btn";
  b.addEventListener("click", function () {
    window.location.href = btn.url;
  });
  container.appendChild(b);
});
