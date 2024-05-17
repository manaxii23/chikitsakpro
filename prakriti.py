import streamlit as st

# Define the questions and their corresponding response options for Mental category
mental_questions = [
    {"question": "Performs Activities:", "options": ["Very Rapidly", "With Moderate Speed", "Slowly"]},
    {"question": "Motivated, Enthusiastic, and Excitable:", "options": ["Very Easily", "Moderately", "Non-changing and Steady"]},
    {"question": "Moods:", "options": ["Change Quickly", "Change Quickly and Intense", "Non-changing and Steady"]},
    {"question": "Learn:", "options": ["Quickly and Easily", "Somewhat Quickly and Easily", "Slowly"]},
    {"question": "Quality of Mind:", "options": ["Quick, Creative, Imaginative but Restless", "Sharp Penetrating", "Stable"]},
    {"question": "Memory:", "options": ["Good – Short Term", "Medium", "Good – Long Term"]},
    {"question": "Digestion:", "options": ["Inconsistent, Varies Between Weak and Strong", "Usually Strong", "Weak and Slow"]},
    {"question": "Appetite:", "options": ["Variable, Can Skip Meals Sometimes", "Strong Consistent appetite, not comfortable skipping meals", "Usually Mild, Can Skip Meals Without Discomfort"]},
    {"question": "Taste Preferences:", "options": ["Sweet, Sour and Salty", "Sweet, Bitter and Astringent", "Pungent, Bitter and Astringent"]},
    {"question": "Frequency of Bowel Movements:", "options": ["Irregularly", "Two or More Times Per Day", "Regularly"]},
    {"question": "Consistency of Faeces:", "options": ["Hard, Dry Stool", "Loose Stool, Soft Stool", "Well Formed"]},
    {"question": "Perspiration:", "options": ["Moderate", "Profuse with Body Odour", "Slight"]},
    {"question": "Sexual Desire:", "options": ["Small", "Small to Moderate", "Abundant"]},
    {"question": "Amount of Sleep:", "options": ["Usually 5-6 Hours", "Usually 6-8 Hours", "Usually 8 Hours or More"]},
    {"question": "Quality of Sleep:", "options": ["Light, Easily Interrupted", "Deep and Uninterrupted", "Deep and Heavy"]},
    {"question": "Type of Dreams:", "options": ["Fear, Flying, Running, Jumping, Climbing Trees and Mountains", "Anger, Violence, Struggle, War, Fire, Lightning, The Sun, Gold and Light", "Water, Lakes, Rivers, Oceans, Clouds, Swans, Flowers, and Romance"]},
    {"question": "Response to Challenge:", "options": ["Uncertain, Indecisive, Worried", "Angered, Impatient, Irritable", "Clear, Stable, Patient"]},
    {"question": "Speech:", "options": ["Fast, Omitting Words and Digressing", "Fast, Clear and Precise", "Slow, Clear and Sweet"]},
    {"question": "Gait:", "options": ["Fast with Light Step", "Medium Speed with Precise, Determined Step", "Slow, Steady and Fluid"]}
]

