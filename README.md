<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Final API project: CoderDojo coolest projects</h3>
  <p align="center">
    Backend of a management system for personal projects made by students for "Coolest Project".
    <br />
    <a href="https://finalapiyannickhendrickx.netlify.app/"><strong>frontend of the application hosted on netlify</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#coaches">Endpoints related to coaches</a>
    </li>
    <li>
      <a href="#students">Endpoints related to students</a>
    </li>
    <li>
      <a href="projects">Endpoints related to projects</a>
    </li>
    <li>
      <a href="#token">Endpoint related to token<c/a>
    </li>
    <li>
      <a href="#openAPI-documentation">openAPI documentation</a>
    </li>
    <li><a href="#future-features">Future features</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

For my API development project I decided to develop a system to manage the projects students work on during our CoderDojo training sessions. In the end these projects will be submitted to "Coolest Project" competition. In this application you are able to add new coaches, new students and add their personal projects so you can easily keep track of what projects they are working on. The frontend of this application already has the ability to do the following:

* Login interface where coaches can sign in
    * Oauth2.0
    * session cookie
* Get information about the currently signed in coach
* Get a list of all coaches
* Get information about a specific coach
* Add new coaches
* Get a list of all students (name, projects, ...)
* Get information about a specific student (name, projects, ...)
* Add new students
* Add new projects to studens
* Get a list of all projects



### Built With

[![Html][Html.html]][Html-url]
[![Python][Python.py]][Python-url]
[![FastAPI][FastAPI.py]][FastAPI-url]
[![AlpineJS][Alpine.js]][Alpine-url]


## Login page
Het frontend is voorzien van een loginpage waar een coach kan aanmelden, verder is er ook de mogelijkheid om het publieke gedeelte te bekijken:
![Login pagina][loginpage]\
Op het publieke gedeelte staat enkel een endpoint voor projecten op te vragen, andere endpoints bevatten persoonlijke gegevens en we willen dat enkel gemachtigde personen deze kunnen beheren.\
![Publieke pagina][publicpage]\
Ten slotte is er ook nog een gedeelte voor coaches, deze pagina is voorzien van alle endpoints om coaches, studenten & projecten te beheren.\
![Pagina voor gemachtigde][authorizedpage]
## Coaches
<!-- GET REQUEST for all coaches -->
## GET request to get all coaches
![Get all coaches][get-allcoaches]
This is a get request sent with Postman to the api, same method is used on the frontend. A list of all students will be returned.

<!-- GET REQUEST for specific coach -->
## GET request to get specific coach
![Get specific coaches][get-specificcoach]
This is a get request sent with Postman to the api, same method is used on the frontend. Information of a specific coach will be returned.

<!-- GET REQUEST for current coach that is logged on -->
## GET request to get information current logged on coach
![Get specific coaches][get-currentcoach]
This is a get request sent with Postman to the api, same method is used on the frontend. Information of the logged on coach will be returned.

<!-- POST REQUEST for new coach-->
## POST request to add a new coach
![Post new coach][post-coaches]
This is a post request sent with Postman to the api, same method is used on the frontend. A new coach will be added to the database.

<!-- PUT REQUEST for coach-->
## PUT request to update a coach
![update coach][put-coaches]
This is a post request sent with Postman to the api, same method is used on the frontend. A specific coach will be updated.

<!-- DELETE REQUEST for coach-->
## DELETE request to update a coach
![delete coach][delete-coach]
This is a post request sent with Postman to the api, same method is used on the frontend. A specific coach will be deleted.

## Students
<!-- GET REQUEST for all students -->
## GET request to get all students
![Get all students][get-allstudents]
This is a get request sent with Postman to the api, same method is used on the frontend. A list of all students will be returned.

<!-- GET REQUEST for specific student -->
## GET request to get specific student
![Get specific coaches][get-specificstudent]
This is a get request sent with Postman to the api, same method is used on the frontend. Information of a specific student will be returned.

<!-- POST REQUEST for new student -->
## POST request to add a new student
![Post new student][post-student]
This is a post request sent with Postman to the api, same method is used on the frontend. A new student will be added to the database.

## Projects
<!-- GET REQUEST for all projects -->
## GET request to get all projects
![Get all projects][get-allprojects]
This is a get request sent with Postman to the api, same method is used on the frontend. An unordered list of all projects will be returned.

<!-- POST REQUEST for new project -->
## POST request to add a new project
![Post new project][post-project]
This is a post request sent with Postman to the api, this method is not yet used on the frontend. A new subejct will be added to the specified student.

## Token
<!-- POST REQUEST for JWT token -->
## POST request to fetch new JWT token
Within postman we set the authentication to "OAuth2.0" with the following config:
![token config][post-token1]
after pressing "Get New Access Token" postman will send the post request and recieve a token in response:
![token response][post-token2]

<!-- openAPI documentation -->
## openAPI documentation
![full openapi][full-openapi]
This is the full documentation of the fastapi that can be found here : [swagger UI](https://system-service-yannickhendrickx.cloud.okteto.net/docs)

<!-- Future features -->
## Future features

- [ ] Give frontend proper style/functionality
    - [ ] Instead of buttons, make some data visible automatically

<!-- CONTACT -->
## Contact

Yannick Hendrickx - R0615765@student.thomasmore.be

Project Link: [https://github.com/YannickHendrickx/python-finalapi](https://github.com/YannickHendrickx/python-finalapi)

<p align="right">(<a href="#about-the-project">back to top</a>)</p>





<!-- MARKDOWN LINKS-->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Html.html]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://html.spec.whatwg.org/multipage/
[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/
[FastAPI.py]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastap
[FastAPI-url]: https://fastapi.tiangolo.com/
[Alpine.js]: https://img.shields.io/static/v1?style=for-the-badge&message=Alpine.js&color=222222&logo=Alpine.js&logoColor=8BC0D0&label=
[Alpine-url]: https://alpinejs.dev/
<!-- MARKDOWN IMAGES-->
[loginpage]: images/loginpage.png
[publicpage]: images/publicpage.png
[authorizedpage]: images/authorizedpage.png

[get-allcoaches]: images/get_allcoaches.png
[get-specificcoach]: images/get_specificcoach.png
[get-currentcoach]: images/get_currentcoach.png
[post-coaches]: images/post_coaches.png
[put-coaches]: images/put_coaches.png
[delete-coach]: images/delete_coach.png

[get-allstudents]: images/get_allstudents.png
[get-specificstudent]: images/get_specificstudent.png
[post-student]: images/post_student.png

[get-allprojects]: images/get_allprojects.png
[post-project]: images/post_project.png

[post-token1]: images/post_token1.png
[post-token2]: images/post_token2.png

[full-openapi]: images/openapi.png