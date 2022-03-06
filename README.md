<div align="center">

![logo](https://github.com/renataberoli/bug_catcher/blob/dev/app/static/img/bc-logo.png?raw=true)

[Getting started](#getting-started) •
[About the project](#about-the-project)  •
[Installation](#installation) •
[Roadmap](#roadmap) •
[Test cases](#test-cases) •
[Contact](#contact)
</div>

## Getting started
![Gif home](https://github.com/renataberoli/bug_catcher/blob/dev/app/static/img/gif%20principal.gif?raw=true)

### Try a live Demo

###### user
```sh
renataberoli
```
###### password
```sh
123and4
```
<br>

### About the project
This project is a Pet-project that I created to learn more about the Django framework. Bug catcher is an issue tracker 
that aims to simplicity and be useful for small teams that use or not agile methodologies.

#### Sketch
The sketch is the most basic structure I design in the project. Therefore, it's an excellent opportunity to put the ideas 
on the paper and start some initial tests. Also, working as a developer, I use the sketch to understand the information 
architecture and draw the models I need to create for my system.

![Sketch](https://github.com/renataberoli/bug_catcher/blob/dev/app/static/img/sketchs.png?raw=true)

#### ERD (Entity Relationship Diagram)


#### The solution
After sketching the interfaces and the system architecture, I went to the code to translate my sketch into an interface with Bootstrap patterns.

![Desktop](https://github.com/renataberoli/bug_catcher/blob/dev/app/static/img/bug%20catcher%20desktop%20mock.png?raw=true)

#### Layout responsive
My main idea for the project is a desktop system, but I was careful to keep all the interfaces responsible, as most of the web accesses are from mobile devices.

![Mobile](https://github.com/renataberoli/bug_catcher/blob/dev/app/static/img/mobile%20mock%20bc.png?raw=true)

#### Tech stack
![Django Version](https://img.shields.io/badge/Django-~3.2.10-blueviolet)
![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5-blue)
![HTML](https://img.shields.io/badge/HTML-5-red)
![CSS](https://img.shields.io/badge/CSS-3-yellow)
![Pytest Version](https://img.shields.io/badge/Pytest-idn-green)

<br>

## Installation

### Step 1
- Clone this repository
```sh
$ git clone https://github.com/renataberoli/bug_catcher.git
```

### Step 2
- Create a virtual environment
```sh
$ python3 -m venv myvenv
```
** Linux and macOS
<details>
<summary>Windows</summary>

If you are using a virtualenv on Windows, run the fallen command:

```sh
$ python -m venv myvenv
```
</details>

### Step 3
- Install the requirements
````sh
$ pip install -f requirements.txt
````

<details>
<summary>Installing pip</summary>

If you don't have the 'pip' package installed, run the fallen command:

```sh
$ python -m pip install --upgrade pip
```
In this way you'll get the most updated version of the 'pip' package.

**This command is compatible with Linux, macOS and Windows
</details>

### Step 4
- Create a superuser
```sh
$ python manage.py createsuperuser
```

<br>

## Test cases
### Scenario 1
###### test_search_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|This test aims to check if the search field works as expected.|Use: “error” as the search argument.|The system will return only issues with “error” in some parts of the title.|

<details>
<summary>Scenario 1 - script</summary>

```sh
$
```
</details>

### Scenario 2
###### test_priority_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the priority field works as expected.|Use: “low” as the field’s option.|The system will return only issues with “low” priority.|
<details>
<summary>Scenario 2 - script</summary>

```sh
$
```
</details>

### Scenario 3
###### test_status_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the status field works as expected.|Use: “closed” as the field’s option.|The system will return only issues with the status “closed”.|
<details>
<summary>Scenario 3 - script</summary>

```sh
$
```
</details>

### Scenario 4
###### test_label_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the label field works as expected.|Use: “back-end” as the field’s option.|The system will return only issues with the label “back-end”.|
<details>
<summary>Scenario 3 - script</summary>

```sh
$
```
</details>

### Scenario 5
###### test_assigned_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the assigned field works as expected.|Use: “voorloopnul” as the field’s option.|The system will return only issues assigned to “voorloopnul”.|
<details>
<summary>Scenario 3 - script</summary>

```sh
$
```
</details>

### Scenario 6
###### test_all_filters_together
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if all the list filters work together as expected.|Use: search argument - “error”; priority - “high”; status - “open”; label - “front-end”; assigned - “voorloopnul”.|The system will show only the issue that matches all the filter's arguments.|
<details>
<summary>Scenario 3 - script</summary>

```sh
$
```
</details>

### Scenario 7
###### test_login_success
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the user will be redirected to the main page if the successful login.|Use: user - “renataberoli”; password - “123and4”.|The user will be redirected to the “list of issues” page..|
<details>
<summary>Scenario 3 - script</summary>

```sh
$
```
</details>
<br>

## Roadmap
- [x] Create the basic structure of the system (CRUD - create, read, update and delete).
- [x] Create a place where the issues will be listed to the user.
- [x] Add a pagination for this list of issues. 
- [x] Create a series of list filters to help the user find what he wants.
- [x] Create a login and authentication flow.
- [x] Improve the UI to meet the mockups design before.
- [x] Improve the software's documentation.
- [x] Write some basic tests to make sure that the system is working as expected.

<br>

<div align="center">

## Contact
[LinkedIn](https://www.linkedin.com/) •
[Portfolio](https://renataberoli.github.io/) •
[Twitter](https://twitter.com/renataberoli) 

</div>