# Define the questions and their corresponding response options for Body category
body_questions = [
    {"question": "Shape of Face:", "options": ["Thin and Bony", "Oval, Angular", "Round, Full"]},
    {"question": "Complexion:", "options": ["Dark, Brownish or Black", "Fair, Reddish", "Light, Clear and Whitish"]},
    {"question": "Involuntary Body Movements:", "options": ["Twitching, Jerking and Fine Tremors", "Body is Usually Still", "Body is Usually Still"]},
    {"question": "Body Weight:", "options": ["Light, Five to Ten Pounds Below Normal", "Normal, Medium weight", "Heavy, Five or More Pounds Above Normal"]},
    {"question": "Build:", "options": ["Lean, Thin, Tall or Short", "Medium Build, Medium Height", "Thick, Large, Fleshy or Plump"]},
    {"question": "Texture or Quality of Skin:", "options": ["Dry, Coarse, Rough, Cracked or Scaling and Birthmarks", "Soft, Delicate and Sensitive with Freckles, Moles", "Soft, Smooth and Oily"]},
    {"question": "Body Temperature:", "options": ["Low, Cold", "High, always Feels Warm", "Low, body Feels Cool"]},
    {"question": "Stamina:", "options": ["Short", "Moderate", "Strong"]},
    {"question": "Shape and Quality of Eyes and Lashes:", "options": ["Small, Bulging and Deep-Set With Penetrating", "Sharp and Deep-Set With Penetrating", "Large Attractive and Full With Long Thick Lashes"]},
    {"question": "Dominant Hue of Sclera (white outer layer of the eyeball):", "options": ["Dark", "Yellow or Reddish", "White, Glossy"]},
    {"question": "Peculiar Characteristics of Eyes:", "options": ["Dry, Frequent Blinking", "Light, Sensitive, Easily Reddened", "Teary or Running"]},
    {"question": "Teeth:", "options": ["Very Small or Protruding, Crooked, Easily Cracked", "Moderate Size, Yellowish", "Strong, Large, White"]},
    {"question": "Nails:", "options": ["Short, Rough, Brittle, Dark and Lustreless", "Slightly Oily, Coppery or Pink Coloured", "Full, Thick, Moist and Oily"]},
    {"question": "Lips:", "options": ["Dark, Dry and Cracked", "Soft, Pink or Copper Coloured", "Full, Thick, Moist and Oily"]},
    {"question": "Size and Shape of Fingers:", "options": ["Very Short or Very Long, Stubby and Thick", "Medium Length, Square or Oval Shaped", "Full, Thick, Moist and Oily"]},
    {"question": "Colour and Texture of Hair:", "options": ["Thin, Coarse, Dry and Wiry. Darker in Colour or Balding", "Thin, Fine, Soft, Blonde or Red, early Greying", "Thick, glossy, Firmly Rooted. Wavy and Black"]},
    {"question": "Body hair:", "options": ["Scanty", "Moderate", "Thick and Plentiful"]},
    {"question": "Joints:", "options": ["Loose or Rigid, Pronounced, crack and Pop", "Smooth, Flexible, Well Knit", "Neither hidden of Prominent. Deep and Hidden"]},
    {"question": "Chest:", "options": ["Long, Sunken, Thin Ribs Easily Visible", "Medium in Length, Medium Thickness, Ribs not so Visible", "Broad, Strong and Covered With Flesh"]},
    {"question": "Body Odour:", "options": ["Little or No Perspiration", "Strong, Armpits Fetid (smelly) Perspiration", "None"]},
    {"question": "Tongue:", "options": ["Dark, Brownish, Thick, Rough and Very Cracked on the Sides", "Pink or Dark Red, Soft and Long", "Light, Heavy and Moist"]}
]

# Define the prakriti responses and their corresponding scores for Mental category
mental_prakriti_responses = {
    "Very Rapidly": "VATA",
    "With Moderate Speed": "PITTA",
    "Slowly": "KAPHA",
    "Very Easily": "VATA",
    "Moderately": "PITTA",
    "Non-changing and Steady": "KAPHA",
    "Change Quickly": "VATA",
    "Change Quickly and Intense": "PITTA",
    "Non-changing and Steady": "KAPHA",
    "Quickly and Easily": "VATA",
    "Somewhat Quickly and Easily": "PITTA",
    "Slowly": "KAPHA",
    "Quick, Creative, Imaginative but Restless": "VATA",
    "Sharp Penetrating": "PITTA",
    "Stable": "KAPHA",
    "Good – Short Term": "VATA",
    "Medium": "PITTA",
    "Good – Long Term": "KAPHA",
    "Inconsistent, Varies Between Weak and Strong": "VATA",
    "Usually Strong": "PITTA",
    "Weak and Slow": "KAPHA",
    "Variable, Can Skip Meals Sometimes":"VATA",
    "Strong Consistent appetite, not comfortable skipping meals": "PITTA",
    "Usually Mild, Can Skip Meals Without Discomfort": "KAPHA",
    "Sweet, Sour and Salty": "VATA",
    "Sweet, Bitter and Astringent": "PITTA",
    "Pungent, Bitter and Astringent": "KAPHA",
    "Irregularly": "VATA",
    "Two or More Times Per Day": "PITTA",
    "Regularly": "KAPHA",
    "Hard, Dry Stool": "VATA",
    "Loose Stool, Soft Stool": "PITTA",
    "Well Formed": "KAPHA",
    "Moderate": "VATA",
    "Profuse with Body Odour": "PITTA",
    "Slight": "KAPHA",
    "Small": "VATA",
    "Small to Moderate": "PITTA",
    "Abundant": "KAPHA",
    "Usually 5-6 Hours": "VATA",
    "Usually 6-8 Hours": "PITTA",
    "Usually 8 Hours or More": "KAPHA",
    "Light, Easily Interrupted": "VATA",
    "Deep and Uninterrupted": "PITTA",
    "Deep and Heavy": "KAPHA",
    "Fear, Flying, Running, Jumping, Climbing Trees and Mountains": "VATA",
    "Anger, Violence, Struggle, War, Fire, Lightning, The Sun, Gold and Light": "PITTA",
    "Water, Lakes, Rivers, Oceans, Clouds, Swans, Flowers, and Romance": "KAPHA",
    "Uncertain, Indecisive, Worried": "VATA",
    "Angered, Impatient, Irritable": "PITTA",
    "Clear, Stable, Patient": "KAPHA",
    "Fast, Omitting Words and Digressing": "VATA",
    "Fast, Clear and Precise": "PITTA",
    "Slow, Clear and Sweet": "KAPHA",
    "Fast with Light Step": "VATA",
    "Medium Speed with Precise, Determined Step": "PITTA",
    "Slow, Steady and Fluid": "KAPHA"
}

