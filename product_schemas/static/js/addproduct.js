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
              let jsondata = response.schema
              //console.log(JSON.parse(jsondata));
              parsedJSON=JSON.parse(jsondata);
              console.log(parsedJSON);
              $('#previewForm').jsonForm(
                  parsedJSON    //response is in json string, parsing into js object.
              );            
          },
          error: function(xhr, status, error) {
          console.error('Error:', error);
          }
  
      });
      }
});


  
$(document).on('submit','#save',function(e){
  e.preventDefault();
  let item=$('#item').val();
  console.log(item);
  let brand= $('#brand').val();
  console.log(brand);
  let price= $('#price').val();
  console.log(price);
  let description= $('#description').val();
  console.log(description);

  let selectedOptions = [];

  // Find the selected option from the form elements
  $('#Form').find('select').each(function() {
    selectedOptions.push($(this).val());
    console.log(selectedOptions);
  });
  let isavailable = true;
});