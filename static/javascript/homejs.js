
const recentClothing = localStorage.getItem("currentClothing");

if (recentClothing) {
  const characterClothing = document.getElementById("character_clothing");
  characterClothing.src = recentClothing;
} else {
  const defaultClothing = "/procatstination/static/images/girl/girl/default_girl.png"; 
  const characterClothing = document.getElementById("character_clothing");
  characterClothing.src = defaultClothing;
}
