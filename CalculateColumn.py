import pandas as pd

input_data = pd.read_excel('Input.xlsx')

#calculate a new column total = price * quantity
#save to output.xlsx

input_data['Total'] = input_data['Price'] * input_data['Quantity']

print(input_data)

input_data.to_excel('output.xlsx', index=False)