
import google.generativeai as genai
import json

def findDoctors(location):
    genai.configure(api_key="AIzaSyAcxIh84MuqI7jH6rckbuuJzSOpLN5jHDE")

    model = genai.GenerativeModel('gemini-pro')

    prompt = '''show me the top 5 rated skin doctors in '''+ location +''' with their location address in the python list format:
        [{
            name: 'doctor1name',
            address: 'doctor1address'
        },{
            name: 'doctor2name',
            address: 'doctor2address'
        }]
        Don't assign any variable name, just follow the format please
    '''

    response = model.generate_content(prompt)

    return json.loads(response.text)
