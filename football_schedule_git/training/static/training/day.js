document.addEventListener('DOMContentLoaded', function() {

    

    document.addEventListener('click', event =>{
        const element = event.target;
        if(element.id === 'delete_event'){
            event.preventDefault();

            var form = event.target.parentElement;
            var day = form.getAttribute('data-day');
            var month = form.getAttribute('data-month');
            var year = form.getAttribute('data-year');
            var eventId = form.getAttribute('data-event-id');
        
            var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        
            fetch(`/day_details/${day}/${month}/${year}/delete_event/${eventId}`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    let div = element.parentElement.parentElement.parentElement.parentElement;
                    div.style.animationPlayState = 'running';
                    div.addEventListener('animationend', () =>{
                        div.parentElement.querySelector('hr').remove()
                        div.remove()
                    })
                } else {
                    console.log('Failed to delete event');
                }
            })

        }


    })
    
});

