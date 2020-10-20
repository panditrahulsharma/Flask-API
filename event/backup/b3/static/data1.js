
function onchangefunction(content)
{
	var format = content.value;


	    var id = content.id;
	    alert(id);

      let data={format:format}

		$('#'+id).val('saving...')

      $('#result').html('saving....');
      $.ajax({
        url:"/ajax_post",
        type:'post',
        data:data

      })
        .done(function( res )
        {
  		if ( res.sucess ) {
			$('#result').html('');
			$('#'+id).val(res.name)
          }
          else
          {
            $('#error').html(res.error);
          }
        });


}



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




		$.ajax({
			url: '/ajax_get_data',//calling link when page load here
			success: function(response){

           	var Dashboard_data='';

            $.each(response, function (key, data)
             {

             	random_id=makeid(20);

				Dashboard_data+='<tr>';
				Dashboard_data+='<td ><input type="text" id="'+makeid(10)+'" onchange="onchangefunction(this)" value="'+data['name']+'"></td>';
				Dashboard_data+='<td ><input type="text" id="'+makeid(10)+'" onchange="onchangefunction(this)" value="'+data['length']+'"></td>';
				Dashboard_data+='<td ><input type="text" id="'+makeid(10)+'" onchange="onchangefunction(this)" value="'+data['leng']+'"></td>';
				Dashboard_data+='</tr>';

             	})

				 $('#car_tbody').append(Dashboard_data);
			}
		})

	});
