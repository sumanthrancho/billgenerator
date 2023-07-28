# Bill Generation
import streamlit as st


st.title("Rancho Labs")
st.title(' Bill generator!')

choice = st.text_input("Hello. Would you like to order something? Please answer YES/ NO or yes/no")

Tomatoes =40
Onions =60
Potatoes =55
Brinjal = 65
Cabbage= 75
Cauliflower = 70
Capsicum =80
 
if(choice=="YES" or choice=='yes'):
  st.write("We have a wide range of products")
  nooftomatoes = st.number_input('How many kilos of TOMATOES would you like to purchase?'  ,step=1)
  noofonions = st.number_input('How many kilos of ONIONS would you like to purchase?' ,step=1)
  noofpotatoes = st.number_input('How many kilos of POTATOES would you like to purchase?',step=1)
  noofBrinjal = st.number_input('How many kilos of BRINJAL would you like to purchase?',step=1)
  noofcabbage = st.number_input('How many kilos of cabbage would you like to purchase?',step=1)
  noofcauliflower = st.number_input('How many kilos of cauliflower would you like to purchase?',step=1)
  noofcapsicum = st.number_input('How many kilos of capsicum would you like to purchase?',step=1)

  total_cost_of_tomato =nooftomatoes*Tomatoes
  total_cost_of_onion = noofonions*Onions
  total_cost_of_potatoes =noofpotatoes*Potatoes
  total_cost_of_Brinjal =noofBrinjal*Brinjal
  total_cost_of_cabbage = noofcabbage*Cabbage
  total_cost_of_cauliflower=noofcauliflower*Cauliflower
  total_cost_of_capsicum =noofcapsicum*Capsicum
  Total_bill= total_cost_of_tomato+total_cost_of_onion+total_cost_of_potatoes+total_cost_of_Brinjal+total_cost_of_cabbage+total_cost_of_cauliflower+total_cost_of_capsicum
  if(st.button('Submit')):
   if(Total_bill>0):
    st.success(" Total bill :{} ".format(Total_bill))
   else:
    st.error(" Total bill :{} ".format(Total_bill))
elif(choice=='N' or choice=='n'):
 st.error("Thank you for visitng. Goodbyee")
else:
 st.warning("please give input yes or no")
 
