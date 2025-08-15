#Cafe menu
while True:
   print("Welcome to our Coffee-Shop , What would you like to drink ?")
   print(""" 1.Tea   15 Le
 2.Coffee   20 Le
 3.Nescafe   25 Le
 4.Latte   30 Le
 5.Anise   20 Le
 6.Mint   20 Le
 7.Water   10 Le""")
#Accepting User input
   item = input("Choose Drink number (1,2,3,4,5,6,7) from the menu: ")
   if item in ['1','2','3','4','5','6','7'] :
      quantity=int(input("Enter Item Quantity: "))
#The process
      if item =='1' :
         item_name="Tea"
         price=15
      elif item =='2' :
         item_name="Coffee"
         price=20
      elif item =='3' :
         item_name="Nescafe"
         price=25
      elif item =='4' :
         item_name="Latte"
         price=30
      elif item =='5' :
         item_name="Anise"
         price=20
      elif item =='6' :
         item_name="Mint"
         price=20
      elif item =='7' :
         item_name="Water"
         price=10
      Total_Price=price*quantity
#Dispaly the output
      output=f"                Receipt                       " \
         f"\n              Date:19/12/2024           " \
         f"\nItem:{item_name} \nPrice:{price} \nQuantity:{quantity}" \
         f"\nTotal:{Total_Price} " \
         f"\nThank You for ordering from us"
      print(output)
   else:
      print("You should choose form 1,2,3,4,5,6 or 7")
   break