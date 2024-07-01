document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#selectAll').addEventListener('click', () =>{
        document.querySelectorAll('.select').forEach((option) => {
            option.selected = "true"
        });
        


    });

    document.querySelector('#deselectAll').addEventListener('click', () =>{
        document.querySelectorAll('.select').forEach((option) => {
            option.selected = ""
        });



    });
    
});