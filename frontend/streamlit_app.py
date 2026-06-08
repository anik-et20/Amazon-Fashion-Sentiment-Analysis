import streamlit as st
import requests

st.set_page_config(
    page_title="Amazon Fashion Sentiment Analyzer",
    page_icon="🛍️",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("📊 Model Info")
    st.write("Model: Logistic Regression")
    st.write("Dataset: Amazon Fashion Reviews")
    st.write("Accuracy: 87%")

# Header
st.title("🛍️ Amazon Fashion Sentiment Analyzer")

st.markdown("""
Analyze customer reviews and predict their sentiment using a machine learning model trained on Amazon Fashion reviews.
""")

# Example Reviews
with st.expander("💡 Example Reviews"):
    st.write("**Positive:** This dress fits perfectly and the quality is amazing.")
    st.write("**Negative:** Poor stitching and the size was completely wrong.")
    st.write("**Neutral:** Product arrived on time and works as expected.")

review = st.text_area(
    "Enter Review",
    height=200,
    placeholder="Type a review here..."
)

col1, col2 = st.columns([1, 4])

with col1:
    analyze = st.button("Analyze")

if analyze:

    if not review.strip():
        st.warning("Please enter a review.")
        st.stop()

    with st.spinner("Analyzing review..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"review": review},
                timeout=10
            )

            result = response.json()

            sentiment = result["sentiment"]
            confidence = result["confidence"]

            st.divider()

            if sentiment.lower() == "positive":
                st.success("😊 Positive Review")

            elif sentiment.lower() == "negative":
                st.error("😞 Negative Review")

            else:
                st.warning("😐 Neutral Review")

            st.metric(
                label="Confidence",
                value=f"{confidence:.2%}"
            )

            st.progress(float(confidence))
            st.divider()

            if sentiment.lower() == "positive":
                st.success("😊 Positive Review")

            elif sentiment.lower() == "negative":
                st.error("😞 Negative Review")

            else:
                st.warning("😐 Neutral Review")

            st.metric(
                label="Confidence",
                value=f"{confidence:.2%}"
            )

            st.progress(float(confidence))

            # Review Statistics
            st.subheader("📈 Review Statistics")

            col1, col2 = st.columns(2)

            col1.metric(
                "Words",
                len(review.split())
            )

            col2.metric(
                "Characters",
                len(review)
            )

            # Estimated Rating
            st.subheader("⭐ Estimated Rating")

            if sentiment.lower() == "positive":
                st.write("⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐")

            elif sentiment.lower() == "negative":
                st.write("⭐ - ⭐⭐")

            else:
                st.write("⭐⭐⭐")

        except Exception as e:
            st.error(f"Error: {e}")