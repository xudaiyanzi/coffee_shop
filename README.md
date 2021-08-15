# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

For this project, I have the url configuration:

AUTH0_DOMAIN = 'yxfs.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'drinks'

url: https://yxfs.us.auth0.com/authorize?audience=drinks&response_type=token&client_id=JBb4EvqoD56og5GPs2I1f42FyPniQmHY&redirect_uri=https://127.0.0.1:8080/login-results

Two dummy account:

(1)Barista
User: barista@udacity.com
Password: Udacity123*

token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBTSm12c19JSF94ZlhFeUhXREVmOSJ9.eyJpc3MiOiJodHRwczovL3l4ZnMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTk2ZTc5MjAxYzJlMDA2OTg1ODY2ZSIsImF1ZCI6ImRyaW5rcyIsImlhdCI6MTYyOTA1NzE2OCwiZXhwIjoxNjI5MDY0MzY4LCJhenAiOiJKQmI0RXZxb0Q1Nm9nNUdQczJJMWY0MkZ5UG5pUW1IWSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.JYXFmahdmBVN0C2j8GT15iIAcrX4Y3MgoFrEXj-u0VM3YaBtHDFUXBWAnAiCdqflWCYmypXyn3MlHRy-8j5dR37W_hTGrpbctzoCwVuIbuVMMCddGiEoLGulslniXKXUKhvjM0H2lLq4N8WvMgNM_QufmNzY59cdBufvyCY1Ks4Z4b4KubvH3Exau0Ba7sMpMplStRLzpz6zlzoprAxbmeLXhY_pHur5MZv99T3mFic-cYdr4qPOrylqaDtaxR1CUL9CdJ1TLejdHzHDElcZbsohozzULdWXHZE4NOdIdhUH-geAXa8fwGc8fbI5GWHAhhL0Tun0AUSpUTuqZ4tESQ

(2) manageer:
User: coffee_manager@udacity.com
Password: Udacity123*
token:

 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBTSm12c19JSF94ZlhFeUhXREVmOSJ9.eyJpc3MiOiJodHRwczovL3l4ZnMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTk2ZTUzYmYwZGI5MDA2OTdmMjg4ZiIsImF1ZCI6ImRyaW5rcyIsImlhdCI6MTYyOTA1Njk3MCwiZXhwIjoxNjI5MDY0MTcwLCJhenAiOiJKQmI0RXZxb0Q1Nm9nNUdQczJJMWY0MkZ5UG5pUW1IWSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.CJkIU6vlR8W3VuEZs9CSeYiB2tsGzMcil_d9MG2MlcgiDTwoeCR3HmpsmpB3S4423jIjK-w2jISnUho4c9eqdg4tac0YLxvQPnINV9pdRnm9YmaeQLgM0daEOwOeHMJgopTwq2oXkCnfP7a9hPcwxsJQwZ22wRPzPyjBzlIyHsoL7W0KlPSL1guVIJHJ13F_nY7KkTsWHp2KXIT-7Z6vn3pFuMsojNiCJtKtGeRi2EFvMiP43MCFv1PiFQo4u7K17Xd4oTmRKQ_77cC8d4JZCRgxWOL9lg39k7IB1vb-kxhsZITjQEYE1xtqpQg9cDJUzmIMO01Ek5mH50cWIz3Lpw

### Backend

The `./backend` directory contains a Flask server and SQLAlchemy module. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)
