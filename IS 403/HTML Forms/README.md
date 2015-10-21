# HTML Forms

This tutorial about HTML forms will take less than 30 minutes

**This is what a form looks like in HTML.**  

```html
<form action="/Home/Sign_in" method="POST">
	<input name="email" type="email" />
	<input name="password" type="password" />
	<input type="submit" value="Sign in" />
</form>
```

Attribute | Description
--------- | -----------
Action    | Tells the browser where to send the information the user enters into the form
Method    | GET or POST
GET       | Requests data from a specified resource
POST      | Submits data to be processed to a specified resource

This is how we build forms using the Html form helper class
```
@using (Html.BeginForm("Sign_in", "Home", FormMethod.Post))
{
    @Html.TextBox("Email address")
    @Html.Password("Password")
    <button type="submit">Sign in</button>
}
```
We are building a view that displays a sign in form to the user and submits the form data to the Sign_in action in the Home Controller

![picture of complete product](images/finished.png)

## Getting Started

### Download Starter Code

Running the project displays an empty view for us to build our form in

![inital load screen when running the project](images/initial-run.png)

### Build form with HTML Helper

![build form in index.cshtml](images/build-form.png)

add this code to your index.cshtml file

```
@using (Html.BeginForm("Sign_in", "Home", FormMethod.Post))
{
    <label for="inputEmail">Email address</label>
    @Html.TextBox("Email address")
    <label for="inputPassword">Password</label>
    @Html.Password("Password")
    <button type="submit">Sign in</button>
}
```
run your project and your view should now show an ugly form for the user to input an email address and password

![build form in index.cshtml](images/ugly-form.png)

Before this form will work we need to create an action method in our Home Controller to receive this request

### Create Sign_in Action method in controller



