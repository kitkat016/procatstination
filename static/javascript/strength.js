window.onload = function() {
    const selectedGender = localStorage.getItem('selectedGender');
    const workoutCharacter = document.getElementById('workoutCharacter');

    if (selectedGender === 'male') {
        workoutCharacter.innerHTML = '<img src=/procatstination/static/images/boy/boy/exercise_boy.png alt="Male Workout Character">';
    } else if (selectedGender === 'female') {
        workoutCharacter.innerHTML = '<img src="femaleWorkoutCharacter.png" alt="Female Workout Character">';
    }
};