# Define the prakriti responses and their corresponding scores for Body category
body_prakriti_responses = {
    "Thin and Bony": "VATA",
    "Oval, Angular": "PITTA",
    "Round, Full": "KAPHA",
    "Dark, Brownish or Black": "VATA",
    "Fair, Reddish": "PITTA",
    "Light, Clear and Whitish": "KAPHA",
    "Twitching, Jerking and Fine Tremors": "VATA",
    "Body is Usually Still": "PITTA",
    "Body is Usually Still": "KAPHA",
    "Light, Five to Ten Pounds Below Normal": "VATA",
    "Normal, Medium weight": "PITTA",
    "Heavy, Five or More Pounds Above Normal": "KAPHA",
    "Lean, Thin, Tall or Short": "VATA",
    "Medium Build, Medium Height": "PITTA",
    "Thick, Large, Fleshy or Plump": "KAPHA",
    "Dry, Coarse, Rough, Cracked or Scaling and Birthmarks": "VATA",
    "Soft, Delicate and Sensitive with Freckles, Moles": "PITTA",
    "Soft, Smooth and Oily": "KAPHA",
    "Low, Cold": "VATA",
    "High, always Feels Warm": "PITTA",
    "Low, body Feels Cool": "KAPHA",
    "Short": "VATA",
    "Moderate": "PITTA",
    "Strong": "KAPHA",
    "Small, Bulging and Deep-Set With Penetrating": "VATA",
    "Sharp and Deep-Set With Penetrating": "PITTA",
"Large Attractive and Full With Long Thick Lashes": "KAPHA",
    "Dark": "VATA",
    "Yellow or Reddish": "PITTA",
    "White, Glossy": "KAPHA",
    "Dry, Frequent Blinking": "VATA",
    "Light, Sensitive, Easily Reddened": "PITTA",
    "Teary or Running": "KAPHA",
    "Very Small or Protruding, Crooked, Easily Cracked": "VATA",
    "Moderate Size, Yellowish": "PITTA",
    "Strong, Large, White": "KAPHA",
    "Short, Rough, Brittle, Dark and Lustreless": "VATA",
    "Slightly Oily, Coppery or Pink Coloured": "PITTA",
    "Full, Thick, Moist and Oily": "KAPHA",
    "Dark, Dry and Cracked": "VATA",
    "Soft, Pink or Copper Coloured": "PITTA",
    "Full, Thick, Moist and Oily": "KAPHA",
    "Very Short or Very Long, Stubby and Thick": "VATA",
    "Medium Length, Square or Oval Shaped": "PITTA",
    "Full, Thick, Moist and Oily": "KAPHA",
    "Thin, Coarse, Dry and Wiry. Darker in Colour or Balding": "VATA",
    "Thin, Fine, Soft, Blonde or Red, early Greying": "PITTA",
    "Thick, glossy, Firmly Rooted. Wavy and Black": "KAPHA",
    "Scanty": "VATA",
    "Moderate": "PITTA",
    "Thick and Plentiful": "KAPHA",
    "Loose or Rigid, Pronounced, crack and Pop": "VATA",
    "Smooth, Flexible, Well Knit": "PITTA",
    "Neither hidden of Prominent. Deep and Hidden": "KAPHA",
    "Long, Sunken, Thin Ribs Easily Visible": "VATA",
    "Medium in Length, Medium Thickness, Ribs not so Visible": "PITTA",
    "Broad, Strong and Covered With Flesh": "KAPHA",
    "Little or No Perspiration": "VATA",
    "Strong, Armpits Fetid (smelly) Perspiration": "PITTA",
    "None": "KAPHA",
    "Dark, Brownish, Thick, Rough and Very Cracked on the Sides": "VATA",
    "Pink or Dark Red, Soft and Long": "PITTA",
    "Light, Heavy and Moist": "KAPHA"
}

