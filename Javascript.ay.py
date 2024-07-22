Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1.	// Ask the user for their favorite programming language using prompt
... // and log the response to the console.
... let favoriteLanguage = prompt("What is your favorite programming language?");
... console.log("Your favorite programming language is " + favoriteLanguage);
... 2. // Use prompt to ask the user for their top three skills
... // and store them in an array. Then, log the array to the console.
... let skill1 = prompt("Enter your first skill:");
... let skill2 = prompt("Enter your second skill:");
... let skill3 = prompt("Enter your third skill:");
... let skills = [skill1, skill2, skill3];
... console.log("Your top three skills are: " + skills.join(", "));
... 
... 3. // Use prompt to ask the user for their highest level of education
... // and display a custom message based on their response.
... let education = prompt("What is your highest level of education?");
... console.log("Your highest level of education is " + education + ". That's impressive!");
... 
... // Use prompt to ask the user if they had a good morning.
... // If the response is 'yes', log "Great to hear!"
... // Otherwise, log "Hope the rest of your day goes well!"
... let morning = prompt("Did you have a good morning? (yes/no)");
... if (morning.toLowerCase() === "yes") {
...     console.log("Great to hear!");
... } else {
...     console.log("Hope the rest of your day goes well!");
... }
... 
... 5. // Ask the user for their name using prompt and then
... // display a personalized greeting message.
... let name = prompt("What is your name?");
... console.log("Hello, " + name + "! Nice to meet you.");
... 
