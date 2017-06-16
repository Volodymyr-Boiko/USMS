/**
 * Created by volodymyr.boiko on 6/15/17.
 */
$(document).ready(function() {
    updateStatus();
});

updateStatus = function(e){
    var statusValue = $("input[name='status']").val();
    $('#post-form option[value=' + '"' + statusValue + '"' + ']').attr('selected','selected');
    var status = $("#status-select :selected").val();
    $.ajax({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val())
        },
        type: 'POST',
        url: $('#status-select').attr('data-url'),
        dataType: 'json',
        data: "status=" + status,
        success: function(data){
            $('#database-status').attr('hidden', 'hidden');
            $('#users-status').attr('hidden', 'hidden');
            $('#status').html('you are on ' + data['status']);
            $('#recieved-status').html(data['status']);
        }
    })
};
