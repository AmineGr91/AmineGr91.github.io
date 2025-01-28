weight = 4.8
premium_ground_shipping= 125

#Ground Shipping 
if weight <= 2:
  cost_ground = weight * 1.5 + 20

elif weight > 2 and weight <= 6 :
  cost_ground = weight * 3.0 + 20

elif weight > 6 and weight <= 10 :
  cost_ground = weight * 4.0 + 20

else :
    cost_ground = weight * 4.75 + 20

print("Your Cost to ship the package with Ground Shipping is :" , cost_ground)

#Ground Shipping Premium
print("Ground Shipping Premium $", premium_ground_shipping)


#Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.50

elif weight > 2 and weight <= 6 :
  cost_drone = weight * 9

elif weight > 6 and weight <= 10 :
  cost_drone = weight * 12

else :
    cost_drone = weight * 14.25

print("Your Cost to ship the package with Drone Shipping is :" , cost_drone)