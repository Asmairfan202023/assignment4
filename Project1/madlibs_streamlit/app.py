import streamlit as st
import random

# Define Mad Libs stories
stories = {
    "Harry Potter": "One day, a {adjective} {noun} decided to {verb} all the way to Hogwarts.",
    "Coding": "I love coding in {language} using the {framework} framework!",
    "Zombie Apocalypse": "During the apocalypse, I grabbed my {weapon} and ran to {place} to escape the zombies!",
    "Hunger Games": "{tribute} from District {district} was chosen to fight in the Hunger Games!"
}

def main():
    st.title("🎭 Mad Libs Game with Streamlit!")
    st.subheader("Choose a story, fill in the blanks, and see your hilarious creation!")

    # User selects a story
    story_type = st.selectbox("Choose a Mad Libs theme:", list(stories.keys()))

    # Input fields based on the selected story
    inputs = {}
    if story_type == "Harry Potter":
        inputs["noun"] = st.text_input("Enter a noun:")
        inputs["verb"] = st.text_input("Enter a verb:")
        inputs["adjective"] = st.text_input("Enter an adjective:")
    elif story_type == "Coding":
        inputs["language"] = st.text_input("Enter a programming language:")
        inputs["framework"] = st.text_input("Enter a framework:")
    elif story_type == "Zombie Apocalypse":
        inputs["weapon"] = st.text_input("Enter a weapon:")
        inputs["place"] = st.text_input("Enter a place:")
    elif story_type == "Hunger Games":
        inputs["tribute"] = st.text_input("Enter a tribute's name:")
        inputs["district"] = st.text_input("Enter a district number:")

    # Generate Story Button
    if st.button("Generate Story"):
        if all(inputs.values()):  # Ensure all fields are filled
            story_template = stories[story_type]
            final_story = story_template.format(**inputs)
            st.success(final_story)
        else:
            st.warning("Please fill in all the blanks!")

if __name__ == "__main__":
    main()
