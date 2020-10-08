    function renderButton() {
        gapi.signin2.render('g-signin2', {
            'scope': 'profile email',
            'width': 250,
            'height': 40,
            'longtitle': true,
            'theme': 'dark',
            'onsuccess': onSignIn,
            'onfailure': onFailure
        });
    }
    function onSignIn(googleUser) {
        var profile = googleUser.getBasicProfile();
        // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
        // console.log('Name: ' + profile.getName());
        // console.log('Image URL: ' + profile.getImageUrl());
        // console.log('Email: ' + profile.getEmail());
        var googleTockenId = profile.getId();
        var Firstname = profile.getGivenName();
        var Lastname = profile.getFamilyName();
        
        var email = profile.getEmail();
        var profile = profile.getImageUrl();
        $("#loaderIcon").show('fast');
        $("#g-signin2").hide('fast');
        saveUserData(googleTockenId,Firstname,Lastname,email,profile); // save data to our database for reference
    }
    // Sign-in failure callback
    function onFailure(error) {
        alert(error);
    }
    // Sign out the user
    function signOut() {
        if(confirm("Are you sure to signout?")){
            var auth2 = gapi.auth2.getAuthInstance();
            auth2.signOut().then(function () {
                $("#loginDetails").hide();
                $("#loaderIcon").hide('fast');
                $("#g-signin2").show('fast');
            });
            auth2.disconnect();
        }
    }
    
    function saveUserData(googleTockenId,Firstname,Lastname,email,profile) {
        $.post("/user/googleSignInSignUpData",{authProvider:"Google",googleTockenId:googleTockenId,Firstname:Firstname,Lastname:Lastname,email:email},
            function (response) {

                // if success redirect to  dashboard

            if (response['success']==true){

                window.location.href='/Dashboard'
            }

            else if (response['success']==false){
                // alert(response.error)
                $('#error').html(response['error']);
            }

            else
            {
                console.log("success")
            }

        });
    }

    