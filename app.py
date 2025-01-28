from twilio.rest import Client
import streamlit as st

# Twilio credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Your Twilio number
twilio_number = '+35319128381'
#twilio_number = '+18447942513'
# The phone number you want to call


# Webhook URL to handle the call
webhook_url = '/incoming-call'
ph_no = st.text_input('Phone Number', placeholder = 'Enter phone number with country code Ex: +919999999999, +919999999990')
bulk_ph_no = st.file_uploader('Bulk Phone Numbers')
make_a_call = st.button('Make a call')
if make_a_call:
    # Make the call
    if bulk_ph_no is not None:
        contents = [x.decode('utf-8').strip('\r\n').strip('\n') for x in bulk_ph_no.readlines()]
        del contents[0]
        to_number_list=contents
        print(to_number_list)
    elif ph_no:
        to_number_list = [ x.strip(" ") for x in ph_no.split(',') ]
        print(to_number_list)
    for to_number in to_number_list:
        call = client.calls.create(
            to=to_number,
            from_=twilio_number,
            url=webhook_url  # This URL will be called during the call
        )
        print(f"Call SID: {call.sid}")

