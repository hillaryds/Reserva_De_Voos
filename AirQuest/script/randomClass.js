const buttonSeats = document.querySelectorAll('.button-seat');

function assignRandomClass() {
  const randomClasses = ['background-yellow', 'background-blue', 'background-white'];
  buttonSeats.forEach(buttonSeat => {
    buttonSeat.classList.add(randomClasses[Math.floor(Math.random() * randomClasses.length)]);
  });
}

assignRandomClass();