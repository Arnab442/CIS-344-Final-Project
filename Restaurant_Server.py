from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from Restaurant_Database import RestaurantDatabase
import cgi

class RestaurantPortalHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        self.database = RestaurantDatabase()
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_POST(self):
        try:
            if self.path == '/addReservation':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                customer_id = form.getvalue("customer_id")
                reservation_time = form.getvalue("reservation_time")
                number_of_guests = form.getvalue("number_of_guests")
                special_requests = form.getvalue("special_requests")

                if not customer_name or not contact_info or not reservation_time or not number_of_guests.isdigit():
                    self.send_error(400, "Invalid input data")
                    return
                
                number_of_guests = int(number_of_guests)
                
                self.database.addReservation(customer_name, reservation_time, number_of_guests, special_requests)
                print("Reservation added for customer ID:", customer_name)
                
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| <a href='/addReservation'>Add Reservation</a>|                                 <a href='/viewReservations'>View Reservations</a></div>|                                 <a href='/addCustomer'>Add Customer</a></div>                                 ")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservation has been added</h3>")
                self.wfile.write(b"<div><a href='/addReservation'>Add Another Reservation</a></div>")
                self.wfile.write(b"</center></body></html>")
                return

                if not reservation_id or not reservation_id.isdigit():
                    self.send_error(400, "Invalid reservation ID")
                    return

                reservation_id = int(reservation_id)
                #If this works then the website is healthy.

                self.database.deleteReservation(reservation_id)
                print("Reservation deleted with ID:", reservation_id)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(b"<html><head><title>Delete Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h2>Reservation Deleted</h2>")
                self.wfile.write(b"<p>Reservation has been successfully deleted.</p>")
                self.wfile.write(b"<a href='/deleteReservation'>Delete Another Reservation</a><br>")
                self.wfile.write(b"<a href='/viewReservations'>View Reservations</a></center>")
                self.wfile.write(b"</body></html>")
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

        return
    
    def do_GET(self):
        
        try:
            if self.path == '/':
                data=[]
                records = self.database.getAllReservations()
                print(records)
                data=records
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| <a href='/addReservation'>Add Reservation</a>|                                  <a href='/viewReservations'>View Reservations</a></div>")
                self.wfile.write(b"<hr><h2>All Reservations</h2>")
                self.wfile.write(b"<table border=2> <tr><th> Reservation ID </th>                                        <th> Customer ID </th>                                        <th> Reservation Time </th>                                        <th> Number of Guests </th>                                        <th> Special Requests </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            elif self.path == '/addReservation':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(b"<html><head><title>Add Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h2>Add Reservation</h2>")
                self.wfile.write(b"<form method='post' action='/addReservation'>")
                self.wfile.write(b"<label>Customer Name: </label>")
                self.wfile.write(b"<input type='text' name='customer_name' required><br>")
                self.wfile.write(b"<label>Contact Info: </label>")
                self.wfile.write(b"<input type='text' name='contact_info' required><br>")
                self.wfile.write(b"<label>Reservation Time: </label>")
                self.wfile.write(b"<input type='text' name='reservation_time' required><br>")
                self.wfile.write(b"<label>Number of Guests: </label>")
                self.wfile.write(b"<input type='text' name='number_of_guests' required><br>")
                self.wfile.write(b"<label>Special Requests: </label>")
                self.wfile.write(b"<input type='text' name='special_requests'><br>")
                self.wfile.write(b"<input type='submit' value='Submit'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return
            #This is to add information, currently somewhat works.
            
            if self.path =='/addCustomer':
                return
            
            elif self.path == '/deleteReservation':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                self.wfile.write(b"<html><head><title>Delete Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h2>Delete Reservation</h2>")
                self.wfile.write(b"<form method='post' action='/deleteReservation'>")
                self.wfile.write(b"<label>Reservation ID to delete: </label>")
                self.wfile.write(b"<input type='text' name='reservation_id' required><br>")
                self.wfile.write(b"<input type='submit' value='Delete'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/viewReservations':
                reservations = self.database.getAllReservations()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b"<html><head><title>View Reservations</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>View Reservations</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addReservation'>Add Reservation</a>|\
                                  <a href='/deleteReservation'>Delete Reservation</a>|\
                                  <a href='/viewReservations'>View Reservations</a></div>")
                self.wfile.write(b"<hr><h2>All Reservations</h2>")
                self.wfile.write(b"<table border=1>")
                self.wfile.write(b"<tr><th>Reservation ID</th><th>Customer Name</th><th>Contact Info</th><th>Reservation Time</th><th>Number of Guests</th><th>Special Requests</th></tr>")
                
                for row in reservations:
                    self.wfile.write(b"<tr>")
                    for item in row:
                        self.wfile.write(b"<td>")
                        self.wfile.write(str(item).encode())
                        self.wfile.write(b"</td>")
                    self.wfile.write(b"</tr>")
                    
                self.wfile.write(b"</table>")
                self.wfile.write(b"</center></body></html>")
                return

            #This is to delete any reservations, have not tested it yet due to add reservations not working properly.
            if self.path =='/findReservations':
                return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

def run(server_class=HTTPServer, handler_class=RestaurantPortalHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()
