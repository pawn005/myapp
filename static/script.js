document.getElementById("header").addEventListener("click", function () {
  window.location.href = "{{ url_for('index') }}";
});

buttons.forEach(function (btn) {
  document.getElementById(btn.id).addEventListener("click", function () {
    window.location.href = btn.url;
  });
});

document.getElementById("header").addEventListener("click", function () {
  window.location.href = "/"; // HTML 側で固定 URL にする
});

document.getElementById("backBtn").addEventListener("click", function () {
  window.location.href = "/"; // HTML 側で固定 URL にする
});

document.getElementById("backBtn").addEventListener("click", function () {
  window.location.href = "{{ url_for('index') }}";
});
