def shipping_label(*args, **kwargs): #args before kwargs
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"{kwargs['street']}") #kwargs['street'] is the same as kwargs.get('street')
    if "apt" in kwargs:
        print(f"{kwargs['apt']}")
    print(f"{kwargs['zip']} {kwargs['city']}")
    print(f"{kwargs['state']}, {kwargs['Country']}")

shipping_label("Dr.","Spongebob","Squarepants",
               street="123 Pineapple Lane",
                apt="Apt 1",
               zip="12345",
               city="Bikini Bottom",
               state="Pacific Ocean",
               Country="USA")
