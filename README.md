# hackillinois

This is our 2022 source code for HackIllinois. Our p
Hi there! If you are looking to explore the backend, I would look at `app.py` and `backend/service/service.py`.

If you are looking to explore the frontend, `frontend/src/App.js` and `frontend/src/components/Predictions/index.js` are great places to start.

AgroGen uses Google Cloud, mysql, flask and python in the backend. We came up with a mySQL database structure running on GCP in order to store the farmers login information as well as their produce items. The flask app runs the database as well as the models. The models were pretrained by the python notebook present on our github and are loaded in for use in the backend. In order to deploy the site live, we also serve a compiled version of our frontend on the site.

On the frontend, we use React and TailwindCSS in order to style components and save state between pages. Axios is used to interact with the backend APIs in order to perform actions such as registration, login, or adding produce.

```
### Backend development
```
python3 -m pip install flask
python3 app.py
```
### Web development
```
npm install
npm start
```

### Deployment

```
npm run build (if frontend changed)
<commit all changes>
git push heroku master
```