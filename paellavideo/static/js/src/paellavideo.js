/**
 * Created by leosamu on 29/10/14.
 */
/* Javascript for paellaXBlock. */
function paellaXBlock(runtime, element) {

    console.log($("iframe",element)[0]);

    $($("iframe",element)[0]).on('load',function(){
        setTimeout(function(){
            start = $("[name='trimstart']")[0].value;
            end = $("[name='trimend']")[0].value;
            if (start < end && end>0){
                $("iframe",element)[0].contentWindow.postMessage({event:'paella:settrim',params:{trimEnabled:true,trimStart:start,trimEnd:end}},"http://paellaplayer.upv.es");
            }

        }, 300);

    });


    $(function ($) {
        /* Here's where you'd do things on page load. */
        /*$('#edit_server option[value="https://media.upv.es/player/?id="]')*/

        //document.getElementById("paella").contentWindow.postMessage({event:'paella:settrim',params:{trimEnabled:true,trimStart:20,trimEnd:30}},"http://paellaplayer.upv.es");

    });

}

