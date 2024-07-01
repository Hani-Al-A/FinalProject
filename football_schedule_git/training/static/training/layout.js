document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('.menuButton').addEventListener('click', () =>{
        document.querySelector('.menu').classList.toggle('open')

    });

    document.addEventListener('click', event =>{
        const element = event.target;
        console.log(element);
 
    })
    if(document.querySelector('.message')){
        setTimeout(delete_message, 5000)
    }
    setTimeout(document.querySelector(".thin_container").classList.add('body-fade-in'), 1000);



    
});

function delete_message(){
    let div = document.querySelector('.message_container');
        div.style.animationPlayState = 'running';
        div.addEventListener('animationend', () =>{
            div.remove()
        })
}