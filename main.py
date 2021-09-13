from covid import covid

covid - covid()

country_list =[]

for each in (covid.list_countries()):
    country_list.append(each['name'])

print("************************")
print(country_list)
print("************************")

country_sel = input("Please enter a country from the list above: ")

print("The covid update for the country " + country_sel)
for key in (covid.get_status_by_country_name(country_sel).keys()):
    print(key +":"+ str(covid.get_status_by_country_name(country_sel)[key]))