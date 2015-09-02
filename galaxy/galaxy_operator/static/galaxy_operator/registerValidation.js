/**
 * Created by jlcontreras on 01/09/15.
 */
$.validator.setDefaults({
		submitHandler: function() {
			form.submit();
		}
	});

	$().ready(function() {
		// validate signup form on keyup and submit
		$("#gls-form-register-client-email").validate({
			rules: {
				email: {
					required: true,
					email: true
				},
			},
			messages: {
				email: "Please enter a valid email address"
			}
		});
    });