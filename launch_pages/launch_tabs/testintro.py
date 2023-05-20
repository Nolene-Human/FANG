import streamlit as lit
import Art.Animation.lottie_animations
from streamlit_lottie import st_lottie
from streamlit_extras.mention import mention   

def testing1():

    lit.subheader("Welcome to FANG's User Acceptance Tests")
    lit.markdown("\n")

    col1,gap, col2,gap2, col3 = lit.columns([6,1,5,1,5])

    col1.markdown("""
    **Quick note**
    ______________________________""")
    col1.markdown("""
    This is a the fist version of the applications MVP\n
    The testing does not include UI/UX feedback. Although an endeavor was made to make a good and usable product, not all resources were put into the UX/UI design,
    therefore you might note some inconsistencies among pages, especially around forms.\n
    **I value your feedback so if the question was not ask it does not mean you can provide the feedback (even if it is UX/UI), the last part of each section will have an option for you to add your notes, go wild.**\n""")


    col2.markdown("""
    **What are we testing!**
    _______________________
    - Registration Process
    - Login Process
    - Verification Process
    - Security Confidence""")


    col3.markdown("""
    **How to Test**
    ______________________________""")
    col3.markdown("""

    The survey is broken into 5 sections with 3-5 Questions each,
    You can test one feature, or
    You can test them all (approx 10min)

    - Follow the link below 
    - Answer the first 3questions
    - Go the the section that you have time to test
    - Test the feature
    - Share your thoughts\n
        
    ***The tools for Registered users are Not part of this test***

    """)
    with col3:
        mention(
            label="Feedback Form",
            icon=":superhero:",  
            url="https://forms.office.com/r/s6rJGXtTf3",
    )


        
    with col3:
        test=Art.Animation.lottie_animations.load_animation("Art/Animation/testing.json")
        st_lottie(
                test,
                speed=1,
                width=300,
                loop=True
        )

        lit.write("\n")
