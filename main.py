import streamlit as st
st.title('An application i did on an Online Carpenter in his workshop and how the customers rated him')
st.write('Carpenter and the customer Relationship')

#### Let me now encode my streamlit app
def code():
    return 'Kaka'

### lets fit in the model in the Data i want to deploy

product_subcategory	= st.selectbox('product_subcategory', ['Patio Set', 'Sofa', 'Bar Stool', 'China Cabinet', 'Chest of Drawers', 'Desk', 'Kitchen Cabinet'])
delivery_status = st.selectbox('delivery_status', ['Failed Delivery', 'Cancelled', 'Pending', 'Delivered', 'In Transit'])
customer_rating = st.number_input('Customer choice of rating', value=0)
total_amount = st.number_input('Total amount paid by the customer', value=0)

if st.button('Reviews'):
    customer_rating > 2.9
    st.success(f'Rating from 3 and above the customer was happy,(product_subcategory:{product_subcategory}, (delivery_status:{delivery_status}, (customer_rating:{customer_rating}, (total_amount:{total_amount}  the customer was impressed by the carpenters work')
    st.error(f'Rating was below 3 the customer was unhappy,(product_subcategory:{product_subcategory}, (delivery_status:{delivery_status}, (customer_rating:{customer_rating}, (total_amount:{total_amount}  Not satisfied customer')
    
