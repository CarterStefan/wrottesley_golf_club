/* 
    Logic taken from:
    https://stripe.com/docs/payments/integration-builder
    https://stripe.com/docs/payments/accept-a-payment
    https://stripe.com/docs/js/including

    As well as following the code institute lessons on stripe payments
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret= $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
      base: {
        color: "#333333",
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "#aab7c4"
        }
      },
      invalid: {
        color: "#D92525",
        iconColor: "#D92525"
      }
    };

var card = elements.create('card', { style: style });
card.mount('#card-element');