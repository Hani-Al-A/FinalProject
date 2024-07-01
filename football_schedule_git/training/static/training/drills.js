document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#show_drills').addEventListener('click', () =>{
        document.querySelector('#create_drill').style.display = "block";
        document.querySelector('#show_drills').style.display = "none";
        document.querySelector('.create_drill_form').style.display = "none";
        document.querySelector('#drills_list').style.display = "block";


    });

    document.querySelector('#create_drill').addEventListener('click', () =>{
        document.querySelector('#create_drill').style.display = "none";
        document.querySelector('#show_drills').style.display = "block";
        document.querySelector('.create_drill_form').style.display = "block";
        document.querySelector('#drills_list').style.display = "none";


    });

    document.querySelector('#cancel').addEventListener('click', () =>{
        document.querySelector('#create_drill').style.display = "block";
        document.querySelector('#show_drills').style.display = "none";
        document.querySelector('.create_drill_form').style.display = "none";
        document.querySelector('#drills_list').style.display = "block";


    });

    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    document.getElementById('timezone').value = timezone;
    
});