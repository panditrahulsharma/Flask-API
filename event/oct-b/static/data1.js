
function onchangefunction(content)
{
	var new_value = content.value;


	    var new_id = content.id;
	    alert("new value="+new_value);

	    // now replce new id to old id and get original value

	    old_id=new_id.replace('change','old')
		alert('new_id='+new_id)
	    alert('old_id='+old_id)
	    //now get original data
	    old_value = $('#'+old_id).val(); 
	    alert("old value="+old_value)

      	let data={new_value:new_value}

		$('#'+new_id).val('saving...')

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
			$('#'+new_id).val(res.name)
			$('#'+old_id).val(res.name)
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

             	random_id_start=makeid(20);
             	random_id_end=makeid(20);
             	random_id_text=makeid(20);


				Dashboard_data+='<tr>';
				Dashboard_data+='<td ><input type="text" id="'+random_id_start+'change" onchange="onchangefunction(this)" value="'+data['name']+'"></td>';
				Dashboard_data+='<td ><input type="hidden" id="'+random_id_start+'old" value="'+data['name']+'"></td>';

				Dashboard_data+='<td ><input type="text" id="'+random_id_end+'" onchange="onchangefunction(this)" value="'+data['length']+'"></td>';
				Dashboard_data+='<td ><input type="hidden" id="'+random_id_end+'old" value="'+data['length']+'"></td>';

				Dashboard_data+='<td ><input type="text" id="'+random_id_text+'" onchange="onchangefunction(this)" value="'+data['leng']+'"></td>';
				Dashboard_data+='<td ><input type="hidden" id="'+random_id_text+'old" value="'+data['leng']+'"></td>';

				Dashboard_data+='</tr>';

             	})

				 $('#car_tbody').append(Dashboard_data);
			}
		})

	});
