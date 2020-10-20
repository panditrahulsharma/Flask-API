	$(document).ready(function(){

		        function makeid(length) {
				   var result           = '';
				   var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
				   var charactersLength = characters.length;
				   for ( var i = 0; i < length; i++ ) {
				      result += characters.charAt(Math.floor(Math.random() * charactersLength));
				   }
				   return result;
				}

// ==============================================================================================================================


				$(document).on("change", "#textdata", function(){
				    var format = this.value;

						// const format = $('#textdata').val();
						// alert("The text has been changed.="+format);
							// alert(format)
							
				          let data={format:format}

							$('#textdata').val('updating....')

				          $('#result').html('updating...');
				          $.ajax({
				            url:"/ajax_post",
				            type:'post',
				            data:data

				          })
				            .done(function( res )
				            {


				      		if ( res.sucess ) {
								$('#result').html(res.name);
								$('#textdata').val(res.name)
				              }
				              else
				              {
				                $('#error').html(res.error);
				              }
				            });



				});


// ==============================================================================================================================




		$.ajax({
			url: '/ajax_get_data',//calling link when page load here
			success: function(response){

           	var car_data='';

            $.each(response, function (key, data)
             {

             	random_id=makeid(20);

				car_data+='<tr>';
				car_data+='<td ><input type="text" id="textdata" value="'+data['name']+'"></td>';
				car_data+='<td id="'+random_id+'" >'+data['length']+'</td>';
				car_data+='<td >'+data['leng']+'</td>';
				car_data+='<td >'+data['upload']+'</td>';
				car_data+='<td >'+data['status']+'</td>';
				car_data+='</tr>';

             	})

				 $('#car_tbody').append(car_data);
			}
		})

	});
