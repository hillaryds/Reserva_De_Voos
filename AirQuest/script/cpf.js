const inputCpf = document.getElementById("input-cpf");

inputCpf.addEventListener("keypress", () => {
//   if (isNaN(inputCpf.value)) {
//     inputCpf.preventDefault();
//   }
  if (inputCpf.value.length == 3 || inputCpf.value.length == 7) {
    inputCpf.value += ".";
  } else if (inputCpf.value.length == 11) {
    inputCpf.value += "-";
  }
});
