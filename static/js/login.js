let nome= String(document.getElementById('nome'))
let pass=String(document.getElementById('pass'))

fetch('https://3246-andreagri-flasklogin-zemtfifyyso.ws-eu111.gitpod.io/csv')
.then(response => response.json())
    .then(data => {
        console.log(data)})

function Login(){
    

}
