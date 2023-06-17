# Healthcare Pro GPT
## A LLM based AI for personal healthcare suggestions

### By: Team Tru
- Gurneet Singh
- Aaryan Palit

### Note: This application must be used only for reference purpose and you should always consult a doctor.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Healthcare pro is an healthcare recommendation web app, based on ChatGPT 3, with feature such as voice output as well.

## Usage

- Input your current condition.
- Use the slider to tell since how many days you have been feeling the same
- Click on Submit Button

## The program outputs the follwing:
- What could be the cause of your current state/disease 
- What could be possible medications you can take to improve your state
- What all other possible symptoms you can be facing at the time

## Tech

Healthcare Pro uses the following to work properly:

- GPT-3 API : Developed by OpenAI, it uses the "gpt3-turbo" model to work. Works at 3 Rate/minute.
- Streamlit : Helps to create the web app and frontend of the application
- Google Text-to-Speech Converter

And of course Healthcare pro itself is open source with a [public repository](https://github.com/Gurneet1928/healthcare-pro-gpt)
 on GitHub.

## Installation and Running

Heatlhcare pro requires python v3.8+ to run.

To run the webapp, clone the repository using:

```sh
git clone https://github.com/Gurneet1928/healthcare-pro-gpt.git
```
and then run the following command:
```sh
python -m streamlit run app.py
```
or
```sh
streamlit run app.py
```

## Development

Want to contribute? Great!
Just make a pull request or send us the mail and we will contact you.

## License

MIT

**Free Software, Hell Yeah!**
