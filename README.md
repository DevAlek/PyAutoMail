# PyAutoMail 🐍💌

PyAutoMail is an open source tool created to make it easier to send emails to multiple people. 

# Features 💫
* 🎩 Multiple destinations
* 🔮 Use handy spreadsheets specify destinations and information
* 🧹 Replace specific parts of your documents or message for each indivudal destination
* 🌐 Uses GMail SMTP by default - supports any SMTP servers

# How-to ✂️

1. Create a spreadsheet in the following format, and save it as a TSV file

![image](https://user-images.githubusercontent.com/78972830/135733243-eab52f4c-38a9-449b-8548-70a61e1a162a.png)

![image](https://user-images.githubusercontent.com/78972830/135733262-bfd7ace6-4fd0-43b6-83bd-78230046af4e.png)

2. Load the file in the program

![image](https://user-images.githubusercontent.com/78972830/135733067-105a3bba-53a0-4d42-abc2-3c687b236a0f.png)

Done!

As you can see in the above example image, you can set text that varies depending on the destination, by including the column name in curly brackets (`{}`).

You can have a look at the TSV file and keywords by checking the `Show tool section` box and clicking `Check TSV Slots`.

![image](https://user-images.githubusercontent.com/78972830/135733439-27c00251-8b26-439c-baf4-d9d5b0c5abaa.png)

You can also check if the keywords are being replaced properly by clicking "Check Replace Output"

![image](https://user-images.githubusercontent.com/78972830/135733532-3f564cad-5ad1-4c93-ae8c-ac701408405a.png)
