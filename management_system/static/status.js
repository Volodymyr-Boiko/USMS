/**
 * Created by volodymyr.boiko on 6/15/17.
 */
$(document).ready(function () {
  updateStatus();
  filterByStatus()
});

updateStatus = function () {
  var statusValue = $("input[name='status']").val();
  $('#post-form option[value=' + '"' + statusValue + '"' + ']').attr('selected', 'selected');
  var status = $("#status-select :selected").val();
  $.ajax({
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
    },
    type: 'POST',
    url: $('#status-select').attr('data-url'),
    dataType: 'json',
    data: "status=" + status,
    success: function (data) {
      $('#database-status').attr('hidden', 'hidden');
      $('#users-status').attr('hidden', 'hidden');
      $('#user-status-' + data['user_name']).html('(' + data['status'] + ')');
      $('#status').html('you are on ' + data['status']);
    }
  })
};


filterByStatus = function () {
  var $users = $('.users');
  $users.map(function (el) {
    $users[el].style.display = "inline";
  });
  var status = $("#filter :selected").val();
  $.ajax({
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
    },
    type: 'POST',
    url: $('#filter').attr('data-url'),
    dataType: 'json',
    data: "status=" + status,
    success: function (data) {
      $users.map(function (el) {
        $users[el].style.display = "none";
      });
      for (user in data) {
        if ($('#user-name-' + user).attr('id') == 'user-name-' + user) {
          $('#' + user).css('display', 'inline');
          $('#user-name-' + user).html(user);
          $('#user-status-' + user).html('(' + data[user] + ')');
        }
      }
      console.log(data);
    }
  })
};
