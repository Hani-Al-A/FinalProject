document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('table').classList.add("table", "table-bordered");

    document.querySelector('#user_time_zone').value = Intl.DateTimeFormat().resolvedOptions().timeZone

    if (document.querySelector('#create_event')){
        
        document.querySelector('#create_event').addEventListener('click', () =>{
            document.querySelector('#create_event').style.display = "none";
            document.querySelector('#view_calendar').style.display = "block";
            document.querySelector('#create_event_form').style.display = "block";
            document.querySelector('.cal').style.display = "none";
            document.querySelector('#sync_button').style.display = "none";
    
        });

        document.querySelector('#view_calendar').addEventListener('click', () =>{
            document.querySelector('#view_calendar').style.display = "none";
            document.querySelector('.cal').style.display = "block";
            document.querySelector('#create_event').style.display = "block";
            document.querySelector('#create_event_form').style.display = "none";
            document.querySelector('#sync_button').style.display = "block";
            
        });
    
    }

    document.querySelector('#next_month').addEventListener('click', () =>{
        var url = window.location.href;
        var urlParts = url.split('/');
        var urlMonth = urlParts[urlParts.length - 2]; // Assuming month is the second last part
        var urlYear = urlParts[urlParts.length - 1];
        var month = parseInt(urlMonth);
        var year = parseInt(urlYear);
        if (month == 12){
            month = 1;
            year++;
        } else{
            month++;
        }
        var newURL = urlParts[0] + "/schedule/" + month + "/" + year;
        window.location.href = newURL;



    });
    document.querySelector('#previous_month').addEventListener('click', () =>{
        var url = window.location.href;
        var urlParts = url.split('/');
        var urlMonth = urlParts[urlParts.length - 2];
        var urlYear = urlParts[urlParts.length - 1];
        var month = parseInt(urlMonth);
        var year = parseInt(urlYear);
        if (month === 1){
            month = 12;
            year--;
        } else{
            month--;
        }
        var newURL = urlParts[0] + "/schedule/" + month + "/" + year;
        window.location.href = newURL;



    });

    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    console.log(timezone)
    if (document.getElementById('timezone')){
        document.getElementById('timezone').value = timezone;
    }
    


});