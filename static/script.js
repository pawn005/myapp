function changeText() {
    const h1 = document.getElementById("main-text");
    if(h1.innerText === "Hello, Flask!!") {
        h1.innerText = "文字が変わりました！！！";
    } else {
        h1.innerText = "Hello, Flask!!";
    }
}
