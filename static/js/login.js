let nome= String(document.getElementById('nome'))
let pass=String(document.getElementById('pass'))
let user={'nome_utente': nome, 'password': pass}

function Login(){
    fetch('https://3246-andreagri-flasklogin-frtz8zkrvb6.ws-eu113.gitpod.io/csv',{
        method: 'POST',
        headers :  {
            'Content-Type': 'aplication/json'
        },
        body: JSON.stringify(user)
    })
    .then{
        data=>
    }
    













}


