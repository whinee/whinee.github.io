window.onload = function () {
    console.log(document.referrer);
    const style = document.querySelector("#gb");
    if (document.referrer) {
        style.innerHTML = `<a id="more-btn" href="${document.referrer}"><button class="rnd-btn">GO BACK</button></a>`;
    }
}