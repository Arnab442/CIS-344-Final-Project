create database restaurant_reservations;
use restaurant_reservations;
CREATE TABLE customers (
CustomerId int not null unique auto_increment,
CustomerName VARCHAR (45) not null,
Contactinfo VARCHAR (200),
Primary Key (CustomerId)
);
INSERT INTO customers (CustomerId, CustomerName, Contactinfo)
VALUES
(1, 'Michael Smith', 'MSmith@gmail.com'),
(2, 'Sahuna James', 'SJames@gmail.com'),
(3, 'Jonathan Mann', 'JMann@gmail.com'),
(4, 'Sandra Keys', 'SKeyes@gmail.com');

CREATE TABLE reservations (
ReservationId int not null unique auto_increment,
CustomerId int not null,
ReservationTime datetime not null,
Numberofguests int not null,
Specialrequests VARCHAR(200),
Primary Key (ReservationId),
Foreign Key (CustomerId) references customers(CustomerId)
);
INSERT INTO reservations (ReservationId, CustomerId, ReservationTime, Numberofguests, Specialrequests)
VALUES
(100, 1, '2024-05-22 14:00:00', 4, 'Ic Sculpture'),
(101, 2, '2024-05-22 17:00:00', 20, 'Birthday Party'),
(102, 3, '2024-05-24 16:00:00', 6, 'Flowers'),
(103, 4, '2024-05-24 11:00:00', 4, 'Romantic Setting With Candles');

CREATE TABLE diningpreferences (
PreferenceId int not null unique auto_increment,
CustomerId int not null,
FavoriteTable VARCHAR (200),
DietaryRestrictions VARCHAR (200),
Primary Key (PreferenceId),
Foreign Key (CustomerId) references customers(CustomerId)
);
INSERT INTO diningpreferences (PreferenceId, CustomerId, FavoriteTable, DietaryRestrictions)
VALUES
(46, 1, 'Short Table', 'Pescatarian'),
(72, 2, 'Long Table', 'Nothing'),
(42, 3, 'Party Table', 'Vegetarian'),
(76, 4, 'Short Table', 'Vegan');

Delimiter //
Create Procedure findreservations(in Customer_ID Int) 
Begin
select * from reservations
Where CustomerId = Customer_ID;
End //

Delimiter //
Create Procedure addspecialrequest(in reservation_ID Int, in requests VARCHAR(255)
)
Begin
Insert into specialrequests (reservationID, requests)
Values (
reservation_ID,
requests
);
End //

Delimiter //
Create Procedure addreservations(
in Customer_ID Int,
in Restaurant_ID Int,
in Reservation_Date Date,
in Reservation_Time Time,
in Number_of_Guests Int
)
Begin
Insert Into reservations (
CustomerId,
RestaurantId,
ReservationDate,
ReservationTime,
Numberofguests
)
Values (
Customer_ID,
Restaurant_ID,
Reservation_Date,
Reservation_Time,
Number_Of_Guests
);
End //
