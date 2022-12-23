


var inputText = '[1, "dLark", "4567"]'
var arr =[];

async function getData(inputText){
    return fetch(`http://127.0.0.1:5000/loginData/${inputText}`)
        .then((response)=>response.text())
        .then((data)=>{return processResults(data)});
}

async function testFunc(){
    if (inputText != ""){
        arr = await getData(inputText);
        console.log(arr);
    }
}

function processResults(data){
    data = JSON.parse(data)
    return data
}


testFunc()

