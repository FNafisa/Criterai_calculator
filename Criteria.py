import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

about_page= st.Page(
    page= "Criteria.py",
    title= "Criteria Calculator",
    icon=":material/account_circle:",
    default=True
)

# setup page header
st.title('Criteria Calculator', anchor=False)
# text_page_header= """
#     <div dir= "rtl">
#     <h1>حاسبة تصنيف المقاولين</h1>
#     </div>
# """
# st.markdown(text_page_header, unsafe_allow_html=True)



st.divider()
col_input_basic, col_input_additional, col_output= st.columns(3,gap='medium')
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


# input fields for basic criteria
with col_input_basic:
    st.subheader('Basic Criteria (Maximum 80 points)', anchor= False)
    engineers_percentage = st.number_input('Percentage of Engineers in the company (%)', min_value=0.0, max_value=100.0, step=0.01,
                                       help=criteria_explanations['engineers_percentage'])
    technicians_percentage = st.number_input('Percentage of Technicians in the company (%)', min_value=0.0, max_value=100.0, step=0.01,
                                            help=criteria_explanations['technicians_percentage'])
    engineers_experience = st.number_input('Average years of Engineers\' experience', min_value=0, max_value=100, step=1,
                                        help=criteria_explanations['engineers_experience'])
    technicians_experience = st.number_input('Average years of Technicians\' experience', min_value=0, max_value=100, step=1,
                                            help=criteria_explanations['technicians_experience'])


# Input fields for additional criteria
with col_input_additional:
    st.subheader('Additional Criteria (Maximum 20 points)')
    saudis_percentage = st.number_input('Percentage of Saudi employees (%)', min_value=0.0, max_value=100.0, step=0.01,
                                    help=criteria_explanations['saudis_percentage'])
    saudi_engineers_percentage = st.number_input('Percentage of Saudi Engineers (%)', min_value=0.0, max_value=100.0, step=0.01,
                                                help=criteria_explanations['saudi_engineers_percentage'])
    high_wage_saudis_percentage = st.number_input('Percentage of High Wage Saudis (%)', min_value=0.0, max_value=100.0, step=0.01,
                                                help=criteria_explanations['high_wage_saudis_percentage'])
    saudi_women_percentage = st.number_input('Percentage of Saudi Women (%)', min_value=0.0, max_value=100.0, step=0.01,
                                            help=criteria_explanations['saudi_women_percentage'])



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

import streamlit as st
import streamlit.components.v1 as components



import streamlit as st

tab1, tab2, tab3 = st.tabs(['Instructions',"AI Recommendations", "Consultant"])

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

with tab3:

    html_content_iframe = """
    <iframe allow="join-ad-interest-group" data-tagging-id="AW-864381662" data-load-time="1737534024462" height="0" width="0" src="https://td.doubleclick.net/td/rul/864381662?random=1737534024425&amp;cv=11&amp;fst=1737534024425&amp;fmt=3&amp;bg=ffffff&amp;guid=ON&amp;async=1&amp;gtm=45be51l0v888918826za200zb9105249181&amp;gcd=13l3l3l3l1l1&amp;dma=0&amp;tag_exp=102067555~102067808~102081485~102123607~102308675&amp;u_w=1920&amp;u_h=1080&amp;url=https%3A%2F%2Fstudio.d-id.com%2Fagents%2Fshare%3Fid%3Dagt_WIQbwJKJ%26utm_source%3Dcopy%26key%3DWVhWMGFEQjhOalExTnpkaE16STFNak0yTW1SaE1UZGhPREZqTTJaaU9uZFFZMmt5U1Y5Q2VWaGxRa1V3VEVobGJFOVJkUT09&amp;hn=www.googleadservices.com&amp;frm=0&amp;tiba=D-ID%20Creative%20Reality%20Studio&amp;did=dZTQ1Zm&amp;gdid=dZTQ1Zm&amp;npa=0&amp;pscdl=noapi&amp;auid=1363006706.1730965553&amp;uaa=x86&amp;uab=64&amp;uafvl=Google%2520Chrome%3B131.0.6778.265%7CChromium%3B131.0.6778.265%7CNot_A%2520Brand%3B24.0.0.0&amp;uamb=0&amp;uam=&amp;uap=Windows&amp;uapv=10.0.0&amp;uaw=0&amp;fledge=1&amp;data=event%3Dgtag.config" style="display: none; visibility: hidden;"></iframe>
    """
    # Using Streamlit components to render custom HTML
    components.html(html_content_iframe, height=600)  # Adjust height as necessary
    

    html_content_scripts = """
    <div id="agent-container" style="height: 500px;"> <!-- You can adjust container settings -->
    <!-- Your script will target this div based on its settings -->
    </div>
    <script type="module"
        src="https://agent.d-id.com/v1/index.js"
        data-name="did-agent"
        data-mode="fabio"
        data-client-key="YourClientKey"  # Make sure to keep your keys secure
        data-agent-id="YourAgentID"
        data-monitor="true">
    </script>
    """

    # Using Streamlit components to render custom HTML
    components.html(html_content_scripts, height=600)  # Adjust height as necessary
