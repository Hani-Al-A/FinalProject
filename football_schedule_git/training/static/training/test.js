document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#fetchTeamsBtn').addEventListener('click', function() {
        const competitionId = document.querySelector('#competition').value.split(',')[0];
        const competition_name= document.querySelector('#competition').value.split(',')[1];;

        if (competitionId) {
            window.location.href = `/test/get_teams/${competitionId}/${competition_name}`;

        } else {
            alert('Please select a competition first.');
        }
    })

    document.querySelector('#back_to_comp_select').addEventListener('click', function() {
        window.location.href = `/test`;
 
    });
});
