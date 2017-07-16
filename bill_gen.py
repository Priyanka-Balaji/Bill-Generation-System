import csv
class products:
	def __init__(self,filename):
		self.dict_bill=dict()
		self.filename=filename
		f=open(self.filename,'r')
		reader=csv.DictReader(f)
		for row in reader:
			self.dict_bill.update({row['Product']:{'Name':row['Product'],'Price':float(row['Price']),'Quantity':int(row['Quantity'])}})
		print(self.dict_bill)
		f.close()
	def search_item(self):
		print("\nEnter the product to search :")
		n=raw_input()
		print(self.dict_bill[n])
	def modify(self):
		print("\nEnter the product to be modified :")
		n=raw_input()
		print("\nEnter 1 to modify the Quantity and 2 to modify the Price :");
		m=input()
		if(m==1):
			print("\nEnter the Quantity : ")
			value=input()
			self.dict_bill[n]['Quantity']=value
		else:
			print("\nEnter the price : ")
			value=input()
			self.dict_bill[n]['Price']=value
 	def delete(self):
		print("\nenter the item to be deleted : ")
		del self.dict_bill[raw_input()]	
	def add(self):
		print("\nEnter the item to add : ")
		name=raw_input()
		print("Enter the Price :")
		p=input()
		print("\nEnter the Quantity : ");
		q=input()
		self.dict_bill.update({name:{'Name':name,'Price':p,'Quantity':q}})
	def print_list(self):
		print(self.dict_bill)	 
	def total(self):
		total=0
		for k in self.dict_bill.keys():
			total+=(self.dict_bill[k]['Price']*self.dict_bill[k]['Quantity'])
		print("The total is ",total)
	def write_to_file(self):
		with open("products.csv",'w') as f1:
			writer=csv.writer(f1)
			writer.writerow(["Product","Price","Quantity"])
			for x in self.dict_bill:
				writer.writerow([self.dict_bill[x]['Name'],self.dict_bill[x]['Price'],self.dict_bill[x]['Quantity']])
	  
obj_pro=products("products.csv")
print("\nEnter 1.To Search for an item \n2.Modify an item details \n3:Delet an item \n4:To add an item")
choice=input()
if choice== 1:
	obj_pro.search_item()
elif choice== 2:
	obj_pro.modify()
elif choice== 3:
	obj_pro.delete()
elif choice==4:
	obj_pro.add()
else :
	print("\nInvalid option")
print("\nThe final List : ")
obj_pro.print_list()
obj_pro.total()
obj_pro.write_to_file()
