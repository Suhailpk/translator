import streamlit as st

from ibm_watson import LanguageTranslatorV3

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#define url and key for authentication

API_key = 'I6eCsG3fVH6k-L_4MYAbvgD_eoXk1U480UC8GezkUUcc'
url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/209d939b-59cb-4001-a707-013244cee735'

authentication = IAMAuthenticator(apikey=API_key)

transalator = LanguageTranslatorV3(version='2018-05-01',
                                    authenticator=authentication)

transalator.set_service_url(url)

#create the heading
st.title("Language Translator")


# create the markdown for langauges

option1 = st.selectbox('Choose the language to translate',
            ('English','Arabic','Malayalam','Hindi','Korean','Tamil','Russian'))


option2 = st.selectbox('Which language would you like to translate to',
            ('English','Arabic','Malayalam','Hindi','Korean','Tamil','Russian'))

sent = 'Enter the text in '+option1+' to translate'

launguage_lib = {
    'English':'en','Arabic':'ar','Malayalam':'ml','Hindi':'hi','Korean':'ko','Tamil':'ta','Russian':'ru'
}

text_area = st.text_area(sent,height= 250)

if st.button('Translate'):

    try:

        if option1 == option2:
            st.write('Both are not same language,please select different language')

        else:

            trans = transalator.translate(text_area,model_id=launguage_lib[option1]+"-"+launguage_lib[option2])
            trans_res = trans.get_result()['translations'][0]['translation']
            
            sent2 = 'Translated language  in '+option2+' are'

            st.markdown(sent2)
            st.write(trans_res)

    except:
        st.warning('Not empty field')

