const timerDiv = document.querySelector('.timer-div');
const timerElement = document.querySelector('.timer');
const statusElement = document.querySelector('.status');
const pointsSpan = document.getElementById('points');
const pointsChart = new Chart(document.getElementById('pointsChart'), {
      type: 'pie',
      data: {
        labels: ['Current strength', 'Required for next level'],
        datasets: [
          {
            data: [0, 100], // Initial points and remaining value (assuming 100 is the max value)
            backgroundColor: ['#9ea1d4', '#a8d1d1'] // Colors for each segment
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });

    let timerInterval;
    let totalTime = 10; // 10 seconds
    let isTimerRunning = false;
    let points = 0; // Initial points

    function updatePoints() {
      points += 10; // Increase points by 10
      pointsSpan.textContent = points; // Update the points display
      pointsChart.data.datasets[0].data = [points, 100 - points];
      pointsChart.update(); // Update the chart
    }

    function updateTimer() {
      if (totalTime <= 0) {
        clearInterval(timerInterval);
        timerInterval = null;
        timerElement.textContent = '00:00'; // Show 00:00 when timer is done
        statusElement.textContent = 'Timer finished!';
        updatePoints(); // Add points when the timer finishes
        setTimeout(resetTimer, 3000); // Reset the timer after 3 seconds
      } else {
        timerElement.textContent = `00:${String(totalTime).padStart(2, '0')}`;
        totalTime--;
      }
    }

    function resetTimer() {
      timerElement.textContent = '10';
      totalTime = 10;
      statusElement.textContent = 'Click here to start';
      isTimerRunning = false;
      timerDiv.style.backgroundColor = '';
    }

    timerDiv.addEventListener('click', () => {
      if (!isTimerRunning) {
        timerInterval = setInterval(updateTimer, 1000);
        timerDiv.style.backgroundColor = '#c7d7c0';
        statusElement.textContent = 'Click here to pause';
        updateTimer();
      } else {
        clearInterval(timerInterval);
        timerInterval = null;
        timerDiv.style.backgroundColor = '#e4abab';
        statusElement.textContent = 'Click here to resume';
      }

      isTimerRunning = !isTimerRunning;
    });