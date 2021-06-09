HyperAgency
Project showing resumes and vacancy, and adding new ones

Using python, Django, HTML, CSS.

To open the website:
	1. Download the project. 
	2. In terminal open the folder where you downloaded the project.
	3. Create virtual enviroment:
		If you dont have installed virtual enviroment yet: pip install virtualenv
		Then create it:
		Unix:
			python -m venv
		Windows:
			python -m venv
	4. Open virtual enviroment - copy in terminal:
		Windows: 
			venv\Scripts\activate - to activate the virtual enviroment
			pip install Django==2.2 - if the Django is not installed
		Unix:
			source venv/bin/activate
			pip install Django==2.2


The first page is a menu, where you can choose to log in, sign in or check all the resumes or vacancies.
	Log in: There is 2 type of users: agent and job seekers. Agents are superusers and can create resumes and vacancies. Job seekers are normal users and are created through the sign-in page. Those can create resumes, but no vacancies. After you finish creating new resumes, you can log out and it will back to the first page.
	Sign in: For creating a new user (username and password).

Jacinta Mihelcic, May 2021
