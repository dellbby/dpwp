'''
Delia Akbari
August 13, 2015
Simple Form
DPWP
'''

class Page(object):
    def __init__(self): #declaring self
        #start Doctype html code - header, form,result,etc.
    	self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Dellbby Photography - Contact Us</title>
        <link href = "css/style.css" rel="stylesheet" type="text/css"/>
        <center><img src="images/banner.png"></center>
    </head>
    <body>
        """

        self.form = """
        <header>

        <h1>Need a Photographer? Contact us!</h1>

        </header>
        <div class="form"><form method="GET" action="">
        <h2>Fill out our quick contact form:</h2>
        <label>First Name: </label><input type="text" name="fname" /><br>
        <label>Last Name: </label><input type="text" name="lname" /><br>
        <label>Phone Number: </label><input type="text" name="number" /><br>
        <label>City: </label><input type="text" name="city" /><br>
        <label>State:</label><select name="state"><br>
        <option value=" " > Please choose a state</option>
		<option value="AL">Alabama</option>
		<option value="AK">Alaska</option>
		<option value="AZ">Arizona</option>
		<option value="AR">Arkansas</option>
		<option value="CA">California</option>
		<option value="CO">Colorado</option>
		<option value="CT">Connecticut</option>
		<option value="DE">Delaware</option>
		<option value="DC">District Of Columbia</option>
		<option value="FL">Florida</option>
		<option value="GA">Georgia</option>
		<option value="HI">Hawaii</option>
		<option value="ID">Idaho</option>
		<option value="IL">Illinois</option>
		<option value="IN">Indiana</option>
		<option value="IA">Iowa</option>
		<option value="KS">Kansas</option>
		<option value="KY">Kentucky</option>
		<option value="LA">Louisiana</option>
		<option value="ME">Maine</option>
		<option value="MD">Maryland</option>
		<option value="MA">Massachusetts</option>
		<option value="MI">Michigan</option>
		<option value="MN">Minnesota</option>
		<option value="MS">Mississippi</option>
		<option value="MO">Missouri</option>
		<option value="MT">Montana</option>
		<option value="NE">Nebraska</option>
		<option value="NV">Nevada</option>
		<option value="NH">New Hampshire</option>
		<option value="NJ">New Jersey</option>
		<option value="NM">New Mexico</option>
		<option value="NY">New York</option>
		<option value="NC">North Carolina</option>
		<option value="ND">North Dakota</option>
		<option value="OH">Ohio</option>
		<option value="OK">Oklahoma</option>
		<option value="OR">Oregon</option>
		<option value="PA">Pennsylvania</option>
		<option value="RI">Rhode Island</option>
		<option value="SC">South Carolina</option>
		<option value="SD">South Dakota</option>
		<option value="TN">Tennessee</option>
		<option value="TX">Texas</option>
		<option value="UT">Utah</option>
		<option value="VT">Vermont</option>
		<option value="VA">Virginia</option>
		<option value="WA">Washington</option>
		<option value="WV">West Virginia</option>
		<option value="WI">Wisconsin</option>
		<option value="WY">Wyoming</option></select>
        <br><label>Zipcode: </label><input type="text" name="zipcode" /><br>
        <label>Email: </label><input type="text" name="email" /><br>
        <label>Prefered method of contact:</label><input type="radio" name="contact" value="email">Email<br>
        <input type="radio" name="contact" value="phone">Phone<BR><BR>
        <label>Reason:</label><select name="reason"><br>
		<option value=" " >Please choose reason for contact</option>
		<option value="event">Event</option>
		<option value="wedding">Wedding</option>
		<option value="family">Family Portrait</option>
		<option value="baby">Baby Shower</option>
		<option value="engagement">Engagement</option></select>
        <label></label><input type="submit" class="button" value="submit" /></div>
        """

        self.result = """
        <link href = "css/style.css" rel="stylesheet" type="text/css"/>

        <b><h4>Thank you for contacting us! </h4>
        <h2>Below is a confirmation of what you entered.</h2>
        <h2>We should follow up with you shortly.</h2></b> <p> <h3>"""

        self.close = """
        <HR>

        <h3><center><a href=#>Home</a> / <a href=http://www.dellbbyphotography.com/#!portraits/c199t>Portraits</a> / <a href=http://www.dellbbyphotography.com/#!projects/cc5q>Events</a> / <a href=http://www.dellbbyphotography.com/#!blog/c70f>Blog</a> / <a href=#>Contact</a>
    </h3></body>
</html>
        """
