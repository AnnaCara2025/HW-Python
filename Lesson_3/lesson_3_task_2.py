from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79101234567"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79209876543"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79305554433"))
catalog.append(Smartphone("Google", "Pixel 8", "+79401112233"))
catalog.append(Smartphone("OnePlus", "11", "+79509998877"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
