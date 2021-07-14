import mysql.connector

mybd = mysql.connector.connect(host  ="localhost",user = "root",)

my_cursor = mybd.cursor()
# my_cursor.execute("CREATE DATABASE HOTEL_MANAGEMENT_SYSTEM")
option = True
user_input = 0;

while option:
	print()
	print(" ***** CSE 414 (DBMS) Semester Project ***** ")
	print("**********************************************************")
	print("*** Welcome To Hotel Management And Reservation System ***")
	print("Select From The Menu:")
	print("1 For Interfaces.")
	print("2 For RIGHT OUTER JOIN Implementation.")
	print("3 For LEFT OUTER JOIN Implementation.")
	print("4 For FULL OUTER JOIN Implementation.")
	print("5 For Exit.")

	user_input = int(input("Enter Your Input: "))
	
	if user_input == 1:
		interface_input = 0;
		interface_option = True
		while interface_option:
			
			print()
			print("**********************************************************")
			print(" *** Interfaces *** ")
			print("Select From The Menu:")
			print("1 For: Manager Interface")
			print("2 For: Receptionist Interface.")
			print("3 For: Cleaner Interface.")
			print("4 For: IT Tech Guy Interface.")
			print("5 For: Customer Interface.")
			print("6 For: Return To Main Menu.")
			interface_input = int(input("Enter Your Input Here: "))

			if interface_input == 1:
				
				print()
				print("**********************************************************")
				print(" *** Manager Interface *** ")
				# Manager View
				print()
				print("*** Hotel Information For Manager***")
				my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.manager_hotel_view")
				record = my_cursor.fetchall()
				print("Hotel Name: "+ record[0][1])
				print("Hotel Email Address: "+ record[0][2])
				print("Hotel Fax Address: "+ record[0][3])
				print("Hotel Location Address: "+ record[0][4])
				print("Hotel Description: "+ record[0][5])
				print("Hotel Current Budget: "+ str(record[0][6]))
				print("Hotel Establishment Date: "+ record[0][7])
				print("**********************************************************")

				print()
				print("Adding Employee To The System...")
				name = input("Employee Name: ")
				sure_name = input("Employee Sure Name: ")
				gender = input("Employee Gender: ")
				salary = int(input("Employee Salary: "))
				place_of_birth = input("Employee Place Of Birth: ")
				sql = "INSERT INTO HOTEL_MANAGEMENT_SYSTEM.employee (First_Name,Last_Name,Gender,Salary,Place_Of_Birth) VALUES (%s,%s,%s,%s,%s)"
				val = (name,sure_name,gender,salary,place_of_birth)
				my_cursor.execute(sql,val)
				mybd.commit()
				print("Employee Inserted Successfully !!!")

			elif interface_input == 2:
				interface2_input = 0;
				interface2_option = True

				while interface2_option:
					print()
					print("**********************************************************")
					print(" *** Receptionist Interface *** ")
					# Receptionist View
					print()
					print("*** Hotel Information For Receptionist ***")
					my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.reciptionist_hotel_view")
					record = my_cursor.fetchall()
					print("Hotel Name: "+ record[0][0])
					print("Hotel Fax Address: "+ record[0][1])
					print("Hotel Location Address: "+ record[0][2])
					print("Hotel Establishment Date: "+ record[0][3])
					print("**********************************************************")

					print()
					print("Select From The Menu:")
					print("1 For: Your Personal Details.")
					print("2 For: Book Rooms For Your Customers.")
					print("3 For: Back To Menu.")
					interface2_input = int(input("Enter Your Input Here: "))
						
					if interface2_input == 1:
						print("Receptionist's Personal Info")
					elif interface2_input == 2:
						print()
						print("Booking Rooms For Customers...")
						cus_name = input("Customer Name: ")
						cus_surename = input("Customer Sure Name: ")
						gender = input("Customer Gender: ")
						place_of_birth = input("Customer Place Of Birth: ")
						sql = "INSERT INTO HOTEL_MANAGEMENT_SYSTEM.customer (First_Name,Last_Name,Gender,Place_Of_Birth) VALUES (%s,%s,%s,%s)"
						val = (cus_name,cus_surename,gender,place_of_birth)
						my_cursor.execute(sql,val)
						mybd.commit()
						print("Room Booked For Mr/Miss: " + cus_name +" "+ cus_surename+" !!!")
					elif interface2_input == 3:
						interface2_option = False
					elif interface2_input > 3 or interface2_input < 1:
						print("Enter a Valid Input !!!")

			elif interface_input == 3:
				interface3_input = 0;
				interface3_option = True

				while interface3_option:
					print()
					print("**********************************************************")
					print(" *** Cleaner Interface *** ")

					# Cleaner View
					print()
					print("*** Manager Information For Cleaner ***")
					my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.cleaner_manager_view")
					record = my_cursor.fetchall()
					print("Manager First Name: "+ record[0][0])
					print("Manager Last Name: "+ record[0][1])
					print("Manager Email: "+ record[0][2])
					
					print()
					print("Select From The Menu:")
					print("1 For: Your Personal Details.")
					print("2 For: Request Cleaning Facilities To The Hotel.")
					print("3 For: Back To Menu.")
					interface3_input = int(input("Enter Your Input Here: "))
						
					if interface3_input == 1:
						print()
						print("Cleaner's Personal Info")
					elif interface3_input == 2:
						print()
						print("Requesting Cleaning Facilities To The Hotel...")
					elif interface3_input == 3:
						interface3_option = False
					elif interface3_input > 3 or interface3_input < 1:
						print("Enter a Valid Input !!!")
			elif interface_input == 4:
				interface4_input = 0
				interface4_option = True

				while interface4_option:
					print()
					print("**********************************************************")
					print(" *** IT Guy Interface *** ")
					# IT View
					print()
					print("*** Manager Information For IT Guy ***")
					my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.it_manager_view")
					record = my_cursor.fetchall()
					print("Manager First Name: "+ record[0][0])
					print("Manager Last Name: "+ record[0][1])
					print("Manager Phone Number: "+ record[0][2])
					print("Manager Email: "+ record[0][3])
					
					print()
					print("Select From The Menu:")
					print("1 For: Your Personal Details.")
					print("2 For: Find Out About A Customer.")
					print("3 For: Back To Menu.")
					interface4_input = int(input("Enter Your Input Here: "))
						
					if interface4_input == 1:
						print()
						print("IT's Personal Info")
					elif interface4_input == 2:
						print()
						print("Find Customer's Details...")
					elif interface4_input == 3:
						interface4_option = False
					elif interface4_input > 3 or interface4_input < 1:
						print("Enter a Valid Input !!!")
			elif interface_input == 5:
				interface5_input = 0
				interface5_option = True

				while interface5_option:
					print()
					print("**********************************************************")
					print(" *** Customer Interface *** ")
					
					# Customer View
					print()
					print("*** Hotel Information For Customer***")
					my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.customer_hotel_view")
					record = my_cursor.fetchall()
					print("Hotel Name: "+ record[0][0])
					print("Hotel Email Address: "+ record[0][1])
					print("Hotel Fax Address: "+ record[0][2])
					print("Hotel Location Address: "+ record[0][3])
					print("**********************************************************")
					print()
					print("Select From The Menu:")
					print("1 For: Book Room.")
					print("2 For: Back To Menu.")
					interface5_input = int(input("Enter Your Input Here: "))
						
					if interface5_input == 1:
						print()
						print("Booking Room...")
						cus_name = input("Customer Name: ")
						cus_surename = input("Customer Sure Name: ")
						gender = input("Customer Gender: ")
						place_of_birth = input("Customer Place Of Birth: ")
						sql = "INSERT INTO HOTEL_MANAGEMENT_SYSTEM.customer (First_Name,Last_Name,Gender,Place_Of_Birth) VALUES (%s,%s,%s,%s)"
						val = (cus_name,cus_surename,gender,place_of_birth)
						my_cursor.execute(sql,val)
						mybd.commit()
						print("Room Booked For Mr/Miss: " + cus_name +" "+ cus_surename+" !!!")
					elif interface5_input == 2:
						interface5_option = False
					elif interface5_input > 2 or interface5_input < 1:
						print("Enter a Valid Input !!!")
			elif interface_input == 6:
				interface_option = False
			elif interface_input > 6 or interface_input < 1:
				print("Enter a Valid Input !!!")
	elif user_input == 2:
		my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.customer RIGHT OUTER JOIN HOTEL_MANAGEMENT_SYSTEM.room_types ON HOTEL_MANAGEMENT_SYSTEM.customer.Customer_ID = HOTEL_MANAGEMENT_SYSTEM.room_types.CustomerId;") 
		record = my_cursor.fetchall()
		print()
		print("Customer_ID  First_Name  Last_Name  GenderDate_Of_Birth  Place_Of_Birth  ID  customerId  roomTypeId  roomTypeName")
		print()
		for x in range(len(record)):
			print(record[x])

	elif user_input == 3:
		my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.customer LEFT OUTER JOIN HOTEL_MANAGEMENT_SYSTEM.room_types ON HOTEL_MANAGEMENT_SYSTEM.customer.Customer_ID = HOTEL_MANAGEMENT_SYSTEM.room_types.CustomerId;") 
		record = my_cursor.fetchall()
		print()
		print("Customer_ID  First_Name  Last_Name  GenderDate_Of_Birth  Place_Of_Birth  ID  customerId  roomTypeId  roomTypeName")
		print()
		for x in range(len(record)):
			print(record[x])
	elif user_input == 4:
		my_cursor.execute("SELECT * FROM HOTEL_MANAGEMENT_SYSTEM.customer INNER JOIN HOTEL_MANAGEMENT_SYSTEM.room_types ON HOTEL_MANAGEMENT_SYSTEM.customer.Customer_ID = HOTEL_MANAGEMENT_SYSTEM.room_types.CustomerId;") 
		record = my_cursor.fetchall()
		print()
		print("Customer_ID  First_Name  Last_Name  GenderDate_Of_Birth  Place_Of_Birth  ID  customerId  roomTypeId  roomTypeName")
		print()
		for x in range(len(record)):
			print(record[x])
	elif user_input == 5:
		option = False
	elif user_input > 5 or user_input < 1:
		print("Enter a Valid Input !!!")