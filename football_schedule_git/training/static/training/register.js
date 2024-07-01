document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#user_time_zone').value = Intl.DateTimeFormat().resolvedOptions().timeZone

    document.querySelectorAll('.must_select').forEach((e) => {
        e.addEventListener('change', () =>{
            const user_is_coach = document.querySelector('#job_title').value;
            const team_selected = document.querySelector('#team').value;
            if (user_is_coach !== 'none' && team_selected !== ""){
                    document.querySelector('.register_details').style.display = "block";

            }
            else{
                    document.querySelector('.register_details').style.display = "none";
            }

        })
    });
    

});

