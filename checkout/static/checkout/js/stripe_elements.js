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
        fontSize: "14px",
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
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#submit-button-text').fadeToggle(100);
    $('#loading-spinner').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    }
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        // If the client secret was rendered server-side as a data-secret attribute
        // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address:{
                        line1: $.trim(form.street_address.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value)
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value)
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById("card-errors")
                // Show error to your customer (e.g., insufficient funds)
                errorDiv.textContent = result.error.message;
                $('#payment-form').fadeToggle(100);
                $('#submit-button-text').fadeToggle(100);
                $('#loading-spinner').fadeToggle(100);
                card.update({ 'disabled': false});
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
    }).fail(function () {
        // relaod page, error will appear in django messages
        location.reload();
    })    
});