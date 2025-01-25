import streamlit as st
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# page setup:
# - title
# - width
# - config
st.set_page_config(page_title='محاكي المعايير الفنية', layout="wide", page_icon="🟢")

# about_page= st.Page(
#     page= "Criteria.py",
#     title= "Criteria Calculator",
#     icon=":material/account_circle:",
#     default=True
# )

from PIL import Image
import requests
from io import BytesIO

# Load the image from the web
response = requests.get("https://ournews.sa/wp-content/uploads/2021/10/2-2.jpg")
image = Image.open(BytesIO(response.content))

# Display image next to the title
col1, col2 = st.columns([1, 2], gap='large')
with col1:
    st.image(image, width=200)  # Adjust width as necessary
with col2:
    st.markdown("# Technical Criteria Simulator")

# The rest of your Streamlit code goes here

# The rest of your Streamlit code goes here

# st.title('Technical Criteria Simulator', anchor=False)
# text_page_header= """
#     <div dir= "rtl">
#     <h1>حاسبة تصنيف المقاولين</h1>
#     </div>
# """
# st.markdown(text_page_header, unsafe_allow_html=True)
st.divider()

col_main_fuctions, col_support_fuctions= st.columns([0.7, 0.3])


with col_main_fuctions:

    # build the calculator
    criteria_explanations = {
        'engineers_percentage': 'The percentage of total employees that are engineers. This impacts the technical capabilities of the company.',
        'technicians_percentage': 'The percentage of total employees that are technicians. Technicians are crucial for operational success.',
        'engineers_experience': 'The average years of experience of engineers in your company. More experienced engineers can handle complex projects.',
        'technicians_experience': 'The average years of experience of technicians in your company. Experienced technicians ensure higher quality work.',
        'saudis_percentage': 'The percentage of Saudi nationals among total employees. This reflects the company\'s support of local employment.',
        'saudi_engineers_percentage': 'The percentage of engineers who are Saudi nationals. Promotes local expertise in engineering roles.',
        'high_wage_saudis_percentage': 'The percentage of Saudi nationals earning high wages. Indicates investment in high-skilled local labor.',
        'saudi_women_percentage': 'The percentage of female Saudi nationals in the company. Supports gender diversity in the workplace.'
    }

    # Main functions Sections: the calculator
    col_input_basic, col_input_additional, col_output= st.columns(3,gap='medium')
    # INPUT fields for basic criteria
    with col_input_basic:
        st.subheader('Basic Criteria', anchor= False)
        st.write('(Maximum 80 points)')
        engineers_percentage = st.number_input('Percentage of Engineers in the company (%)', min_value=0.0, max_value=100.0, step=0.01,
                                        help=criteria_explanations['engineers_percentage'])
        technicians_percentage = st.number_input('Percentage of Technicians in the company (%)', min_value=0.0, max_value=100.0, step=0.01,
                                                help=criteria_explanations['technicians_percentage'])
        engineers_experience = st.number_input('Average years of Engineers\' experience', min_value=0, max_value=100, step=1,
                                            help=criteria_explanations['engineers_experience'])
        technicians_experience = st.number_input('Average years of Technicians\' experience', min_value=0, max_value=100, step=1,
                                                help=criteria_explanations['technicians_experience'])
    # INPUT fields for additional criteria
    with col_input_additional:
        st.subheader('Additional Criteria')
        st.write('(Maximum 20 points)')
        saudis_percentage = st.number_input('Percentage of Saudi employees (%)', min_value=0.0, max_value=100.0, step=0.01,
                                        help=criteria_explanations['saudis_percentage'])
        saudi_engineers_percentage = st.number_input('Percentage of Saudi Engineers (%)', min_value=0.0, max_value=100.0, step=0.01,
                                                    help=criteria_explanations['saudi_engineers_percentage'])
        high_wage_saudis_percentage = st.number_input('Percentage of High Wage Saudis (%)', min_value=0.0, max_value=100.0, step=0.01,
                                                    help=criteria_explanations['high_wage_saudis_percentage'])
        saudi_women_percentage = st.number_input('Percentage of Saudi Women (%)', min_value=0.0, max_value=100.0, step=0.01,
                                                help=criteria_explanations['saudi_women_percentage'])
    # OUTPUT field
    with col_output:
        # Button to calculate score
        if st.button('Calculate Score'):
            # Calculate the basic score
            basic_score = min(engineers_percentage, 30) + min(technicians_percentage, 30) + min(engineers_experience, 10) + min(technicians_experience, 10)
            
            # Calculate the additional score
            additional_score = min(saudis_percentage, 5) + min(saudi_engineers_percentage, 5) + min(high_wage_saudis_percentage, 5) + min(saudi_women_percentage, 5)
            
            
            # Total score
            total_score = basic_score + additional_score
            
        
            # Determine the category based on the total score
            if total_score >= 81:
                category = 'Excellent'
            elif total_score >= 61:
                category = 'Good'
            elif total_score >= 41:
                category = 'Average'
            elif total_score >= 21:
                category = 'Below Average'
            else:
                category = 'Poor'


            st.subheader('Calculated Score')
            st.write(f"Basic Criteria Score: {basic_score} points")
            st.write(f"Additional Criteria Score: {additional_score} points")
            st.write(f"Total Score: {total_score} points")
            st.write(f"Category: {category}")


    st.divider()
    # Main Functions Section: Tabs (Instruction and AI Consultant)
    tab1, tab2 = st.tabs(['Instructions',"AI Consultant"])

    # the first tab is for instuctions on how the classification works
    with tab1:
        # RTL text using HTML in Streamlit
        # rtl_text= """
        # <div dir= "rtl">
        # <h2>تصنيف النتيجة</h2>
        # <ul>
        # <li><b>ضعيف</b>: النتيجة أقل من 18.5</li>
        # <li><b>طبيعي</b>: النتيجة بين 18.5 و 24.9</li>
        # <li><b>زائد</b>: النتيجة بين 25 و 29.9</li>
        # <li><b>خطير</b>: النتيجة أكثر من 30</li>
        # </ul>
        # </div>
        # """

        intructions_text= """
        <div>
        <h3>Score Categories</h3>
        <h4>Determine the score ranges that correspond to each category. For example, if the maximum possible score is 100 (80 from basic criteria + 20 from additional criteria), you might categorize the scores as follows:</h4>
        <ul>
        <li><b>Excellent</b>: 81-100</li>
        <li><b>Good</b>: 61-80</li>
        <li><b>Average</b>: 41-60</li>
        <li><b>Below Average</b>: 21-40</li>
        <li><b>Poor</b>: 0-20</li>
        </ul>
        </div>
        """
        st.markdown(intructions_text, unsafe_allow_html=True)

    with tab2:
        # HTML content
        html_string = """
        <iframe src="https://copilotstudio.microsoft.com/environments/Default-eb90203d-ff63-4590-a567-64b68f6f4f9d/bots/cr6fb_websiteQACopilot/webchat?__version__=2" width="700" height="500" frameborder="0" style="border:0" allowfullscreen></iframe>
        """
        # Embed the iframe
        components.html(html_string, height=500)


