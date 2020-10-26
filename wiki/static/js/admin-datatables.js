// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});
$(document).ready(function($) {
    $("#table-row").click(function() {
        window.document.location = $(this).data("href");
    });
});
