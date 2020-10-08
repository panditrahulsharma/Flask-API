
$(document).ready(function()
{


function checkForm(FirstName,LastName,password,resetpassword)
  {



    if(FirstName == "") {
      alert("Error: FirstName cannot be blank!");
      // form.username.focus();
       // location.reload()
      return false;

    }
    // re = /^\w/;
    var re = /^[a-zA-Z]*$/; // allow letters, numbers, and underscore
    var reWhiteSpace = new RegExp("\\s+");

    if(!re.test(FirstName)) {
      alert("Error: FirstName must contain only letters,Not numbers and Special characters!");
      // form.username.focus();
      return false;
    }


    if(!isNaN(FirstName))
    {
    alert("Please Enter Only Characters");
    // document.form.name.select();
    return false;
    }


    if ((FirstName.length > 20))
    {
    alert("FirstName must be Less 20 Character");
    // document.form.name.select();
    return false;
    }



// for Lastname
    if(LastName == "") {
      alert("Error: LastName cannot be blank!");
      form.username.focus();
       // location.reload()
      return false;

    }
    // re = /^\w/;
    var re = /^[a-zA-Z]*$/; // allow letters, numbers, and underscore
    var reWhiteSpace = new RegExp("\\s+");

    if(!re.test(LastName)) {
      alert("Error: LastName must contain only letters,Not numbers and Special characters!");
      // form.username.focus();
      return false;
    }


    if(!isNaN(LastName))
    {
    alert("Please Enter Only Characters");
    // document.form.name.select();
    return false;
    }


    if ((LastName.length > 20))
    {
    alert("LastName must be Less 20 Character");
    // document.form.name.select();
    return false;
    }

// end of last name



    if(password != "" && password == resetpassword) {



      if((password.length < 6) || (password.length > 30)) {
        alert("Error: Password must contain at least six and maximum 30 characters!");
        // form.pwd1.focus();
        return false;
      }

      if(password == FirstName) {
        alert("Error: Password must be different from Username!");
        // form.pwd1.focus();
        return false;
      }
      re = /[0-9]/;
      if(!re.test(password)) {
        alert("Error: password must contain 1 special character 1 number 1 lowercase 1 uppercase and min 6 length Kindly Check Your Entered password");
        // form.pwd1.focus();
        return false;
      }
      re = /[a-z]/;
      if(!re.test(password)) {
        alert("Error: password must contain 1 special character 1 number 1 lowercase 1 uppercase and min 6 length Kindly Check Your Entered password");
        // form.pwd1.focus();
        return false;
      }
      re = /[A-Z]/;
      if(!re.test(password)) {
        alert("Error: password must contain 1 special character 1 number 1 lowercase 1 uppercase and min 6 length Kindly Check Your Entered password");
        // form.pwd1.focus();
        return false;
      }

      var SpecialChar=/[\!\@\#\$\%\^\&\*\)\(\+\=\.\<\>\{\}\[\]\:\;\'\"\|\~\`\-]/g

      if(!SpecialChar.test(password)) {
        alert("Error: password must contain 1 special character 1 number 1 lowercase 1 uppercase and min 6 length Kindly Check Your Entered password");
        // form.pwd1.focus();
        return false;
      }


      if (reWhiteSpace.test(password)) {
          alert("Please Check Your Fields For Spaces");
          // form.pwd1.focus();
          return false;
      }


    } 
    
    else {
      alert("Error: Please check that you've entered and confirmed your password!");
      // form.pwd1.focus();
      return false;
    }

    // alert("You entered a valid password: " + password);
    return true;
  }




function resetpasswordForm(password,resetpassword)
  {
    var re = /^[a-zA-Z]*$/; // allow letters, numbers, and underscore
    var reWhiteSpace = new RegExp("\\s+");
    if(password != "" && password == resetpassword) {
        if((password.length < 6) || (password.length > 30)) {
          alert("Error: Password must contain at least six and maximum 30 characters!");
          // form.pwd1.focus();
          return false;
        }

        re = /[0-9]/;
        if(!re.test(password)) {
          alert("Error: password must contain at least one number (0-9)!");
          // form.pwd1.focus();
          return false;
        }
        re = /[a-z]/;
        if(!re.test(password)) {
          alert("Error: password must contain at least one lowercase letter (a-z)!");
          // form.pwd1.focus();
          return false;
        }
        re = /[A-Z]/;
        if(!re.test(password)) {
          alert("Error: password must contain at least one uppercase letter (A-Z)!");
          // form.pwd1.focus();
          return false;
        }

        var SpecialChar=/[\!\@\#\$\%\^\&\*\)\(\+\=\.\<\>\{\}\[\]\:\;\'\"\|\~\`\-]/g

        if(!SpecialChar.test(password)) {
          alert("Error: password must contain at least one SpecialChar");
          // form.pwd1.focus();
          return false;
        }


        if (reWhiteSpace.test(password)) {
            alert("Please Check Your Fields For Spaces");
            // form.pwd1.focus();
            return false;
        }


      } 
      
      else {
        alert("Error: Please check that you've entered and confirmed your password!");
        // form.pwd1.focus();
        return false;
      }

      // alert("You entered a valid password: " + password);
      return true;
  }


function ValidateEmail(mail){

	// https://flaviocopes.com/how-to-validate-email-address-javascript/
	// https://www.codespot.org/javascript-email-validation/

	// email valid or not link
	// http://softwaretesterfriend.com/manual-testing/valid-invalid-email-address-format-validation/

	var email = mail;
	const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	if(email.match(re))
	{
	// document.form1.text1.focus();
	return true;
	}

	if(email.length > 320)
	{
		alert("You Exceed length of Email Should be Less 320 charactor");
	// document.form1.text1.focus();
	return False;
	}

	else
	{
	alert("Your email is invalid!");
	// document.form1.text1.focus();
	return false;
	}

}






$('#sign-up').submit(function(e){
	e.preventDefault();
	const Type = $('#Type').val();
	const email = $('#email').val();
	const FirstName = $('#fname').val();
	const LastName = $('#lname').val();
	const password = $('#password').val();
	const resetpassword = $('#resetpassword').val();


	if(!ValidateEmail(email)){
		// alert("You have entered an invalid email address!");
		return false;
	}


	if(!checkForm(FirstName,LastName,password,resetpassword)){
		return false;
	}



	let data = {Type:Type,FirstName:FirstName,LastName:LastName,email:email,password:password,captcha: grecaptcha.getResponse()}

    $('#loadingmessage').show();
    $('#alert').hide();

	// $('#loadingmessage').show();

	$.ajax({
		url:"/user/register",
		type:'post',
		data:data
	})
		.done(function( data )
		 {
			$('#loadingmessage').hide();
			if ( data.success )
			{
				//let obj = {'email':email,'name':data.name,'password':password}
				// localStorage.setItem('auth',JSON.stringify(obj));
				window.location.href='/thanks'

			}
			else
			{

        $('#alert').show();
        $('#error').html(data.error);
        
			}
		});
});



$('#login-form').submit(function(e){
	e.preventDefault();
	const email = $('#email').val();
	const password = $('#password').val();
  const checkBox=localStorage.chkbx;

	// alert(checkBox)

	if(!email || !password){
		alert('Fill all fields!')
	}
	if(!ValidateEmail(email)){
		alert("You have entered an invalid email address!");
		return false;
	}
	// $('#loadingmessage').show();


    $('#loadingmessage').show();
    $('#alert').hide();

	// returns true if the variable does NOT contain a valid number)
	let data = { email:email, password:password,checkBox:checkBox}

	console.log(data)

	$.ajax({
		url:"/user/login",
		type:'post',
		data:data

	})
		.done(function( data )
		{
			$('#loadingmessage').hide();
			if ( data.success ) {
				let obj = {'email':email,'name':data.name,'password':password}//here also return id of user
				window.location.href='/Dashboard'
			}
			else
			{
        // $('#loadingmessage').hide();
        $('#alert').show();
				$('#error').html(data.error);
			}
		});
});



$('#ForgotPassword').submit(function(e){
	e.preventDefault();
	const email = $('#Email').val();
	
	//alert("login form")
	if(!email){
		alert('Fill all fields!')
	}
	if(!ValidateEmail(email)){
		alert("You have entered an invalid email address!");
		return false;
	}
	let data = { email:email}

	console.log(data)

    $('#loadingmessage').show();
    $('#alerterror').hide();
    $('#alertmsg').hide();

	// $('#msg').html("Please Wait ..");

	$.ajax({
		url:"/CheckForgotPasswordAccount",
		type:'post',
		data:data

	})
		.done(function( data )
		{
			$('#loadingmessage').hide();
			if ( data.success ) {
				// let obj = {'email':email,'name':data.name,'password':password}//here also return id of user
				// window.location.href='/Dashboard'
      $('#alertmsg').show();

				$('#msg').html(data.msg);
			}
			else
			{
				// $('#msg').hide()
         $('#alerterror').show();
				$('#error').html(data.error);
			}
		});
});




// reset password 



$('#resetPassword').submit(function(e){
  e.preventDefault();

  const UserId = $('#UserId').val();
  const NewPassword = $('#NewPassword').val();
  const NewPassword1 = $('#NewPassword1').val();
  
// here write password check using resetpasswordForm function 

  if(!resetpasswordForm(NewPassword,NewPassword1)){
    return false;
  }

  let data = { UserId:UserId,NewPassword:NewPassword,NewPassword1:NewPassword1}

  console.log(data)

  $.ajax({
    url:"/updatePassword",
    type:'post',
    data:data

  })
    .done(function( data )
    {
      // $('#loadingmessage').hide();
      if ( data.success ) {
        // let obj = {'email':email,'name':data.name,'password':password}//here also return id of user
        window.location.href='/Dashboard'
        // $('#msg').html(data.msg);
      }
      else
      {
        $('#error').html(data.error);
      }
    });
});

// end of resetpassword


    $(document).ready(function (e) {
      $('#upload').on('click', function () {
        var form_data = new FormData();
        var ins = document.getElementById('file-upload').files.length;
        
        if(ins == 0) {
          $('#msg').html('<span style="color:red">Select at least one file</span>');
          return;
        }
        
        for (var x = 0; x < ins; x++) {
          form_data.append("files[]", document.getElementById('file-upload').files[x]);
        }
        
        $.ajax({
          url: '/user/profile/update/profilePic/', // point to server-side URL
          dataType: 'json', // what to expect back from server
          cache: false,
          contentType: false,
          processData: false,
          data: form_data,
          type: 'post',
          success: function (response) { // display success response
            $('#msg').html('');
            $.each(response, function (key, data) {             
              if(key !== 'message') {
                $('#msg').append(key + ' -> ' + data + '<br/>');
              } else {
                $('#msg').append(data + '<br/>');
              }
            })
          },
          error: function (response) {
            $('#msg').html(response.message); // display error response
          }
        });
      });
    });
  





});