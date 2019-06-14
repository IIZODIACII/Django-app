function validateForm() {
  // var size = document.getElementById("size").value;
  var array = document.getElementById("array").value.split(",");
  // var average = document.getElementById("average").value;

  var valid = true;
  array.forEach(element => {
    if (element == parseInt(element, 10) && valid) {
      valid = true;
    } else {
      valid = false;
    }
  });

  if (!valid) {
    alert("all the numbers must be integers in the array");
    return false;
  } else return true;
}
