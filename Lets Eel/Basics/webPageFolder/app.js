function SendDataToPython() {
  // this will call a python function directly from here
  const input = document.getElementById("theFirstInput");
  eel.printFromPython(input.value); // eel.thePythonFunctionToCall
}

async function getDataFromPython() {
  // this will also call another function from python and get returned result
  let returnedValueFromPython = await eel.sendDataToJavaScript()();
  document.getElementById(
    "showDataFromPython"
  ).innerText = returnedValueFromPython;
}

eel.expose(alertThis);

function alertThis(someString) {
  alert(someString);
}

eel.expose(getDataFromSecondInput);

function getDataFromSecondInput() {
  let data = document.getElementById("theSecondInput").value;
  return data;
}
