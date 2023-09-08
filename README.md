# Stripe Payment

![](https://images.ctfassets.net/fzn2n1nzq965/6JEjxpwMd1OIIk6RosReNU/3d5c5f5217a7cce4af750ebfe599b6fc/Payments-social-card.png?q=80)

The "Stripe Payment" project demonstrates the seamless integration of the Stripe payment functionality into a Flask web application. Stripe is a widely used online payment processing platform that enables businesses and individuals to securely accept online payments.

With Stripe, users can initiate a checkout session and make subscription payments for products and services. The application provides an intuitive "Checkout" button that redirects users to the Stripe checkout page, where they can enter their payment details securely.

Stripe supports various payment methods, including credit and debit cards, digital wallets, and bank transfers. It handles the complexities of payment processing and ensures that transactions are secure and compliant with industry standards.

The project provides basic templates (checkout.html, success.html, and cancel.html) that users can customize to match their application's design. The "Payment Successful" page (success.html) and "Payment Failed" page (cancel.html) provide users with clear confirmation of their payment status.

This project aims to serve as a starting point for developers looking to implement subscription-based payment systems with Stripe in their Flask applications. It also presents opportunities for future enhancements, such as user authentication, subscription plan management, and automated testing.


## Table Of Contents
 - [Installation](https://github.com/abhisheksingh-17/Stripe-Payment#installation)
 - [Usage](https://github.com/abhisheksingh-17/Stripe-Payment#usage)
 - [Acknowledgements](https://github.com/abhisheksingh-17/Stripe-Payment#acknowledgements)
 - [Technologies Used](https://github.com/abhisheksingh-17/Stripe-Payment#technologies-used)
 - [Code Explanation](https://github.com/abhisheksingh-17/Stripe-Payment#code-explanation)
 - [Screenshots](https://github.com/abhisheksingh-17/Stripe-Payment#screenshots)
 - [Future Scope](https://github.com/abhisheksingh-17/Stripe-Payment#future-scope)
 - [Contributing](https://github.com/abhisheksingh-17/Stripe-Payment#contributing)
 - [License](https://github.com/abhisheksingh-17/Stripe-Payment#license)
## Installation

**1.Clone the repository or download the source code-** https://github.com/abhisheksingh-17/Stripe-Payment.git

**2.Create and activate a virtual environment (optional, but recommended):**

```bash
  python3 -m venv venv

  source venv\Scripts\activate
```
**3.Install the required dependencies:**    
```bash
  pip install -r requirements.txt
```
**4.Set up your Stripe API key:**

Replace "Your api key" in the app.py file with your actual Stripe API key. You can obtain the API key from your Stripe dashboard-https://dashboard.stripe.com/test/apikeys
## Usage

**1.Run the Flask development server:**
```bash
  python app.py
```
**2.Access the application in your web browser:**

Open http://localhost:5000/checkout.html in your web browser to see the home page.

**3.Checkout and make a subscription payment:**

Click the "Checkout" button on the home page to initiate a checkout session. You will be redirected to the Stripe checkout page to enter payment details.

**4.Success and Cancel Pages:**

After completing the payment, you will be redirected to the success page (success.html) if the payment is successful or the cancel page (cancel.html) if the payment is canceled.


## Acknowledgements
I would like to express my sincere gratitude to the following individuals and resources for their valuable contributions and support during the development of this project:

 - Stripe: I am thankful to Stripe for providing an excellent payment processing platform and comprehensive documentation that made integrating payments into this project straightforward.  
https://stripe.com/docs/api

 - Font Awesome: The provided templates utilize Font Awesome icons, adding visual elements to the application and enhancing the user experience.
https://fontawesome.com

 - Open Source Community: I extend my thanks to the open-source community for their contributions to the Flask framework and related libraries, making this project possible.
## Technologies Used

The "Stripe Payment Integration with Flask" project utilizes the following technologies:

 - Flask: Flask is a lightweight web framework for Python, used to build the backend server and handle HTTP requests.

 - Stripe API: The Stripe API provides the payment processing functionality, enabling secure and seamless online payments.

 - HTML & CSS: The frontend of the application is built using HTML for the structure and CSS for styling.

 - Font Awesome: Font Awesome icons are used to enhance the visual elements of the application.

 - Python: The project's backend logic is written in Python, handling the Stripe integration and other server-side operations.

 - Virtual Environment: A virtual environment is used to manage project dependencies and ensure isolation from other Python projects.

 - Git: Git is used for version control and to track changes to the project's codebase.

 - GitHub: GitHub serves as the code repository and collaboration platform for the project.
## Code Explanation

  1.app.py

```python
# Import required modules
import stripe
from flask import Flask, redirect

# Create a Flask application
app = Flask(__name__, static_url_path="", static_folder="public")

# Set the Stripe API key
stripe.api_key = "" # Your Api key 

# Define the base URL for redirecting after payment
YOUR_DOMAIN = "http://localhost:5000"

```
Explanation-

- The code begins by importing the necessary modules: stripe for interacting with the Stripe API and Flask and redirect from the flask package for building the web application.

 - A Flask application object is created, and the static_url_path and static_folder parameters are set. This configuration enables the Flask application to serve static files from the "public" folder.

 - The Stripe API key is set using the stripe.api_key attribute. Replace "my api key" with your actual Stripe API key obtained from the Stripe dashboard.

 - The YOUR_DOMAIN variable is defined, which stores the base URL for redirecting users after successful or canceled payments.

``` python
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        # Create a new Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NPldASGBvo3mDx5SlAdoX0t',
                    'quantity': 1
                }
            ],
            mode="subscription",
            success_url=YOUR_DOMAIN + "/success.html",
            cancel_url=YOUR_DOMAIN + "/cancel.html"
        )

    except Exception as e:
        return str(e)

    # Redirect the user to the Stripe checkout page
    return redirect(checkout_session.url, code=303)

```
Explanation-

 - The create_checkout_session function is a route handler that is triggered when a POST request is made to the /create-checkout-session endpoint.

 - Inside the function, a new Stripe checkout session is created using stripe.checkout.Session.create(...). It specifies the line items for the checkout, in this case, a single item with the given price ID ('price_1NPldASGBvo3mDx5SlAdoX0t') and a quantity of 1.

 - The checkout session's mode is set to "subscription", indicating that it's a subscription-based payment.

 - The success_url and cancel_url parameters define the URLs where Stripe will redirect the user after successful payment or if the payment is canceled. These URLs are concatenated with the YOUR_DOMAIN variable.

 - In case an exception occurs during the creation of the checkout session, the error message is returned as a response.

 - If the checkout session is successfully created, the user is redirected to the Stripe checkout page using redirect(...). The checkout_session.url contains the URL provided by Stripe for the checkout session.
The code begins by importing the necessary modules: stripe for interacting with the Stripe API and Flask and redirect from the flask package for building the web application.

  2.Templates (checkout.html, success.html, cancel.html)

   The provided templates are simple HTML files that  define the frontend layout and content for the  application.

 - checkout.html: This template contains a form with a single "Checkout" button. When users click the button, it initiates the /create-checkout-session POST request to start the Stripe checkout process.

 - success.html: This template displays a "Payment Successful" message and informs the user that their subscription has been successfully established. It uses Font Awesome icons for visual elements.

 - cancel.html: This template displays a "Payment Failed" message and encourages users to revisit the website to complete their purchase if their payment was canceled. It also utilizes Font Awesome icons for visual elements.

  3.Styling (CSS)

 - The CSS styles for the templates are embedded within the <style> tags in each template file.

 - The CSS defines the layout and appearance of the application's elements, including background images, button styles, font sizes, and positioning.

 - The templates use Font Awesome icons via the link to the Font Awesome kit. https://kit.fontawesome.com/92d70a2fd8.js
## Screenshots


 - Home Page-

![](https://github.com/abhisheksingh-17/Stripe-Payment/blob/main/Results/1.png?raw=true)


 - Checkout Page-

![](https://github.com/abhisheksingh-17/Stripe-Payment/blob/main/Results/2.png?raw=true)

![](https://github.com/abhisheksingh-17/Stripe-Payment/blob/main/Results/4.png?raw=true)


 - Payment Successful Page-

![](https://github.com/abhisheksingh-17/Stripe-Payment/blob/main/Results/6.png?raw=true)


 - Payment Failed Page-

![](https://github.com/abhisheksingh-17/Stripe-Payment/blob/main/Results/7.png?raw=true)


 - Payment Dashboard-
 
![](https://github.com/abhisheksingh-17/Stripe-Payment/blob/main/Results/8.png?raw=true)
## Future Scope
The "Stripe Payment" project provides a solid foundation for a subscription-based payment system. Here are some potential areas for future enhancement and expansion:

 - User Authentication-
Currently, the application allows any user to initiate a checkout session. Implementing user authentication and registration will enable personalized subscriptions and better user management.

 - Subscription Plan Management-
Introduce an admin dashboard to manage subscription plans, allowing administrators to create, update, and remove subscription options.

 - Payment History and Invoices-
Include a payment history feature that allows users to view past payments and access/download invoices for their records.

 - Webhooks and Event Handling-
Implement Stripe webhooks to handle events like payment failures, subscription cancellations, and other crucial events to provide users with timely notifications.

 - Secure Deployment-
In a production environment, ensure secure deployment with HTTPS, protect sensitive data, and follow best practices for securing web applications.

 - User Account Management-
Create user profiles where users can manage their account details, update payment methods, and view their subscription status.

 - Subscription Upgrade/Downgrade-
Allow users to upgrade or downgrade their subscription plans easily from within their account.

 - Support for Multiple Payment Gateways-
In addition to Stripe, consider adding support for other payment gateways to provide users with more payment options.

 - Internationalization and Localization-
Extend support for multiple languages and currencies to make the application more accessible to a global audience.

 - Automated Testing-
Implement automated testing to ensure the application's robustness and prevent regressions.
## Contributing

Contributions to the "Stripe Payment" project are welcome and encouraged! If you have any ideas, bug fixes, or enhancements, please follow these steps:

 - Fork the repository on GitHub.

 - Create a new branch for your feature or bug fix: git checkout -b my-feature.

 - Make your changes, commit them, and push the changes to your forked repository.

 - Submit a pull request to the main branch of the original repository.

 - Your pull request will be reviewed by the maintainers, and any necessary feedback will be provided.

 - Once your pull request is approved, it will be merged into the main branch.

Thank you for your contributions!



## License

The "Stripe Payment" project is licensed under the MIT License. See the LICENSE file for more details.
