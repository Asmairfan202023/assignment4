import streamlit as st
import pandas as pd

def main():
    st.title("🎂 Cake Order Form")
    
    with st.container():
        # Customer Name
        name = st.text_input("Enter your name:")
        
        # Cake Type Selection
        cake_type = st.selectbox("Select Cake Type:", ["Chocolate", "Vanilla", "Red Velvet", "Black Forest", "Strawberry"])
        
        # Cake Size Selection
        cake_size = st.radio("Select Cake Size:", ["Small (1 Pound)", "Medium (2 Pounds)", "Large (3 Pounds)"])
        
        # Additional Flavors
        flavors = st.multiselect("Select Additional Flavors:", ["Caramel", "Blueberry", "Raspberry", "Coffee", "Almond"])
        
        # Special Message
        special_message = st.text_area("Enter a special message for the cake:")
        
        # Number of Layers
        layers = st.slider("Select Number of Layers (Max 5):", min_value=1, max_value=5)
    
    # Submit Button
    if st.button("Submit Order"):
        order_data = {
            "Name": [name],
            "Cake Type": [cake_type],
            "Cake Size": [cake_size],
            "Additional Flavors": [', '.join(flavors) if flavors else "None"],
            "Special Message": [special_message if special_message else "None"],
            "Layers": [layers]
        }
        df = pd.DataFrame(order_data)
        
        st.success("Order placed successfully! Here are the details:")
        st.dataframe(df, height=200)
        
if __name__ == "__main__":
    main()
