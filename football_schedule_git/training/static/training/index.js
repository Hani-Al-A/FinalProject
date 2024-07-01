document.addEventListener('DOMContentLoaded', function() {
    const today = new Date();
    const day = today.getDate();

    console.log(day);
    document.querySelector('.this_week').querySelectorAll('tr').forEach( (row) =>{
        if (row.querySelectorAll('td')){
            row.querySelectorAll('td').forEach( (cell) => {
                if (cell.querySelector('div')){
                    let event_day_cell = cell.querySelector('div').querySelector('a');
                    if (cell.innerHTML === `${day}` || event_day_cell.innerHTML === `${day}`){
                        cell.setAttribute("id", 'current_day');                        
                    }
                } else{
                    if (cell.innerHTML === `${day}`){
                        cell.setAttribute("id", 'current_day');
                    }
                }
                
                
            })
        }
    })

});