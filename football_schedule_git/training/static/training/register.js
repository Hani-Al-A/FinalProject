document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#job_title').addEventListener('change', () =>{
        const user_is_coach = document.querySelector('#job_title').value;
        if (user_is_coach === 'True'){
            document.querySelector('.coach_field').style.display = "block";
            document.querySelector('.player_field').style.display = "none";
            document.querySelector('.register_details').style.display = "block";

        }
        else if (user_is_coach === 'False'){
            document.querySelector('.player_field').style.display = "block";
            document.querySelector('.coach_field').style.display = "none";
            document.querySelector('.register_details').style.display = "block";
        }
        else{
            document.querySelector('.player_field').style.display = "none";
            document.querySelector('.coach_field').style.display = "none";
            document.querySelector('.register_details').style.display = "none";
        }
    });

});

