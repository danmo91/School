#!/user/bin/env python3

#initialize django

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()


#regular imports

import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess, sys


#empty (or drop) db

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")

#create db

cursor.execute("CREATE SCHEMA PUBLIC")

#Migrage db

subprocess.call([sys.executable, "manage.py", "migrate"])

#initialize tables

####################################### Groups #######################################

#Delete old groups

Group.objects.all().delete()

#Create new groups, Admin, Manager, Guest
for data in [
  ['Admin'],
  ['Manager'],
  ['Guest'],
]:

    #create group, set name
    g = Group()
    g.name = data[0]

    #save
    g.save()


####################################### Permission #######################################

permissions = Permission.objects.all()

# Give admin permission

for p in permissions:
    g = Group.objects.get(name="Admin")
    g.permissions.add(p)

    g.save()

for p in permissions:
    g = Group.objects.get(name="Manager")

    #if permission is in the right range, then add to group
    if p.id > 15:
        g.permissions.add(p)

    g.save()


####################################### User #######################################

#Delete old users
hmod.User.objects.all().delete()

#Create new users: username, password, first_name, last_name, is_superuser, group, full_name, email
for data in [
  ['danmo91', 'password', 'Dan', 'Morain', True, True, 'Admin', 'Dan Morain', 'dan.morain91@gmail.com'],
  ['mojok13', 'password', 'Morgs', 'Kap', False, True, 'Manager', 'Morgs Kap', 'mojo@gmail.com'],
  ['breezy', 'password', 'Bri', 'Sor', False, False, 'Guest', 'Bri Sor', 'breezy@gmail.com'],
  ['urge', 'password', 'Rj', 'Smith', False, False, 'Guest', 'Rj Smith', 'urge@gmail.com'],
]:

    #set attributes
    u = hmod.User()
    u.username = data[0]
    u.set_password(data[1])
    u.first_name = data[2]
    u.last_name = data[3]
    u.is_superuser = data[4]
    u.is_staff = data[5]
    u.full_name = data[7]
    u.account_balance = 0.00
    u.email = data[8]

    #save
    u.save()

    # Add user to group
    g = Group.objects.get(name=data[6])
    u.groups.add(g)

####################################### Venue #######################################

# Delete old Venue
hmod.Venue.objects.all().delete()

#Create new venue
for data in [
  ['Glen Canyon Park', 'Canyon Park', 'Provo Canyon Drive', 'Provo', 'UT', '84604'],
  ['Scera Shell Theatre', 'Theatre', '123 State Street', 'Orem', 'UT', '84606'],
  ['Brigham Young University', 'University', '456 University Ave', 'Provo', 'UT', '84606'],
  ['Utah Valley Convention Center', 'Convention Center', '432 Center Street', 'Provo', 'UT', '84604'],
]:

    v = hmod.Venue()


    # set attributes
    v.name = data[0]
    v.description = data[1]
    v.street = data[2]
    v.city = data[3]
    v.state = data[4]
    v.zip_code = data[5]

    #save
    v.save()


####################################### event #######################################

#Delete old events
hmod.Event.objects.all().delete()

#Create new events: name, description, start, end, venue
for data in [
  ['Colonial Heritage Festival','Come enjoy a night out at the park with friends and family.','2015-04-06','2015-04-07','1'],
  ['Event Volunteer Reunion','Meet up with volunteer old friends and make some new ones.','2015-03-12','2015-03-12','2'],
  ['Childrens Day Festival','Bring your children to a fun night out at the fair.','2015-02-28','2015-02-28','3'],
  ['Revolutionary Reenactment','Practice up! This is sure to be an eventful night.','2015-05-05','2015-05-05','4'],
]:

    #set attributes
    e = hmod.Event()
    e.name = data[0]
    e.description = data[1]
    e.start = data[2]
    e.end = data[3]
    e.venue = hmod.Venue.objects.get(id=data[4])

    #save
    e.save()

####################################### Area #######################################

# Delete old Area
hmod.Area.objects.all().delete()

#Create new Area
for data in [
  ['Candle Shop', 'Purchase or make candles!', '1', '1'],
  ['Sewing Area', 'Purchase or learn to sew clothing!', '2', '1'],
  ['Crafting', 'Make crafts with your kids!', '3', '3'],
  ['Beadery', 'Make beaded necklaces!', '4', '3'],
  ['Lunch Area', 'Purchase or make candles!', '1', '1'],
  ['Cooking', 'Purchase or learn to sew clothing!', '2', '1'],
  ['Games', 'Make crafts with your kids!', '3', '3'],
  ['Sewing Area', 'Purchase or learn to sew clothing!', '2', '3'],
]:

    a = hmod.Area()

    # set attributes
    a.name = data[0]
    a.description = data[1]
    a.venue = hmod.Venue.objects.get(id=data[2])
    a.event = hmod.Event.objects.get(id=data[3])

    #save
    a.save()

####################################### Items #######################################

#Delete old items
hmod.Item.objects.all().delete()

