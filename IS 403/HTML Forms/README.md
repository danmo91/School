# HTML Forms

This tutorial about HTML forms will take 30 minutes or less

**This is what a form looks like in HTML.**  The form's action attribute tells the browser where to send the information the user enters into the form.  The method attribute tells the browser whether to GET data or POST data to/from the server.  The form contains input tags where the user will enter information and submit the form.

```html
<form action="/Home/Sign_in" method="POST">
	<input name="email" type="email" />
	<input name="password" type="password" />
	<input type="submit" value="Sign in" />
</form>
```
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

```
@using (Html.BeginForm("Sign_in", "Home", FormMethod.Post))
{
    @Html.TextBox("Email address")
    @Html.Password("Password")
    <button type="submit">Sign in</button>
}
```




