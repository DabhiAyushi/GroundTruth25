import streamlit as st
from generate_images import generate_ad_image
from generate_captions import generate_caption
from utils import create_zip
import os

st.title("🎨 AI Creative Studio")

logo = st.file_uploader("Upload Brand Logo")
product = st.file_uploader("Upload Product Image")
brand = st.text_input("Brand Name")
product_name = st.text_input("Product Name")

if st.button("Generate Creatives"):
    if not logo or not product or not brand or not product_name:
        st.error("Please upload images and fill all fields.")
    else:
        st.write("Generating creatives ...")

        files = []

        for i in range(1, 11):
            st.write(f"▶ Generating image {i}...")

            prompt = f"""
            Create a modern, professional advertisement image for {brand}'s product {product_name}.
            Use bold lighting, clean background, commercial style.
            Variation {i}.
            """

            # ---------------- Image ----------------
            img = generate_ad_image(prompt, i)

            if img is None:
                st.error(f"❌ Failed to generate image {i}, skipping...")
                continue

            # ---------------- Caption ----------------
            caption = generate_caption(brand, product_name)

            caption_file = f"caption_{i}.txt"
            with open(caption_file, "w") as f:
                f.write(caption)

            # Add to ZIP list
            files.append(img)
            files.append(caption_file)

        if len(files) == 0:
            st.error("Could not generate any creatives. Try again.")
        else:
            zip_file = create_zip(files)

            st.success("🎉 Your creatives are ready!")
            with open(zip_file, "rb") as f:
                st.download_button("⬇ Download ZIP", f, file_name="creatives.zip")