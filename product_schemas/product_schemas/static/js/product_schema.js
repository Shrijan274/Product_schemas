function FormValidation() {
  var productNameInput = document.getElementById('productName');
  productNameInput.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
          handleSubmit(event);
      }
  });
}

function handleSubmit(event) {
  event.preventDefault(); 
  var productName = document.getElementById('productName').value.trim();

  if (!productName) {
      alert('Product name cannot be empty')
      return false;
  }
  if (!/^[a-zA-Z0-9\s]{3,50}$/.test(productName)) {
      alert('Product name must be between 3 and 50 characters!')
      return false;
  }
  $('#productTable').slideToggle();
  $('#add-row-button,#saveButton, #previewButton').slideToggle();
  generateTableRows();
}
  
function generateTableRows(cloneRow = false) {
  var tableBody = document.querySelector('#productTable tbody');
  var selectOptions = ['string','number'];
  var dataTypes = ['string', 'select', 'number', 'boolean', 'list', 'string1', 'string2'];
  var stringLimits = {
    'string1': 264,
    'string2': 512,
  };
  if (cloneRow) {
    var firstRow = tableBody.firstElementChild.cloneNode(true);
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
    var row = document.createElement('tr');

    for (var j = 0; j < 7; j++) {
      var cell = document.createElement('td');

      if (dataTypes[j] === 'select') {
        var select = document.createElement('select');
        for (var option of selectOptions) {
          var optionElement = document.createElement('option');
          optionElement.value = option;
          optionElement.textContent = option;
          select.appendChild(optionElement);
        }
        
        cell.appendChild(select);
      } else if (dataTypes[j] === 'boolean') {
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        cell.appendChild(checkbox);
      } else if (dataTypes[j] === 'number') {
        var input = document.createElement('input');
        input.type = 'number';
        input.className = 'length-input';
        cell.appendChild(input);
      } else {
        var input = document.createElement('input');
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

 
function previewButton() {
  var table = document.getElementById("productTable");
  var rows = table.querySelectorAll("tr");
  var schemaName = document.getElementById('productName')?.value.trim();
  var data = {
    schema: {}
  };

  for (var i = 1; i < rows.length; i++) {
    var row = rows[i];
    var cells = row.querySelectorAll("td");
    var fieldName = cells[0].querySelector("input").value;
    var type = cells[1].querySelector("select").value;
    var Values = cells[4].querySelector("input").value.split(",");
    var isRequired = cells[3].querySelector("input").checked;
    var description = cells[6].querySelector("input").value;
    var cssclass = cells[5].querySelector("input").value;
     

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
  console.log(data.schema);
  var jsonData = JSON.stringify(data, null, 2);
  console.log(jsonData);

  var previewFormDiv=document.getElementById('previewForm');


  $('#previewButton').click(function() {
    previewFormDiv.style.display = 'block';
    document.getElementById('configSaveButton').style.display = 'block';
});

  $(previewFormDiv).html('').jsonForm({
      schema: data.schema,
  });
}
document.getElementById('configSaveButton').style.display = 'none';

  function configSaveButton() {
    //
  }
  
$(document).ready(function() {
  $('#add-row-button, #previewButton').hide();
  $('#productTable').hide();
});