with col_support_fuctions:
    html_content_scripts = """
    <script
    type="module"
    src="https://agent.d-id.com/v1/index.js"
    data-name="did-agent"
    data-mode="fabio"
    data-client-key="YXV0aDB8NjQ1NzdhMzI1MjM2MmRhMTdhODFjM2ZiOndQY2kySV9CeVhlQkUwTEhlbE9RdQ=="
    data-agent-id="agt_WIQbwJKJ"
    data-monitor="true">
    </script>
    """

    # Using Streamlit components to render custom HTML
    components.html(html_content_scripts, height=800)  # Adjust height as necessary
    # This button will open the form
    if st.button('Contact Us'):
        with st.form(key='contact_form'):
            st.write('Please enter your details:')
            name = st.text_input('Name', key='name')
            email = st.text_input('Email', key='email')
            feedback_type = st.selectbox('Type', ['Complaint', 'Comment'], key='feedback_type')
            description = st.text_area('Description', key='description')

            # Form submission buttons
            submit_button = st.form_submit_button('Submit')
            cancel_button = st.form_submit_button('Cancel')

            if submit_button:
                if name.strip() and email.strip() and description.strip():  # Check for non-empty strings
                    st.success('Thank you for your feedback!')
                    # Add your logic here for what to do with the form data
                else:
                    st.error('All fields are required. Please fill out all fields.')

            if cancel_button:
                # Clearing inputs by rerunning the app to reset the state
                st.experimental_rerun()

# st.divider()
# Add this code at the end of your Streamlit script to display the footer
footer = """
<style>
.footer {
    width: 100%;
    background-color: ; /* Lighter grey background */
    color: green; /* Olive text */
    border-top: 3px solid green; /* Olive border */
    padding: 10px 0;
    font-size: 12px;
}
.footer .links {
    width: 50%;
    float: left;
    padding: 8px 0;
    text-align: left;
    margin-left: 10%;
}
.footer .privacy {
    width: 40%;
    float: right;
    padding: 8px 0;
    text-align: right;
    margin-right: 10%;
}
a {
    color: green; /* Olive links */
    padding: 5px;
}
.privacy a {
    color: #024610; /* Dark green */
    transition: color 0.3s; /* Smooth transition for hover effect */
}
.privacy a:hover {
    color: #90EE90; /* Light green when hovered */
}
a:hover {
    text-decoration: none;
    opacity: 0.8;
}
</style>
<div class='footer'>
    <div class='links'>
        <a href='https://www.youtube.com' target='_blank'><img src='https://img.icons8.com/color/48/000000/youtube-play.png' style='vertical-align: middle;'/></a>
        <a href='https://twitter.com/x' target='_blank'><img src='https://img.icons8.com/color/48/000000/twitter-circled.png' style='vertical-align: middle;'/></a>
        <a href='https://www.instagram.com' target='_blank'><img src='https://img.icons8.com/color/48/000000/instagram-new.png' style='vertical-align: middle;'/></a>
    </div>
    <div class='privacy'>
        <a href='https://sca.sa/ar/rulespageone' target='_blank'>Privacy Policy</a>
    </div>
    <div style='clear: both; text-align: center; margin-top: 10px;'>© 2025 Your Company Name. All Rights Reserved.</div>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

