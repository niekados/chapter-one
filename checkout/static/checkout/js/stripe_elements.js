var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
      iconColor: '#171310',
      color: '#171310',
      fontWeight: '500',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      ':-webkit-autofill': {
        color: '#fce883',
      },
      '::placeholder': {
        color: '#aab7c4',
      },
    },
    invalid: {
      iconColor: '#dc3545',
      color: '#dc3545',
    },
  };

var card = elements.create('card', {
    style: style,
    hidePostalCode: true        // Disable postal code input in the card element.
                                // Reason: Use the form's postal code value instead,
                                // preventing Stripe from overriding it with card details.
});
card.mount('#card-element');

// Handle card element validation errors

card.addEventListener('change', function(event){
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
          <span class="icon" role="alert">
            <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `
      $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
      'csrfmiddlewaretoken': csrfToken,
      'client_secret': clientSecret,
      'save_info': saveInfo,
    }
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
          payment_method: {
              card: card,
              billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                  line1: $.trim(form.street_address1.value),
                  line2: $.trim(form.street_address2.value),
                  city: $.trim(form.town_or_city.value),
                  country: $.trim(form.country.value),
                  state: $.trim(form.county.value),
                  postal_code: $.trim(form.postcode.value),
                }
              }
          }
      }).then(function(result) {
          if (result.error) {
              var errorDiv = document.getElementById('card-errors');
              var html = `
                  <span class="icon" role="alert">
                  <i class="fas fa-times"></i>
                  </span>
                  <span>${result.error.message}</span>`;
              $(errorDiv).html(html);
              $('#payment-form').fadeToggle(100);
              $('#loading-overlay').fadeToggle(100);
              card.update({ 'disabled': false});
              $('#submit-button').attr('disabled', false);
          } else {
              if (result.paymentIntent.status === 'succeeded') {
                  form.submit();
              }
          }
      });
    }).fail(function() {
      location.reload();
    })
});