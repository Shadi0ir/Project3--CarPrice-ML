$(document).ready(function() {
    var make_models_obj;
    
    function createYearOptions(yearList){
       var yearSelectElm = document.getElementById('years');
       for (var i=0; i<yearList.length; i++){
            var newOption = document.createElement("option");
            newOption.text = yearList[i]
            newOption.value = yearList[i]
            yearSelectElm.appendChild(newOption);
       }    
    }
    function createMakeOptions(){
        var makeSelectElm = document.getElementById('makes');
        Object.keys(make_models_obj).forEach(function(key,index) {
            var newOption = document.createElement("option");
            newOption.text = key
            newOption.value = key
            makeSelectElm.appendChild(newOption);
        });   
    }
    function createModelOptions(make){
        var modelSelectElm = document.getElementById('models');
        $('#models').empty();
        var modelList = make_models_obj[make];
        if(modelList){
            for (var i=0; i<modelList.length; i++){
                var newOption = document.createElement("option");
                newOption.text = modelList[i]
                newOption.value = modelList[i]
                modelSelectElm.appendChild(newOption);
           } 
        }
        else{
            var newOption = document.createElement("option");
            newOption.text = "Please select a car make ";
            newOption.value = "Please select a car make ";
            modelSelectElm.appendChild(newOption);
        }
          
        
    }
    function createStateOptions(stateList){
        var stateSelectElm = document.getElementById('states');
        for (var i=0; i<stateList.length; i++){
             var newOption = document.createElement("option");
             newOption.text = stateList[i]
             newOption.value = stateList[i]
             stateSelectElm.appendChild(newOption);
        }   
        
    }
    
    function fetchOPtions(){
        $.ajax({
            url: 'get_options',
            dataType: 'json',
            success: function (data) {
                createYearOptions(data['years']);
                make_models_obj = data['makes']
                createMakeOptions();
                createStateOptions(data['states']);
                $('.loader').hide();
            }
          });
    }
    fetchOPtions();


    $('#makes').on('change', function() {
        createModelOptions(this.value);
    });

    $(document).on("click", "#submit" , function(e) {
        e.preventDefault();
        $('#submit').hide();
        $('#disabled_button').show();
    
        // submit form via AJAX
        $.ajax({
            url: '/',
            data: $('#prediction_form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var msg = ""
                $('#predicted_value').text(response.prediction);
                $('#submit').show();
                $('#disabled_button').hide();
            },
            error: function(error) {
                console.log(error);
                $('#submit').show();
                $('#disabled_button').hide();
            }
        });


    });

});