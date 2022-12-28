let signup_btn = document.getElementById("signup");
let login_btn = document.getElementById("login");
let signup_div = document.getElementById("signupDiv");
let login_div = document.getElementById("loginDiv");
let signup_toggle = document.getElementById("signup-toggle")
let login_toggle = document.getElementById("login-toggle")
let signupDivDisplay = false;
let loginDivDisplay = true

signup_btn.addEventListener('click', () => {
    handleSignupDisplay()
})

login_btn.addEventListener('click', () => {
    handleLoginDisplay()
})

signup_toggle.addEventListener('click', () => {
    handleSignupDisplay()
})

login_toggle.addEventListener('click', () => {
    handleLoginDisplay()
})

const handleSignupDisplay = () => {
    if (!signupDivDisplay) {
        signup_div.style.display = "block";
        login_div.style.display = "none";
        signupDivDisplay = true
        loginDivDisplay = false
    }    
}

const handleLoginDisplay = () => {
    if(!loginDivDisplay) {
        login_div.style.display = "block";
        signup_div.style.display = "none";
        loginDivDisplay = true
        signupDivDisplay = false
    }
}