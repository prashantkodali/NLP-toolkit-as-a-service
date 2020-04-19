$(document).ready(function() {

	$('form#input').on('submit', function(event) {

		$.ajax({
			data : {
				text : $('#text').val()
			},
			type : 'POST',
			url : '/tokenize_call'
		})
		.done(function(data) {
        console.log(data)
				$('textarea#output_text').val(data.output_text);
			}

		});

		event.preventDefault();

	});

});
