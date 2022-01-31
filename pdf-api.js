function createDocument(invoice_id, tutor_name, tutor_id_number, course_name, total_revenue, tutor_revenue, tax_amount, tutor_payment) {
  var TEMPLATE_ID = '17joW_pxkapj5QTm7Cf-2yrkWMzpQXdntr8pYLGdApA0';  
  var documentId = DriveApp.getFileById(TEMPLATE_ID).makeCopy().getId();
  
  drivedoc = DriveApp.getFileById(documentId);
  drivedoc.setName("Invoice " + invoice_id);
  
  doc = DocumentApp.openById(documentId);
  
  var body = doc.getBody();
  
  body.replaceText('{invoice_id}', invoice_id);
  body.replaceText('{tutor_name}', tutor_name);
  body.replaceText('{tutor_id_number}', tutor_id_number);
  body.replaceText('{course_name}', course_name);
  body.replaceText('{total_revenue}', total_revenue);
  body.replaceText('{tutor_revenue}', tutor_revenue);
  body.replaceText('{tax_amount}', tax_amount);
  body.replaceText('{tutor_payment}', tutor_payment);
  
  drivedoc.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.EDIT);

  return "https://docs.google.com/document/d/" + documentId + "/export?format=pdf";
}

function doGet(e) {
  var invoice_id = e.parameter.invoice_id;
  var tutor_name = e.parameter.tutor_name;
  var tutor_id_number = e.parameter.tutor_id_number;
  var course_name = e.parameter.course_name;
  var total_revenue = e.parameter.total_revenue;
  var tutor_revenue = e.parameter.tutor_revenue;
  var tax_amount = e.parameter.tax_amount;
  var tutor_payment = e.parameter.tutor_payment;
  
  var url = createDocument(invoice_id, tutor_name, tutor_id_number, course_name, total_revenue, tutor_revenue, tax_amount, tutor_payment);
  return ContentService.createTextOutput(url);
}