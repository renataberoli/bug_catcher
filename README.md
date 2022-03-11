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
![Django Version](https://img.shields.io/badge/Django-~4.0.3-blueviolet)
![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5-blue)
![HTML](https://img.shields.io/badge/HTML-5-red)
![CSS](https://img.shields.io/badge/CSS-3-yellow)

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
### Scenario 1 - Login
###### test_login_failed
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the user can access the system if the login is failed. |Use: username - “beroli”; password - “1234”|The system will return an error asking the user to enter a correct username.|

<details>
<summary>Code - test_login_failed</summary>

```sh
response = self.client.post('/accounts/login/', {'username': 'beroli', 'password': '1234'})
self.assertIn(b"correct username", response.content)
```
</details>

###### test_login_success
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the user will be redirected to the main page if the successful login.|Use:  username - “renataberoli”; password - “123and4”|The user will be redirected to the “list of issues” page.|

<details>
<summary>Code - test_login_success</summary>

```sh
response = self.client.post('/accounts/login/', {'username': 'renataberoli', 'password': '123and4'})
self.assertRedirects(response, '/')
```
</details>

### Scenario 2 - List filters
###### test_search_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|This test aims to check if the search field works as expected.|Use: Use: “error” as the search argument.|The system will return only issues with “error” in some parts of the title.|

<details>
<summary>Code - test_search_filter</summary>

```sh
user = User.objects.get(username="renataberoli")
date = timezone.now()
Issue.objects.create(title='Slow internet error', author=user, creation_date=date)
Issue.objects.create(title='Teste title 2', author=user, creation_date=date)

self.client.login(username='renataberoli', password='123and4')
response = self.client.get("/", {"data": "error"})
self.assertIn(b"Slow internet error", response.content)
self.assertNotIn(b"Teste title 2", response.content)

```
</details>

###### test_priority_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the priority field works as expected.|Use: Use: “urgent” as the field’s option.|The system will return only issues with “Urgent” priority.|

<details>
<summary>Code - test_priority_filter</summary>

```sh
user = User.objects.get(username="renataberoli")
date = timezone.now()
Issue.objects.create(title='Test issue with priority urgent', author=user, creation_date=date, priority='1')
Issue.objects.create(title='Test issue with priority normal', author=user, creation_date=date, priority='3')

self.client.login(username='renataberoli', password='123and4')
response = self.client.get('/', {'priority': '1'})
self.assertIn(b"Test issue with priority urgent", response.content)
self.assertNotIn(b"Test issue with priority normal", response.content)

```
</details>

###### test_status_filter
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the status field works as expected.|Use: Use: “closed” as the field’s option.|The system will return only issues with the status “closed”.|
<details>
<summary>Code - test_status_filter</summary>

```sh
user = User.objects.get(username="renataberoli")
date = timezone.now()
Issue.objects.create(title='Test issue with status closed', author=user, creation_date=date, status='closed')
Issue.objects.create(title='Test issue with status open', author=user, creation_date=date, status='open')

self.client.login(username='renataberoli', password='123and4')
response = self.client.get('/', {'status': 'closed'})
self.assertIn(b"Test issue with status closed", response.content)
self.assertNotIn(b"Test issue with status open", response.content)

```
</details>

###### test_all_filters_together
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if all the list filters work together as expected.|Use: search argument - “error”; priority - “urgent”; status - “open”; label - “frontend”; assigned - “renataberoli”.|The system will show only the issue that matches all the filter's arguments.|
<details>
<summary>Code - test_all_filters_together</summary>

```sh
user = User.objects.get(username="renataberoli")
Issue.objects.create(title='Test issue with all arguments - error', author=user, priority='1', status='open',
                     label='frontend', assignee=user)
Issue.objects.create(title='Test issue without data arguments', author=user, priority='1', status='open',
                     label='frontend', assignee=user)

self.client.login(username='renataberoli', password='123and4')
response = self.client.get('/', {'data': 'error', 'priority': '1', 'status': 'open', 'label': 'frontend',
                                 'assignee': user.id})

self.assertIn(b"Test issue with all arguments - error", response.content)
self.assertNotIn(b"Test issue without data arguments", response.content)

```
</details>

### Scenario 3 - Create issue
###### test_issue_creation
| Description | Test Data | Expected Result | 
| ----------- | --------- | --------------- | 
|The test aims to check if the issue's creation is working as expected.|Use: title - “Test issue if issue is created”; project - “Acme”; status - “open”; assignee - “renataberoli”.|The system will create a new issue and redirect the user to the detail view.|

<details>
<summary>Code - test_issue_creation</summary>

```sh
user = User.objects.get(username="renataberoli")
self.client.login(username='renataberoli', password='123and4')
project = Project.objects.create(name='Acme')
response = self.client.post('/issue/new/', {'title': 'Test issue if issue is created', 'assignee': user.id,
                                            'project': project.id, 'status': 'open'})
issue = Issue.objects.get(title='Test issue if issue is created')
self.assertRedirects(response, f'/issue/{issue.id}/')

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