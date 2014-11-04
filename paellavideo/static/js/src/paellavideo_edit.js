/* Javascript for paellaXBlock. */
function paellaXBlock(runtime, element) {

    function paellaSaved(result) {
        $('.server', element).text();
        $('.video_id', element).text(result.video_id);
        $('.display_name', element).text(result.display_name);
    }

    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.save-button').bind('click', function() {
        var data = {
            'display_name': $(edit_display_name).context.value,
            'server':$(edit_server).context.value,
            'video_id': $(edit_video_id).context.value,
            'trimstart': $(edit_start).context.value,
            'trimend': $(edit_end).context.value

        };

        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'save_paella');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
            } else {
                $('.xblock-editor-error-message', element).html('Error: '+response.message);
                $('.xblock-editor-error-message', element).css('display', 'block');
            }
        });
    });


    $(function ($) {
        /* Here's where you'd do things on page load. */
        /*$('#edit_server option[value="https://media.upv.es/player/?id="]')*/
    });
}

