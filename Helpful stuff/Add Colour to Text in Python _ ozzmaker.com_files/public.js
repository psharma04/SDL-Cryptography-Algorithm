function capitaliseFirstLetter( string ){
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function update_notification_field( reset ){

	"use strict";

	var pid, logged_in, d, has_lic;

	pid = jQuery('.wew-id-for-notify').val();
	logged_in = jQuery('#wew-is-logged-in').val();
	has_lic = jQuery('#wew-has-lic').val();

	if( reset ){

		jQuery('.wew-notification-action_wrapper.variations').html("");
	}
	else{

		if( parseInt(has_lic, 10 ) === 1 ){

			if( logged_in ){
				d = '<button id="wew-submit-email-to-notify" class="add_to_cart_button button logged">' + wew_ajax_object.texts.subscribe + '</button>';
			} else {
				d = '<input type="text" name="wew-email-to-notify" class="wew-email-to-notify" placeholder="' + wew_ajax_object.texts.insert + '" />';
				d += '<button id="wew-submit-email-to-notify" class="add_to_cart_button button">' + wew_ajax_object.texts.subscribe + '</button>';
				d += '<input type="hidden" class="wew-id-for-notify" value="' + pid + '" />';
			}
			d += '<img class="wew-spinner" src="' + wew_ajax_object.spinner + '" />';
		}
		else{

			d = '<strong>' + wew_ajax_object.texts.pending + '</strong>';
		}

		setTimeout( function(){

			jQuery('.wew-notification-action_wrapper.variations').html( d );

		}, 100 );
	}
}

(function ( $ ) {

	"use strict";

	$(function () {

		var $productVariations, $oosType, $oosParent, $waitlistTable, $waitlistTable_checks, $waitlistTable_checks_header;

		$oosType = $.trim( $('#oos-type').val() );

		$oosParent = $('#oos-parentid').length ? $('#oos-parentid').val() : false;

		$('.type-product').on('click', '#wew-submit-email-to-notify', function(){

			var pid, uemail, mesgarea, $loading;

			$loading = $(this).nextAll('img');
			$loading.css('visibility', 'visible');

			if( $(this).parents('tr').length && $oosParent ) {	// Grouped products

				pid = $(this).parents('tr').find('.wew-id-for-notify').val();
				uemail = $.trim( $(this).parents('tr').find('.wew-email-to-notify').val() );
				mesgarea = $(this).parents('tr').find('.wew-notification-action_wrapper');
			}
			else{

				pid = $.trim( $('.wew-id-for-notify').val() );
				uemail = $.trim( $('.wew-email-to-notify').val() );
				mesgarea = $('.wew-notification-action_wrapper');
			}

			jQuery.ajax({
				type: "post",
				url: wew_ajax_object.ajax_url,
				dataType: 'json',
				data: {
					action:'wew_save_to_db_callback',
					pid : pid,
					uemail : uemail,
					is_grouped: $oosType === "grouped" ? 1 : 0,
					parent_id: $oosParent,
					is_variation: $oosType === "variation" || ($oosType === "stock" && $('input[name="variation_id"]').length) ? 1 : 0,
					variation_id: $oosType === "variation" || ($oosType === "stock" && $('input[name="variation_id"]').length) ? parseInt( $('input[name="variation_id"]').val() ) : 0
				},
				success:function(data, textStatus, XMLHttpRequest){

					$loading.css('visibility', 'hidden');

					if( data && ( data.error === false  || ( data.error === true && parseInt( data.code ) === 3 ) ) ){

						mesgarea.html( '<strong>' + data.message + '</strong>' );
					}
					else{

						if( data.message !== undefined ){
							alert( data.message );
						}
					}
				},
				error:function(data, textStatus, XMLHttpRequest){

					$loading.css('visibility', 'hidden');
					console.log('error ajax - save wew');
				}
			});

			return false;
		});

		$('.wew-email-to-notify').keyup(function(event){

			if( event.keyCode === 13 ){

				$('#wew-submit-email-to-notify').click();

				return false;
			}
		});

		if( $('.variations_form').length && $('.variations_form').data('product_variations') ){

			$productVariations = $('.variations_form').data('product_variations');

			$('input[name="variation_id"]').on('change', function(){

				var selectedVal,
					cnt,
					cnnt = 0,
					c,
					productInStock,
					okey,
					varTit = [],
					varDTitle = "";

				selectedVal = parseInt( $(this).val() ) > 0 ? parseInt( $(this).val() ) : false ;

				if( selectedVal ){

					for( cnt = 0; cnt < $productVariations.length; cnt++ ){

						if( parseInt( $productVariations[cnt].variation_id ) === selectedVal ){

							productInStock = $productVariations[cnt].is_in_stock;

							if( productInStock === true && !$productVariations[cnt].backorders_allowed ){

								update_notification_field( true );
							}
							else{

								update_notification_field( false );

							}

						}

					}

				}
				else{

					update_notification_field( true );
				}

			});
		}

		if( $('#author-waitlist-table').length ){

			$waitlistTable = $('#author-waitlist-table');
			$waitlistTable_checks = $waitlistTable.find('tbody .check-column > input');
			$waitlistTable_checks_header = $waitlistTable.find('thead .check-column > input');

			$waitlistTable_checks.removeAttr('checked');
			$waitlistTable_checks_header.removeAttr('checked');
			jQuery('#author_waitlist_unsubscribe').attr( 'disabled', 'disabled' );

			$waitlistTable_checks.on('change', function(){

				var selectedNum = $waitlistTable.find('tbody .check-column > input:checked').length,
					allNum = $waitlistTable.find('tbody .check-column > input').length;

				if( $(this).attr("checked") !== undefined ){

				}
				else{

					$waitlistTable_checks_header.removeAttr('checked');
				}

				if( selectedNum === 0 ){

					jQuery('#author_waitlist_unsubscribe').attr( 'disabled', 'disabled' );
				}
				else{

					if( selectedNum === allNum ){

						$waitlistTable_checks_header.attr( 'checked', 'checked' );
					}

					jQuery('#author_waitlist_unsubscribe').removeAttr( 'disabled' );
				}
			});

			$waitlistTable_checks_header.on('change', function(){

				if( $(this).attr("checked") !== undefined ){

					$waitlistTable_checks.attr('checked', 'checked');
				}
				else{

					$waitlistTable_checks.removeAttr('checked');
				}

				var selectedNum = $waitlistTable.find('tbody .check-column > input:checked').length;

				if( selectedNum === 0 ){

					jQuery('#author_waitlist_unsubscribe').attr( 'disabled', 'disabled' );
				}
				else{

					jQuery('#author_waitlist_unsubscribe').removeAttr( 'disabled' );
				}
			});
		}

	});

}(jQuery));