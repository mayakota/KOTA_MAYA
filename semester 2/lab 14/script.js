    function validate() {
        var x = document.forms.input.username.value;
        var atPos = x.indexOf('@');
        var dotPos = x.lastIndexOf("");

        if(atPos < 1 ||)
            alert("This is not a valid email address!");
    }