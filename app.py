from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# This is necessary to allow the HTML file to talk to the Flask server
CORS(app) 

# 1. Knowledge Base: A dictionary of rules based on campus information and website data.
knowledge_base = {
    "college_office": {
        "questions": ["where is the college office?", "college office location", "principal's office", "admin office", "administration"],
        "solution": "The college office is located on the ground floor of the main building. You can find the Principal's office and other administrative sections here."
    },
    "first_year_staff": {
        "questions": ["first year staff room", "staff room for first year", "first year building"],
        "solution": "The staff room for the first-year building is on the first floor of the first-year building."
    },
    "t&p_hall": {
        "questions": ["where is the t&p hall?", "training and placement cell location", "t&p", "placement cell"],
        "solution": "The Training & Placement (T&P) hall is located near the auditorium. The auditorium is on the upper floor of the T&P hall."
    },
    "auditorium": {
        "questions": ["where is the auditorium?", "location of auditorium", "functions", "events"],
        "solution": "The auditorium is on the upper floor of the Training & Placement (T&P) hall. It is used for functions and events."
    },
    "v-bhandar": {
        "questions": ["where is vastu bhandar?", "location of stationery shop", "stationary shop", "college shop"],
        "solution": "Vastu Bhandar, the stationery shop, is a prominent building with a four-wheeler parking spot in front of it. It provides all stationary needed for college work."
    },
    "hostel": {
        "questions": ["hostel for students", "hostel facility", "hostel rules"],
        "solution": "Hostel facilities are available exclusively for first-year students, with two separate wings for boys and one for girls. A canteen is also available near the hostel."
    },
    "canteen": {
        "questions": ["where is the canteen?", "canteen location", "mess"],
        "solution": "The canteen is located near the hostel and provides meals and snacks."
    },
    "parking": {
        "questions": ["where can i park?", "parking spots", "two wheeler parking", "four wheeler parking"],
        "solution": "There are two four-wheeler parking spots: one in front of Vastu Bhandar and one near the vermi-compost area. There are three two-wheeler parking spots: near the first-year building, near Vastu Bhandar, and near the main building."
    },
    "library": {
        "questions": ["where is the library?", "library location", "reading hall", "research area", "books"],
        "solution": "The library is located near the sports ground, behind the school building. It has a research area and a study hall with seating for 100 students."
    },
    "clubs": {
        "questions": ["list of clubs", "college clubs", "robotics club", "aideas", "coap", "mesa", "tesa", "astronomy club", "ed-cell"],
        "solution": "The college has various active clubs, including the Robotics Club, AIDEAS, COAP, MESA, TESA, Astronomy Club, and the ED-cell."
    },
    "engineering_departments": {
        "questions": ["list of departments", "engineering branches", "b.e.", "m.e.", "printing", "mechanical", "electrical", "e&tc", "computer", "it", "ai & ds"],
        "solution": "The engineering departments are AI & DS, Printing and Packaging Technology, Mechanical, Electrical, E & TC, Computer, and IT. The college offers both BE and ME programs in these branches."
    },
    "management_department": {
        "questions": ["mba department", "management college", "bba", "mba"],
        "solution": "The college has a management department that offers BBA and MBA programs with specialities in IB, Plain, or Finance."
    },
    "sports": {
        "questions": ["sports facilities", "basketball", "badminton", "skating", "ground", "multi sport"],
        "solution": "Sports facilities include a Basketball court, a Badminton court, a Skating ground, and a common ground for multi-sport activities."
    },
    "admission": {
        "questions": ["admission process", "how to apply", "intake", "direct second year"],
        "solution": "The college has an intake of 60 students per BE branch (120 for Mechanical and E&TC), with an additional 30 seats via extra quota. 10% of seats are reserved for Direct Second Year students from diploma programs."
    },
    "accreditation": {
        "questions": ["accreditation", "naac", "naac rating"],
        "solution": "PVG's College of Engineering has been accredited 'A' by NAAC."
    },
    "contact": {
        "questions": ["contact info", "email address", "phone number", "telephone", "fax"],
        "solution": "The main college email is info@pvgcoet.ac.in. You can also call +91 020 24228258 / 65 / 79."
    },
    "website": {
        "questions": ["college website", "official website"],
        "solution": "The official college website is https://www.pvgcoet.ac.in/."
    },
    "general": {
        "questions": [],
        "solution": "I'm sorry, I don't have information on that topic. Please visit the relevant department or office for assistance."
    }
}

# 2. Inference Engine: The logic to process user input and match rules.
def find_solution(user_query):
    """
    Analyzes the user's query and finds the best matching solution from the knowledge base.
    """
    user_query = user_query.lower().strip()

    for category, rule in knowledge_base.items():
        if any(keyword in user_query for keyword in rule["questions"]):
            return rule["solution"]

    return knowledge_base["general"]["solution"]

# 3. Flask API Endpoint: This is what the frontend will talk to.
@app.route('/ask', methods=['POST'])
def ask_expert_system():
    data = request.get_json()
    user_question = data.get('question', '')
    solution = find_solution(user_question)
    return jsonify({"answer": solution})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
