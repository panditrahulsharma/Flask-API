	$(document).ready(function(){
		 
		// generate random id

		        function makeid(length) {
				   var result           = '';
				   var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
				   var charactersLength = characters.length;
				   for ( var i = 0; i < length; i++ ) {
				      result += characters.charAt(Math.floor(Math.random() * charactersLength));
				   }
				   return result;
				}


		$.ajax({
			url: '/ajax_get_data',
			success: function(response){

           	var car_data='';

            $.each(response, function (key, data)
             {

             	random_id=makeid(20);

				car_data+='<tr>';
				car_data+='<td>'+data['name']+'</td>';
				car_data+='<td id="'+random_id+'">'+data['length']+'</td>';
				car_data+='<td>'+data['leng']+'</td>';
				car_data+='<td>'+data['upload']+'</td>';
				car_data+='<td >'+data['status']+'</td>';
				car_data+='</tr>';

             	})

				 $('#car_tbody').append(car_data);
			}
		})




	// upload file==================================================================================================================
		    

		    $('#upload-file-btn1').click(function() {

		        var form_data = new FormData();
		        var language=$('#SelectLanguage').val();
		        
				random_id_lenght=makeid(20);
				random_id_status=makeid(20);

		        var ins = document.getElementById('file-upload').files.length;
		        form_data.append("language",language)

		        form_data.append("random_id_lenght",random_id_lenght)
		        form_data.append("random_id_status",random_id_status)
		 
		        for (var x = 0; x < ins; x++) {
		          // alert(document.getElementById('file-upload').files[x].name)
		          var Uploadfilename = document.getElementById('file-upload').files[x].name.replace(/.*(\/|\\)/, '');
		          if (Uploadfilename.length >255)
		          {
		            alert("Upload FileName Should be Less 255");
		            return false
		          }
		          else{
		          form_data.append("files[]", document.getElementById('file-upload').files[x]);
		        }

		        }

				var car_data='';
				car_data+='<tr>';
				car_data+='<td>'+Uploadfilename+'</td>';
				car_data+='<td id="'+random_id_lenght+'">'+"-"+'</td>';
				car_data+='<td>'+language+'</td>';
				car_data+='<td>'+"-"+'</td>';
				car_data+='<td id="'+random_id_status+'">'+"processing..."+'</td>';
				car_data+='</tr>';
				$('#car_tbody').append(car_data);

		        $.ajax({
		            type: 'POST',
		            url: '/uploaFile',
		            data: form_data,
		            contentType: false,
		            cache: false,
		            processData: false,
		            success: function(response) 
		            {


						// var car_data='';
        				$.each(response, function (key, data)
				             {

									document.getElementById(data['random_id_lenght']).innerHTML=data['length'];
									document.getElementById(data['random_id_status']).innerHTML=data['status'];
				             		
				             	})

						// 		 $('#car_tbody').append(car_data);

					console.log("success")

		            },
		        });
		    });
	// end upload file==================================================================================================================






	});
	


