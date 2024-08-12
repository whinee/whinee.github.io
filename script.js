colors = {
    "github": "110, 84, 148",
    "twitter": "29, 161, 242",
    "anilist": "18, 39, 94",
    "discord": "95, 125, 201",
    "reddit": "252, 5, 5",
}

window.onload = function () {
    var str = ""

    Object.entries(colors).forEach(function ([k, v]) {
        str = str.concat(`#icons01 .${k} button:hover {
            background-color: rgb(${v}) !important;
            -webkit-box-shadow: 0px 15px 20px rgba(${v}, 0.4);
            box-shadow: 0px 15px 20px rgba(${v}, 0.4);
        }`)
    });
    const style = document.querySelector("#style");
    console.log(str);
    style.innerHTML = str;
}
