function FormValidation() {
  let productNameInput = document.getElementById('productName');
  productNameInput.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
          handleSubmit(event);
      }
  });
}

function handleSubmit(event) {
  event.preventDefault(); 
  let productName = document.getElementById('productName').value.trim();

  if (!productName) {
      alert('Product name cannot be empty')
      return false;
  }
  if (!/^[a-zA-Z0-9\s]{3,50}$/.test(productName)) {
      alert('Product name must be between 3 and 50 characters!')
      return false;
  }
  $('#productTable').slideToggle();
  $('#add-row-button,#saveButton, #PreviewButton').slideToggle();
  generateTableRows();
}
  
function generateTableRows(cloneRow = false) {
  let tableBody = document.querySelector('#productTable tbody');
  let selectOptions = ['string','number'];
  let dataTypes = ['string', 'select', 'number', 'boolean', 'list', 'string1', 'string2'];
  let stringLimits = {
    'string1': 264,
    'string2': 512,
  };
  if (cloneRow) {
    let firstRow = tableBody.firstElementChild.cloneNode(true);
    firstRow.querySelectorAll('input, select').forEach((element) => {
      if (element.tagName === 'INPUT') {
        if (element.type === 'checkbox') {
          element.checked = false; 
        } else {
          element.value = ''; 
          // Enable the length input field
          if (element.className === 'length-input') {
            element.disabled = false;
          }
        }
      } else if (element.tagName === 'SELECT') {
        element.selectedIndex = 0;  
      }
    });
    tableBody.appendChild(firstRow);
  } else {
    let row = document.createElement('tr');

    for (let j = 0; j < 7; j++) {
      let cell = document.createElement('td');

      if (dataTypes[j] === 'select') {
        let select = document.createElement('select');
        for (let option of selectOptions) {
          let optionElement = document.createElement('option');
          optionElement.value = option;
          optionElement.textContent = option;
          select.appendChild(optionElement);
        }
        
        cell.appendChild(select);
      } else if (dataTypes[j] === 'boolean') {
        let checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        cell.appendChild(checkbox);
      } else if (dataTypes[j] === 'number') {
        let input = document.createElement('input');
        input.type = 'number';
        input.className = 'length-input';
        cell.appendChild(input);
      } else {
        let input = document.createElement('input');
        input.type = 'text';
        if (stringLimits.hasOwnProperty(dataTypes[j])) {
          input.maxLength = stringLimits[dataTypes[j]];
        }
        cell.appendChild(input);
      }
      row.appendChild(cell);
    }
    tableBody.appendChild(row);
  }
  document.getElementById('productTable').style.display = 'block';
}

document.addEventListener('DOMContentLoaded', () => {
  FormValidation();
  document.getElementById('add-row-button').addEventListener('click', () => { generateTableRows(true);});
});

let data = {
  schema: {}
};

function preview_button() {
  let table = document.getElementById("productTable");
  let rows = table.querySelectorAll("tr");
  let schemaName = document.getElementById('productName')?.value.trim();
  let data = {
    schema: {}
  };

  for (let i = 1; i < rows.length; i++) {
    let row = rows[i];
    let cells = row.querySelectorAll("td");
    let fieldName = cells[0].querySelector("input").value;
    let type = cells[1].querySelector("select").value;
    let Values = cells[4].querySelector("input").value.split(",");
    let isRequired = cells[3].querySelector("input").checked;
    let description = cells[6].querySelector("input").value;
    let cssclass = cells[5].querySelector("input").value;
    
    if (data.schema[fieldName] === undefined) {
      data.schema[fieldName] = {
        'type': type,
        'title':fieldName,
        'description': description,
        'htmlClass': cssclass
      };
    }
    if (isRequired) {
      data.schema[fieldName].required = true;
    }
    if (Values.length > 1) {
      data.schema[fieldName].enum = Values;
    } else {
      data.schema[fieldName].default = Values[0];
    }
  }
  return data;

  /*
    console.log(data.schema);
    let jsonData = JSON.stringify(data, null, 2);
    console.log(jsonData);
  */
  };

document.getElementById('ConfigSaveButton').style.display = 'none';


$.ajaxSetup({ 
  beforeSend: function(xhr, settings) {
      function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
              var cookies = document.cookie.split(';');
              for (var i = 0; i < cookies.length; i++) {
                  var cookie = jQuery.trim(cookies[i]);
                  // Does this cookie string begin with the name we want?
                  if (cookie.substring(0, name.length + 1) == (name + '=')) {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break;
                  }
              }
          }
          return cookieValue;
      }
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
          // Only send the token to relative URLs i.e. locally.
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
  } 
});

  
$(document).ready(function() {

  $('#add-row-button, #PreviewButton').hide();
  $('#productTable').hide();
  $(document).on('submit','#productForm',function(e){
    e.preventDefault();
    let productname=$('#productName').val();
    let schema=preview_button();
    let isactive= true;  //default is true, deactivated later by user
    $.ajax({
      type:'POST',
      url: '/configsave/',
      dataType: 'json',
      data: JSON.stringify({
        productname:productname,
        schema:schema,
        isactive:isactive,
      }, null, 2),
    }).done(function(r){
      console.log(r);
      alert(r.message);
    });
  });

  let previewFormDiv=document.getElementById('previewForm');

  $('#PreviewButton').click(function() {
    previewFormDiv.style.display = 'block';
    document.getElementById('ConfigSaveButton').style.display = 'block';
  });

  $(previewFormDiv).html('').jsonForm({
      schema: data.schema,
  });

});
