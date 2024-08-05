# Recursive Wordhunt Solver 🧩
_A project by Filipp Krasovsky & Luke Mileski_
#### Streamlit Url: 
https://wordhuntersolver.streamlit.app/

## Overview 
This project uses recursive logic to find possible solutions to a crossword puzzle similar to WordHunt, a game available 
on the <a href="https://apps.apple.com/us/app/word-hunt/id1357352041">App Store</a> for Apple & Mac devices. The app is deployed and hosted through Streamlit, a service that enables developers to create Single Page Applications using only Python.

### Flow
A user is prompted to specify the dimensions of an N x N grid (ie 3 rows, 3 columns, etc.)

The user is then offered the choice to either populate the letters in the grid, or use the `randomize` feature to have letters generated for them.

The app turns the grid into a series of traversable nodes and references a standard english dictionary for which letter combinations make up valid english words.

The list is returned to the user along with the longest word, which the grid highlights.

A reset button allows the user to start over.

### Remarks: Streamlit 
Streamlit is a reactive framework, similar to `react.js`, and uses a session state to manage variables. Any time the user interacts with the application, the main script re-executes. To this end, the app logic is configured in chunks inside of a single `main` function that terminate by providing a null return statement in order to lock the user into a single portion of the app flow.

## Local Development

```
git clone https://github.com/kayfilipp/wordHuntSolver.git
cd wordHuntSolver
pip install -r requirements.txt
streamlit run main.py 
```

## Deploying to Streamlit 

1. After making a streamlit account, navigate to https://share.streamlit.io/ and click `Create App`. 
2. Select `Yes, I already have an App.`
3. Specify the repository you used to clone this app.
4. Branch: `Master`
5. main file path: `main.py`
6. Advanced Settings > Python Version: `3.11`
7. Deploy