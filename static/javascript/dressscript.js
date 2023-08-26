const recentClothing = localStorage.getItem("currentClothing");
    const characterClothing = document.getElementById("character_clothing");

    if (recentClothing) {
      characterClothing.src = recentClothing;
    } else {
      characterClothing.src = "images/default_girl.png";
    }

function change_dress(clothing) {
    const character_clothing = document.getElementById("character_clothing");
    character_clothing.src = clothing;
    localStorage.setItem("currentClothing", clothing);
}
  