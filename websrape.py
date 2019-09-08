import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://chaldal.com/powder-mixes') #put the url of webpage

soup = BeautifulSoup(response.text, 'html.parser')

with open('chalDal_Beverage_syrupPowderdrinks','w') as csv_file: # csv file name
	csv_writer = writer(csv_file)
	headers = ['ImageUrl', 'Name','Quantity','Price'] #headers of csv file
	csv_writer.writerow(headers)

	products = soup.find_all(class_='product')

	for product in products:
		image = product.find('img')['src']  # get image source
		name = product.find(class_='name').get_text() #get name from class = name
		quantity = product.find(class_='subText').get_text()
		price = product.find(class_='price').get_text()
		# print(image,name,quantity,price)
		csv_writer.writerow([image,name,quantity,price]) #write row wise data in csv file


