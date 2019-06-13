function validateForm() {
  var size = document.getElementById("size").value;
  var array = document.getElementById("array").value.split(",");
  // var average = document.getElementById("average").value;

  if (size != array.length) {
    alert("The array must contain exactly " + size + " number(s)");
    return false;
  } else return true;
}
