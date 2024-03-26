# python-selenium-automation
This code automates creating a new post on a website (atg.party).
First of all Importsing necessary Libraries for controlling a web browser (selenium), sending keyboard inputs (pynput), logging messages (logging) and making web requests (requests) are imported.
Logging Setup It configures logging to record information about the script's execution.
Browser Setup It launches a Chrome browser controlled by the script.

Load Page & Measure Time It opens the website and measures how long it takes for the page to load.

Check Response Code It checks if the website responded successfully (code 200) or with an error (code 400).

Login (if successful response):

Clicks a login button.
Waits for email and password fields to be visible and enters credentials.
Clicks login button again.
Create New Post (if logged in):

Opens the "article" creation page.
Fills in title and description for the new post.
Clicks the button to add a cover image.
Simulates typing the image file path using the keyboard.
Clicks a button to publish the post.
Records the URL of the newly created post.

Error Handling: If the website responds with an error code, it logs an error message.

Close Browser: It closes the browser window.