#Create new items: name, description, value, rental_price
for data in [
  ['Breeches', 'Excellent quality colonial breeches made from the finest materials.', '55.00', '10.00'],
  ['Tricorne', 'This colonial tricorne adds the finishing touches to any costume.', '49.00', '7.00'],
  ['Spectacles', 'People will think you are Ben Franklin himself in these spectacles.' , '211.00', '4.00'],
  ['Almanac', 'This exact replica of Poor Richards Alamanac is in pristine condition.', '80.00', '9.00'],
]:

    i = hmod.Item()
    i.name = data[0]
    i.description = data[1]
    i.value = data[2]
    i.rental_price = data[3]

    i.save()



####################################### Products #######################################

#Delete old Products
hmod.Product.objects.all().delete()

#Create new Products: name, description, category, current_price
for data in [
  ['Ribbon Candy', 'Delicious ribbon candy just like back in the good old days.', 'Candy', '8.00'],
  ['Canvas Pack', 'Perfect for carrying all of your favorite colonial items.', 'Accesories', '54.00'],
  ['Colonial Flag', 'This exact replica of the colonial flag makes for great gift.' , 'Decorations', '17.00'],
  ['Brass Candlesticks', 'Beautiful brass candlesticks to hold your beeswax candles.', 'Decorations', '27.00'],

]:

    p = hmod.Product()
    p.name = data[0]
    p.description = data[1]
    p.category = data[2]
    p.current_price = data[3]

    p.save()

####################################### Products #######################################

#Delete old Area_Items
hmod.Area_Item.objects.all().delete()

#Create new Area_Items: name, description, price, area
for data in [
  ['Stick Horse', 'Stick horse for children.', '2.00', '3'],
  ['Dolls', 'Perfect doll for your daughter.', '18.00', '3'],
  ['Candle Snuffer', 'This a great snuffer for your candle.' , '8.00', '1'],
  ['Beeswax Candles', 'Beautiful beeswax candles.', '3.00', '1'],
  ['Necklace', 'Beautiful necklaces.', '7.00', '4'],
  ['Bracelet', 'Amazing bracelets.', '4.00', '4'],
  ['Spools of Yarn', 'Many colors of yarn for your projects.', '3.00', '2'],
  ['Loom', 'Loom to help you sew.', '9.00', '2'],
  ['Spools of Yarn', 'Many colors of yarn for your projects.', '3.00', '8'],
  ['Loom', 'Loom to help you sew.', '9.00', '8'],
  ['Corn on the cob', 'Delicious corn, homemade.', '1.50', '5'],
  ['Tea', 'Delicious tea for your lunch break.', '1.00', '5'],
  ['Bread', 'Buy some bread after we teach you how to make it the old fashioned way.', '4.00', '6'],
  ['Jam', 'Delicious jam for your bread.', '6.00', '6'],
  ['Stick and Hoop', 'Fun stick and hoop for your child.', '6.00', '7'],
  ['Stick Pull', 'Fun stick game for your child.', '3.00', '7'],
]:

    ai = hmod.Area_Item()
    ai.name = data[0]
    ai.description = data[1]
    ai.price = data[2]
    ai.area = hmod.Area.objects.get(id=data[3])

    ai.save()


####################################### Rentals #######################################

#Delete old Rentals
hmod.Rental.objects.all().delete()

#Create new Rentals: description,rental_date,due_date, user
for data in [
  # under 30
  ['Breeches', '2015-03-06', '2014-03-06', '1'],
  ['Tricorne', '2015-03-06', '2015-03-06', '1'],
  ['Spectacles', '2015-03-06', '2015-03-06', '1'],
  ['Almanac', '2015-03-06', '2015-03-06', '1'],
  # over 30
  ['Spectacles', '2015-03-06', '2015-03-01', '1'],
  ['Tricorne', '2015-03-06', '2015-03-01', '1'],
  ['Breeches', '2015-03-06', '2015-03-01', '1'],
  ['Almanac', '2015-03-06', '2015-03-01', '1'],
  # over 60
  ['Tricorne', '2015-03-06', '2015-02-01', '1'],
  ['Almanac', '2015-03-06', '2015-02-01', '1'],
  ['Breeches', '2015-03-06', '2015-02-01', '1'],
  ['Spectacles', '2015-03-06', '2015-02-01', '1'],
  # over 90
  ['Almanac', '2015-03-06', '2015-01-01', '1'],
  ['Breeches', '2015-03-06', '2015-01-01', '1'],
  ['Spectacles', '2015-03-06', '2015-01-01', '1'],
  ['Tricorne', '2015-03-06', '2015-01-01', '1'],

]:

    r= hmod.Rental()
    r.description = data[0]
    r.rental_date = data[1]
    r.due_date = data[2]
    user = hmod.User.objects.get(id=data[3])
    r.user = user

    print('Rental:', r)

    r.save()

####################################### Orders #######################################

#Delete old Orders
hmod.Order.objects.all().delete()

#Create new Rentals: order_date, total, user
for data in [
  ['2015-03-06', '20.22', '1'],
  ['2015-03-06', '30.33', '2'],
  ['2015-03-06', '40.44', '3'],
  ['2015-03-06', '50.55', '4'],

]:

    o = hmod.Order()
    o.order_date = data[0]
    o.total = data[1]

    user = hmod.User.objects.get(id=data[2])

    o.user = user

    o.save()
