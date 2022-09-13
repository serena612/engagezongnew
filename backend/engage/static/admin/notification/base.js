(function ($) {
  $(function () {
    var selectTemplateField = $("#id_template");
    var selectActionField = $("#id_action");
    var is_popup = $("#id_is_popup");
    var field_popup = $(".field-is_popup");
    var eventInput = $("#id_event_date");
    var urlInput = $("#id_url");
    var imageInput = $("#id_image");
    var videoInput = $("#id_video");
    var claimInput = $("#id_claim_instantly");

    var eventField = $(".field-event_date");
    var urlField = $(".field-url");
    var imageField = $(".field-image");
    var videoField = $(".field-video");
    var claimField = $(".field-claim_instantly");

    function onSelectAction(value) {
      claimField.show()

      urlField.hide();
      imageField.hide();
      videoField.hide();

      eventInput.empty();
      urlInput.empty();
      imageInput.empty();
      videoInput.empty();
      claimInput.prop('checked', false);

      if (value === "text") {
        urlField.show();
        claimField.hide();
        field_popup.hide();
        is_popup.prop('checked',false);
        $('.field-text label:first-child').html('Text:*')
      } else if (value === "image") {
        imageField.show();
        field_popup.show();
        $('.field-image label:first-child').html('Image:*')
      } else if (value === "video") {
        videoField.show();
        field_popup.show();
        $('.field-video label:first-child').html('Video:*')
      }
    }

    function onSelectTemplate(value) {
      eventField.hide();

      if (value === "event") {
        $('.field-event_date label:first-child').html('Event:*')
        eventField.show();
      }
    }

    // default set text as backend
    if(selectActionField.val() === "image") {
      onSelectAction("image");
    } else if (selectActionField.val() === "video") {
      onSelectAction("video");
    } else {
      onSelectAction("text");
    }
    // template field >> on change value listener
    selectActionField.on("select2:select", function () {
      onSelectAction($(this).val());
    });

    // default set null
    if (selectTemplateField.val() === "event") {
      onSelectTemplate("event");
    } else {
      onSelectTemplate(null);
    }
    // template field >> on change value listener
    selectTemplateField.on("select2:select", function () {
      onSelectTemplate($(this).val());
    });
  });
})(jet.jQuery);
