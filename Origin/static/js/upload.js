$('#imageUpload').click(function(){ $('#inputImage').trigger('click'); });

function changeImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageUploadChange')
                .attr('src', e.target.result)
                .width(400);
            $('#images-result')
                .style.visibility('none');
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function() {
    $('#upload-image-btn').bind('click', function() {
        var form_data = new FormData($('#upload-form')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                console.log('Success!');
            },
        }).done(function(data) {
            procent = 20;

            var h4 = document.getElementById("h4-similar-logos");
            var br = document.createElement("br");
            h4.innerHTML = 'These are';h4.appendChild(br);h4.innerHTML = h4.innerHTML+'similar';h4.appendChild(br);h4.innerHTML = h4.innerHTML+'logos';


            if(data.result != false){
            $("#img-1").attr('src', data.result[1][2]).width(400);
            $("#h-1").text(data.result[1][0]);
            $("#p-1").text("There are " + data.result[1][5] + " matching features out of a total of " + data.result[1][4] + ".");
            $("#span-1").attr("data-percentage", data.result[1][1]);
            $("#img-match-1").attr("src", "data:image/png;base64,"+data.result[1][3]);
            $("#img-modal-1").attr("src", "data:image/png;base64,"+data.result[1][3]);
            $("#h-modal-1").text(data.result[1][0]);
            $("#p-modal-1").text("There are " + data.result[1][5] + " matching features out of a total of " + data.result[1][4] + ".");
            $("#span-modal-1").attr("data-percentage", data.result[1][1]);

            $("#img-2").attr('src', data.result[2][2]).width(400);
            $("#h-2").text(data.result[2][0]);
            $("#p-2").text("There are " + data.result[2][5] + " matching features out of a total of " + data.result[2][4] + ".");
            $("#span-2").attr("data-percentage", data.result[2][1]);
            $("#img-match-2").attr("src", "data:image/png;base64,"+data.result[2][3]);
            $("#img-modal-2").attr("src", "data:image/png;base64,"+data.result[2][3]);
            $("#h-modal-2").text(data.result[2][0]);
            $("#p-modal-2").text("There are " + data.result[2][5] + " matching features out of a total of " + data.result[2][4] + ".");
            $("#span-modal-2").attr("data-percentage", data.result[2][1]);

            $("#img-3").attr('src', data.result[3][2]).width(400);
            $("#h-3").text(data.result[3][0]);
            $("#p-3").text("There are " + data.result[3][5] + " matching features out of a total of " + data.result[3][4] + ".");
            $("#span-3").attr("data-percentage", data.result[3][1]);
            $("#img-match-3").attr("src", "data:image/png;base64,"+data.result[3][3]);
            $("#img-modal-3").attr("src", "data:image/png;base64,"+data.result[3][3]);
            $("#h-modal-3").text(data.result[3][0]);
            $("#p-modal-3").text("There are " + data.result[3][5] + " matching features out of a total of " + data.result[3][4] + ".");
            $("#span-modal-3").attr("data-percentage", data.result[3][1]);

            $("#img-4").attr('src', data.result[4][2]).width(400);
            $("#h-4").text(data.result[4][0]);
            $("#p-4").text("There are " + data.result[4][5] + " matching features out of a total of " + data.result[4][4] + ".");
            $("#span-4").attr("data-percentage", data.result[4][1]);
            $("#img-match-4").attr("src", "data:image/png;base64,"+data.result[4][3]);
            $("#img-modal-4").attr("src", "data:image/png;base64,"+data.result[4][3]);
            $("#h-modal-4").text(data.result[4][0]);
            $("#p-modal-4").text("There are " + data.result[4][5] + " matching features out of a total of " + data.result[4][4] + ".");
            $("#span-modal-4").attr("data-percentage", data.result[4][1]);

            document.getElementById('li-0').style.display = 'block';
            if (data.result[1][1] > procent) document.getElementById('li-1').style.display = 'block';
            else document.getElementById('li-1').style.display = 'none';
            if (data.result[2][1] > procent) document.getElementById('li-2').style.display = 'block';
            else document.getElementById('li-2').style.display = 'none';
            if (data.result[3][1] > procent) document.getElementById('li-3').style.display = 'block';
            else document.getElementById('li-3').style.display = 'none';
            if (data.result[4][1] > procent) document.getElementById('li-4').style.display = 'block';
            else document.getElementById('li-4').style.display = 'none';
            document.getElementById('li-5').style.display = 'block';
            document.getElementById('ul-0').style.display = 'block';

            if (data.result[1][1] < procent && data.result[2][1] < procent && data.result[3][1] < procent && data.result[4][1] < procent){
            //    document.getElementById('li-1').style.display = 'block';
                h4.innerHTML = 'There are';h4.appendChild(br);h4.innerHTML = h4.innerHTML+'no similar';h4.appendChild(br);h4.innerHTML = h4.innerHTML+'logos';
            }

            $(document).ready(function(){
                $('#bar-1').barfiller();
            });
            $(document).ready(function(){
                $('#bar-2').barfiller();
            });
            $(document).ready(function(){
                $('#bar-3').barfiller();
            });
            $(document).ready(function(){
                $('#bar-4').barfiller();
            });
            }
        });
    });
});

$('#uploadModal1').on('shown.bs.modal', function (e) {
  $(document).ready(function(){
                $('#bar-modal-1').barfiller();
            });
})

$('#uploadModal2').on('shown.bs.modal', function (e) {
  $(document).ready(function(){
                $('#bar-modal-2').barfiller();
            });
})

$('#uploadModal3').on('shown.bs.modal', function (e) {
  $(document).ready(function(){
                $('#bar-modal-3').barfiller();
            });
})

$('#uploadModal4').on('shown.bs.modal', function (e) {
  $(document).ready(function(){
                $('#bar-modal-4').barfiller();
            });
})