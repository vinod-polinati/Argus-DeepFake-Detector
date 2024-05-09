import json
import streamlit as st
import os
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

st.set_page_config(layout='wide')

def cont(im1,t1,t11,im2,t2,t22,im3,t3,t33,im4,t4,t44):
    """Displays an image and text side-by-side in a Streamlit app.

    Args:
        image_path (str): Path to the image file.
        text (str): Text to display beside the image.
    """
    col1, col2, col3, col4 = st.columns(4)  # Adjust the number of columns for different layouts

  # Load the image using st.image()
    with col1:
        st.image(im1, width=300)# Adjust width as needed
        st.markdown(t1)
        st.markdown(t11)
  # Display the text using st.write()
    with col2:
        st.image(im2, width=300)# Adjust width as needed
        st.markdown(t2)
        st.markdown(t22)
    with col3:
        st.image(im3, width=300)# Adjust width as needed
        st.markdown(t3)
        st.markdown(t33)
    with col4:
        st.image(im4, width=300)# Adjust width as needed
        st.markdown(t4)
        st.markdown(t44)

def get_file_type(file):
    allowed_image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    allowed_video_extensions = ['mp4', 'avi', 'mkv']

    file_extension = file.name.split('.')[-1].lower()

    if file_extension in allowed_image_extensions:
        return 'image'
    elif file_extension in allowed_video_extensions:
        return 'video'
    else:
        st.error(f"Unsupported file type: {file.name} ({file_extension})")
        return 'unknown'  

def load_lottiefile(filepath: str):
    """Loads a Lottie animation from a JSON file, handling potential encoding issues.

    Args:
        filepath (str): Path to the Lottie JSON file.

    Returns:
        dict: The loaded Lottie animation data.

    Raises:
        UnicodeDecodeError: If the encoding of the file cannot be determined.
    """

    try:
        # Attempt to open the file with UTF-8 encoding (most common)
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except UnicodeDecodeError:
        # If UTF-8 fails, try common encodings for JSON files
        for encoding in ("latin-1", "iso-8859-1"):
            try:
                with open(filepath, "r", encoding=encoding) as f:
                    return json.load(f)
            except UnicodeDecodeError:
                pass

    # Raise an error if no encoding works
    raise UnicodeDecodeError("Could not determine encoding of Lottie JSON file")

try:
    gif1 = load_lottiefile("code.json")# Load the Lottie animation with error handling
    gif2 = load_lottiefile("code2.json")
    gif3 = load_lottiefile("new.json")
except UnicodeDecodeError as e:
    st.error(f"Error loading Lottie animation: {e}")
    st.write("Please ensure your 'code.json' file is in a compatible encoding (e.g., UTF-8).")
else:
    with st.container():
        st.write("##")
        gif_column, text_column = st.columns((1, 2))
        with gif_column:
            st_lottie(
                gif1,
                height=200
                )
        with text_column:
            st.markdown("## Assalamualaikum ")

st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        h2 {
            color: #007BFF;
            font-size: 80px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
    
    # Display skills in two columns

# Main content
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Credit'],
        icons=['person', 'code-slash', 'credit-card-2-front', 'chat-left-text-fill'],
        orientation="horizontal"
    )

if selected == 'About':
    with st.container():
        st.write("##")
        st.markdown("# DEEP FAKE DETECTION")
        st.write("##")
        gif_column, text_column = st.columns((1, 2))
        with gif_column:
            st_lottie(
                gif3,
                height=200
                )
        with text_column:
            st.markdown(""":small_blue_diamond:**Combating misinformation:** Deepfakes can be used to spread lies or propaganda, making it crucial to have tools to detect them.\n\n:small_blue_diamond:**Protecting reputations:** Deepfakes could be used to damage someone's image by putting them in compromising situations.Detection helps prevent this.\n\n:small_blue_diamond:**Building trust online:** By making it easier to spot deepfakes, deepfake detection can help maintain trust in the authenticity of online content.""")
        text_cl , gif_cl = st.columns((2,1))
        with text_cl:
            st.markdown(":small_blue_diamond:**Combats fraud:**Deepfake detection helps law enforcement investigate deepfake-related crimes like CEO fraud, where impersonation is used for financial gain.\n\n:small_blue_diamond:**Protecting businesses:**Businesses can leverage deepfake detection to shield themselves from malicious attacks. Deepfakes can be used by competitors to damage a brand's image or sabotage marketing efforts. By identifying such manipulated content, businesses can take action to mitigate the harm before it impacts sales.")  
        with gif_cl:
            st_lottie(
                gif2,
                height=200
            )
            
        
elif selected == "Projects":
    st.title("DEEPFAKE DETECTION APPLICATION")
    st.markdown("## Welcome :clap:")

    # Deepfake model selection with informative descriptions
    selected_options = st.multiselect(
        'Select A Deep Fake Model:',
        [1, 2, 3],
        key='model_selection',
        help="Select one or more deepfake detection models to use for analysis.")

    # File upload with clear guidance and validation
    uploaded_files = st.file_uploader(
        "Choose files to upload:",
        type=['jpg', 'png', 'mp4'],
        accept_multiple_files=True,
        help="Upload images or videos to analyze for potential deepfakes. Supported file types: JPG, PNG, MP4.")

    if uploaded_files:
        # Process uploaded files
        for file in uploaded_files:
            file_type = get_file_type(file)

            if file_type == 'image':
                st.image(file, caption=f"Uploaded Image - {file.name}", use_column_width=True)

            elif file_type == 'video':
                st.video(file, caption=f"Uploaded Video - {file.name}")

            # Add placeholder for deepfake detection results based on selected models
            st.empty()  # Create an empty container for future content
            st.markdown("_(Deepfake Detection Results will be displayed here)_")  # Add a placeholder text

    # Button with clear action and feedback
    if st.button("Hit Me!", key='analyze_button', help="Trigger deepfake analysis based on uploaded files and selected models."):
        if not uploaded_files:
            st.error("Please upload files to analyze.")
        else:
            # Perform deepfake analysis using selected models and display results
            st.success("Deepfake analysis in progress...")
            # Replace ... with actual analysis logic and result presentation

    # Review text area with optional input and validation
    review_text = st.text_area("Review please :", key='review_text', help="Optionally provide a review of the analysis results.")

    # Submit button with clear action and feedback
    if st.button("Submit", key='submit_button', help="Submit your analysis and review."):
        if not uploaded_files:
            st.error("Please upload files to analyze.")
        elif not review_text:
            st.error("Please provide a review.")
        elif not selected_options:
            st.error("Model is Not selected ")
        else:
            # Submit analysis and review (e.g., send to server, save to database)
            st.success("Submitted successfully!")
            st.balloons()

    
elif selected == 'Credit':
    st.markdown("# Team Members")
    im1="Vin.jpg"
    t1="#### **Vinod Polinati**"
    t11="### Machine Learning "

    im2="Raw.jpg"
    t2="#### **Reddy Rewat**"
    t22="### Machine Learning"
    
    im3="Sha.jpg"
    t3="#### **Shaik Shajid**"
    t33="### UI&UX Designer"
    
    im4="rah.jpg"
    t4="#### **Miazur Rahaman**"
    t44="### Streamlit Developer"
    
    cont(im1,t1,t11,im2,t2,t22,im3,t3,t33,im4,t4,t44)

st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        h2 {
            color: #007BFF;
            font-size: 70px;
        }
        h1{
            text-align: center;
        }
        h3{
            color: #0078FF;
            font-size: 50px;
        }
        h4{
            font-size: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)