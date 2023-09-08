import stripe
from flask import Flask, redirect

app = Flask(__name__, static_url_path="", static_folder="public")

stripe.api_key = "" # Your Api key

YOUR_DOMAIN = "http://localhost:5000"


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
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

    return redirect(checkout_session.url, code=303)


if __name__ == '__main__':
    app.run()