# Function to calculate prakriti scores for Mental category
def calculate_mental_prakriti_scores(user_answers):
    prakriti_scores = {"VATA": 0, "PITTA": 0, "KAPHA": 0}
    for answer in user_answers:
        prakriti_type = mental_prakriti_responses.get(answer)
        if prakriti_type:
            prakriti_scores[prakriti_type] += 1
    return prakriti_scores

# Function to calculate prakriti scores for Body category
def calculate_body_prakriti_scores(user_answers):
    prakriti_scores = {"VATA": 0, "PITTA": 0, "KAPHA": 0}
    for answer in user_answers:
        prakriti_type = body_prakriti_responses.get(answer)
        if prakriti_type:
            prakriti_scores[prakriti_type] += 1
    return prakriti_scores

# Function to calculate prakriti percentages for Mental category
def calculate_mental_prakriti_percentages(user_answers):
    total_questions = len(user_answers)
    prakriti_scores = calculate_mental_prakriti_scores(user_answers)
    prakriti_percentages = {prakriti_type: (score / total_questions) * 100 for prakriti_type, score in prakriti_scores.items()}
    return prakriti_percentages

# Function to calculate prakriti percentages for Body category
def calculate_body_prakriti_percentages(user_answers):
    total_questions = len(user_answers)
    prakriti_scores = calculate_body_prakriti_scores(user_answers)
    prakriti_percentages = {prakriti_type: (score / total_questions) * 100 for prakriti_type, score in prakriti_scores.items()}
    return prakriti_percentages

# Streamlit UI
def main():
    st.title("Prakriti Type Analysis")
    st.write("Welcome to the Prakriti Type Analysis Chatbot!")
    st.write("Answer the following questions to determine your Prakriti type.")

    # Mental category
    user_answers = ["Select one"] * len(mental_questions)

    for i, question in enumerate(mental_questions, start=1):
        key = f"select_{i}_{question['question']}"  # Unique key for each selectbox
        user_answer = st.selectbox(f"Mental Q{i}: {question['question']}", options=["Select one"] + question["options"], key=key, index=0)
        user_answers[i - 1] = user_answer

    if st.button("Calculate Mental"):
        unanswered_questions = [f"Q{i+1}" for i, answer in enumerate(user_answers) if answer == "Select one"]
        if unanswered_questions:
            st.error(f"Please select an option for the following questions: {', '.join(unanswered_questions)}")
        else:
            mental_prakriti_percentages = calculate_mental_prakriti_percentages(user_answers)
            st.write("Mental Prakriti Percentages:")
            for prakriti_type, percentage in mental_prakriti_percentages.items():
                st.write(f"{prakriti_type}: {percentage:.2f}%")
            dominant_mental_prakriti = max(mental_prakriti_percentages, key=mental_prakriti_percentages.get)
            st.write(f"Your mental prakriti type is {dominant_mental_prakriti}.")

    # Body category
    user_answers = ["Select one"] * len(body_questions)

    for i, question in enumerate(body_questions, start=1):
        key = f"select_{i}_{question['question']}"  # Unique key for each selectbox
        user_answer = st.selectbox(f"Body Q{i}: {question['question']}", options=["Select one"] + question["options"], key=key, index=0)
        user_answers[i - 1] = user_answer

    if st.button("Calculate Body"):
        unanswered_questions = [f"Q{i+1}" for i, answer in enumerate(user_answers) if answer == "Select one"]
        if unanswered_questions:
            st.error(f"Please select an option for the following questions: {', '.join(unanswered_questions)}")
        else:
            body_prakriti_percentages = calculate_body_prakriti_percentages(user_answers)
            st.write("Body Prakriti Percentages:")
            for prakriti_type, percentage in body_prakriti_percentages.items():
                st.write(f"{prakriti_type}: {percentage:.2f}%")
            dominant_body_prakriti = max(body_prakriti_percentages, key=body_prakriti_percentages.get)
            st.write(f"Your body prakriti type is {dominant_body_prakriti}.")

if __name__ == "__main__":
    main()
