var arr =[];

async function getData(inputText){
    return fetch(`http://127.0.0.1:5000/searchRecommendations/${inputText}`)
        .then((response)=>response.text())
        .then((data)=>{return processResults(data)});
}

async function getSuggestions(){
    var inputText = document.getElementById("tickerSearch").value;
    inputText = inputText.toUpperCase()
    console.log(`Input Text = ${inputText}`);
    if (inputText != ""){
        arr = await getData(inputText) 
        
    }
    

}

function processResults(data){

    data = JSON.parse(data)
    let companyNames = [];
    let tickers =[];
    for (var o = 0; o < data.length; o++){
        pairs = data[o]
        tickers.push(pairs[0])
        companyNames.push(pairs[1])
        }
    console.log(`Tickers are: ${tickers.join(", ")} \nCompany Names are: ${companyNames.join(", ")}`)
    return tickers


}

function autocomplete(inp) {
    var currentFocus;
    inp.addEventListener("input", async function(e) {

        await getSuggestions()
        
        var a, b, i, val = this.value;

        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");

        this.parentNode.appendChild(a);
        for (i = 0; i < arr.length; i++) {
            b = document.createElement("DIV");
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
            b.addEventListener("click", function(e) {
                inp.value = this.getElementsByTagName("input")[0].value;
                closeAllLists();
            });
            a.appendChild(b);
        }
    });
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
          currentFocus++;
          addActive(x);
        } else if (e.keyCode == 38) {
          currentFocus--;
          addActive(x);
        } else if (e.keyCode == 13) {
          e.preventDefault();
          if (currentFocus > -1) {
            if (x) x[currentFocus].click();
          }
        }
    });
    function addActive(x) {
      if (!x) return false;
      removeActive(x);
      if (currentFocus >= x.length) currentFocus = 0;
      if (currentFocus < 0) currentFocus = (x.length - 1);
      x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
      for (var i = 0; i < x.length; i++) {
        x[i].classList.remove("autocomplete-active");
      }
    }
    function closeAllLists(elmnt) {
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
          x[i].parentNode.removeChild(x[i]);
        }
      }
    }
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
  }
  
  function getStocks(val) {
  
  return [val+"-Able", "AARG"]
  }
  