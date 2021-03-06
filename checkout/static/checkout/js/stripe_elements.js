/* 
    Logic taken from:
    https://stripe.com/docs/payments/integration-builder
    https://stripe.com/docs/payments/accept-a-payment
    https://stripe.com/docs/js/including

    As well as following the code institute lessons on stripe payments
*/

var stripePublickey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublickey);
var elements = stripe.elements();

var style = {
      base: {
        color: "#333333",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "#aab7c4"
        }
      },
      invalid: {
        color: "#D92525",
        fontFamily: 'Arial, sans-serif',
        iconColor: "#D92525"
      }
    };

var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle validation errors on card element
card.on("change", function (event) {
    // Disable Submit button when form is empty
    // document.getElementById("submit-button").disabled = event.empty;
    
    //Show stripe error message in the error div if there is one
    var errorDiv = document.getElementById("card-errors")
    if (event.error) {       
        errorDiv.textContent = event.error.message;
    }
    else {
        errorDiv.textCotent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    // If the client secret was rendered server-side as a data-secret attribute
    // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById("card-errors")
            // Show error to your customer (e.g., insufficient funds)
            console.log(result.error.message);
            errorDiv.textContent = result.error.message;
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
            form.submit();
            // Show a success message to your customer
            // There's a risk of the customer closing the window before callback
            // execution. Set up a webhook or plugin to listen for the
            // payment_intent.succeeded event that handles any business critical
            // post-payment actions.
            }
        }
    });
});