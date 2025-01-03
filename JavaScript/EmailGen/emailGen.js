//stores numbers for generating random numbers for random string
const email_num = 100
//defines the symbols to use for generating random string
const symbols = ['!', '#', '*', '%', '&', '(', ')']
//get the input field, submit button and print div
const emailInput = document.getElementById("email");

const submitButton = document.getElementById("submit");

const printDiv = document.getElementById("print");

//add an event listener
submitButton.addEventListener('click', () => {
    const userInput = emailInput.value.trim();
    if (userInput === ''){
        document.getElementById('warning').innerHTML = "Enter an email address";
    } else if (!validateEmail(userInput)) {
        document.getElementById('warning').innerHTML = "Invalid Email Address";
    }else{
        const userInput = emailInput.value;
        //generate 10 modified emails
        const modifiedEmails = generateModifiedEmails(userInput);
        //prints modified emails
        displayModifiedEmails(modifiedEmails)
    }
})

//function to validate email.
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

//function to generate 10 new modified email addresses
function generateModifiedEmails(email) {
    const modifiedEmails = [];
    for(let i = 0; i < 10; i++) {
        const [localPart, domain] = email.split("@");
        const randomString = generateRandomString();
        const newEmail = `${localPart}+${randomString}@${domain}`;
        modifiedEmails.push(newEmail);
    }
    return modifiedEmails;
}

//function to generate random string
function generateRandomString() {
    const randomNumber = Math.floor(Math.random() * email_num)
    const randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];
    return randomNumber + randomSymbol;
}
//function to display modified email addresses
function displayModifiedEmails(emails){
    const emailContainer = document.createElement('div');
    emailContainer.innerHTML = '<h2>Modified Email Addresses:</h2>';
    emails.forEach(email => {
        const emailElement = document.createElement('div');
        emailElement.innerHTML = email + '<br>';
        emailContainer.appendChild(emailElement);
    });
    printDiv.innerHTML = ' ';
    printDiv.appendChild(emailContainer);
}
