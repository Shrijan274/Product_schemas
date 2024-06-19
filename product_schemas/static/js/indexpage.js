function showLoginForm() {
  document.getElementById("login-form").style.display = "block";
  document.getElementById("signup-form-container").style.display = "none";
  document.getElementById("forgot-password-form").style.display = "none";
}

function showSignupForm() {
  document.getElementById("login-form").style.display = "none";
  document.getElementById("signup-form-container").style.display = "block";
  document.getElementById("forgot-password-form").style.display = "none";
}

function showForgotPasswordForm() {
  document.getElementById("login-form").style.display = "none";
  document.getElementById("signup-form-container").style.display = "none";
  document.getElementById("forgot-password-form").style.display = "block";
}

// Add event listeners to the password fields for keyup event
document.getElementById('password').addEventListener('keyup', validatePasswords);
document.getElementById('confirmPassword').addEventListener('keyup', validatePasswords);

function validatePasswords() {
    var password1 = document.getElementById('password').value;
    var password2 = document.getElementById('confirmPassword').value;
    var submitButton = document.getElementById('submit-button');

    if (password1 !== password2 || password1 === '' || password2 === '') {
        submitButton.disabled = true; // Disable the submit button if passwords do not match or either field is empty
    } else {
        submitButton.disabled = false; // Enable the submit button if passwords match
    }
}

  
// using jQuery,AJAX to handle submission in signup
$(document).on('submit','#signup-form',function(e){
  e.preventDefault()

  $.ajax({
    type:'POST',
    url:'/signup/',
    data:{
      email:$('#email').val(),
      firstname:$('#firstname').val(),
      lastname:$('#lastname').val(), 
      password:$('#password').val(),
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
    },
      success:function(data){
        alert(data);
        location.reload();
    }
  });
}); 

// using jQuery,AJAX to handle submission in logging
$(document).on('submit','#login-form',function(e){
  e.preventDefault()

    $.ajax({
      type: 'GET',
      url: '/logging/', // Point to the logging view URL
      data: {
        email: $('#email').val(),
        password: $('#password').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
    }).done(function(r){
      console.log(r);
      alert(r.message);
    });;
});

// using jQuery,AJAX to handle submission in forgotpw
$(document).on('submit','#newpassword-form',function(e){
  e.preventDefault()
    $.ajax({
      url: '/resetpassword/' + $('#email').val(),
      type: 'POST',
      data: {
        email: $('#email').val(),
        password: $('#password').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data) {
        alert(data);
        location.reload();
      },
    });
})

