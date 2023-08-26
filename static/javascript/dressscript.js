function selectCharacter(character) {
  // Assuming you have an element with the ID "characterDisplay" on index.html
  const characterDisplay = document.getElementById('characterDisplay');

  if (character === 'character1') {
      characterDisplay.innerHTML = '<img src="character1.png" alt="Character 1">';
  } else if (character === 'character2') {
      characterDisplay.innerHTML = '<img src="character2.png" alt="Character 2">';
  }
}