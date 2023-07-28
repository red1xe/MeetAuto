import streamlit as st
import pandas as pd
import pickle
from datetime import datetime, timedelta

def generate_time_sequence():
    start_time = datetime.strptime('00:00', '%H:%M')
    end_time = datetime.strptime('23:50', '%H:%M')  # Adjust the end time if needed

    time_sequence = []
    current_time = start_time

    while current_time <= end_time:
        time_sequence.append(current_time.strftime('%H:%M'))
        current_time += timedelta(minutes=10)

    return time_sequence

time_sequence_10min = generate_time_sequence()

# Set the page title
st.set_page_config(page_title='MeetAuto', page_icon=':robot-face:')

# Initialize st.session_state if not already initialized
if 'meetings' not in st.session_state:
    st.session_state['meetings'] = []

# Function to save meetings data to a file
def save_meetings_data(meetings_data):
    with open('meetings_data.pkl', 'wb') as file:
        pickle.dump(meetings_data, file)

# Function to load meetings data from a file
def load_meetings_data():
    try:
        with open('meetings_data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Load meetings data when the app starts
st.session_state['meetings'] = load_meetings_data()

# Function to remove a meeting based on its index
def remove_meeting(index):
    if index >= 0 and index < len(st.session_state['meetings']):
        del st.session_state['meetings'][index]
        save_meetings_data(st.session_state['meetings'])  # Save meetings data after deletion
        st.success('Meeting deleted successfully!')

# Function to capture user inputs when the "Add Meeting" button is clicked
def add_meeting():
    meeting_name = st.text_input('Please enter your meeting name :pencil::', placeholder='MATH203.01')
    meeting_link = st.text_input('Please enter your meeting link :link::', placeholder='https://zoom.us/j/1234567890?pwd=1234567890')
    meeting_day = st.selectbox('Please select your meeting day :sunrise::', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    meeting_time = st.select_slider('Please select your meeting time :watch::', options=time_sequence_10min, value=time_sequence_10min[0])
    meeting_type = st.radio('Please select your meeting type :ledger::', ['Daily', 'Weekly', 'Monthly'])

    if st.button('Add Meeting :sparkles:'):
        # Store the user inputs in the meetings list as a dictionary
        meeting_data = {
            'id': len(st.session_state['meetings']) + 1,
            'name': meeting_name,
            'link': meeting_link,
            'day': meeting_day,
            'time': meeting_time,
            'type': meeting_type
        }
        st.session_state['meetings'].append(meeting_data)
        save_meetings_data(st.session_state['meetings'])  # Save meetings data to a file
        st.success('Meeting added successfully!')

   
# Call the function to display the input widgets and capture user inputs
st.title('Meetings Automation :calendar:')
st.subheader('Add your meetings and the MeetAuto will do the rest:sunglasses:')
add_meeting()

# Display the meetings table and allow users to delete meetings
if st.session_state['meetings']:
    st.subheader('Current Meetings:')
    df = pd.DataFrame(st.session_state['meetings'])
    df['Delete'] = df.index  # Add an index column to identify the meeting
    # Create a delete button for each meeting
    df['Action'] = df.apply(lambda row: st.button(f"Delete '{row['id']}' Meeting", on_click=remove_meeting, args=[row['Delete']],use_container_width=True), axis=1)
    st.dataframe(df.drop('Delete', axis=1).drop('Action', axis=1))
else:
    st.subheader('No meetings added yet :x:')