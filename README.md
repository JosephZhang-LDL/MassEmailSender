# Automated Customized Mass Emailer

Before you run this program, make sure you have python3 installed on your machine. Otherwise, the program won't work. Once you have installed python3, run the command:

	pip install openpyxl

This library is crucial for you to be able to run this program.

_ON THE FLIP SIDE_, if you are comfortable running a virtual environment on your computer, all you have to do is enter the command below:

	. venv/bin/activate

and you will be ready to run the program. To exit the venv, use the command `ctrl-d`.

## Introduction

As of right now, this program is really simple, and mostly used for easy-use cases. That is, you should only use it when you need to concatenate a custom subject to your subject line, add _one_ custom message within the body, and sign off with your name only. If you need to add attachments, that functionality is included as well.

## Basic Components You to Use

*message.txt*: This file is where you write your custom email message. The format should be as follows.

> Custom Greeting {},
> 
> Any text that you wish to appear. When you need to add your custom message, use the {} tag.
> 
> Custom closing,
> {}

That is it. Nothing more, and nothing less. Later, more functionality will be added for custom fields.

*attachment file*: This file an be anything you want. Just make sure it is in the same folder/directory that you downloaded everything else in. This way, when the terminal prompt asks you for the name of your attachment, you do NOT need to write the complete file path. Instead, all you will have to do is write the name of the file and the program will attach it for you.

*sender.py*: This contains the complete script for sending the emails. Don't touch it.

## Instructions for Use

Before you do anything with the program, access the xslx spreadsheet included in the downloaded folder. This part is crucial. Each column serves a purpose, and you will need to fill them out carefully or else there will be potential problems when executing the program.

| Name                   | Email              | Subject Ending                                                     | Custom Message                  |
|------------------------|--------------------|--------------------------------------------------------------------|---------------------------------|
| The Name of the sendee | The Sendee's email | Something custom you want to attach to the end of the subject line | The custom message you will use |

DO NOT USE HEADERS. Just follow the table. Column A is the name, Column B is the email, Column C is the Subject, Column D is the custom message. If you follow this format, you will not have any problems with completing the emails.

Once you have completed the excel sheet to your satsifaction, go to [this link](https://myaccount.google.com/lesssecureapps) and turn on access to less secure apps. The python app is by no means less secure, but it will not be able to run unless you perform this action.

Now, run the program on your computer using either:

	python sender.py

or

	python3 sender.py

Once the program is running, it will ask you for several fields. If you have not completed the message text file or chosen your attachment yet, please do so now or exit from the program using `ctrl-c`. You will see a username field pop up. Now your job is to fill in the following fields:

* Username (Gmail username)
* Password (Your password. The terminal window will NOT show the password as you type it)
* Subject (The first portion of the subject line you will use)
* Add attachment (Type "y" if you plan on adding an attachment and use the full filename)
* Your name (For the signature at the bottom of the email)

Once you have filled in all of this info, the emails will begin to send, and you will be able to see on your terminal a confirmation once each email is sent.
