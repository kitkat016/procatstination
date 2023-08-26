const recentClothing = localStorage.getItem("currentClothing");

if (recentClothing) {
  const characterClothing = document.getElementById("character_clothing");
  characterClothing.src = recentClothing;
} else {
  const defaultClothing = "images/default_boy.png"; 
  const characterClothing = document.getElementById("character_clothing");
  characterClothing.src = defaultClothing;
}