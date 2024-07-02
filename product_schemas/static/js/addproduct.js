let parsedJSON;// making the schema of form available globally

//loading form of product when opened
$(document).ready(function() {
  let urlParams = new URLSearchParams(window.location.search);
  let id = urlParams.get('id');
  if (id) {
    $.ajax({
        type: "GET",
        url:`/product_schemas/?id=${id}&source=addproduct`,
        data:{},
        success: function(response) {
            let jsondata = response.schema;
            parsedJSON=JSON.parse(jsondata);
            //console.log(parsedJSON);
            $('#previewForm').jsonForm(parsedJSON); //response is in json string, parsing into js object.                                            
        },
        error: function(xhr, status, error) {
        console.error('Error:', error);
        }
    });
    }
});
