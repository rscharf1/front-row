console.log("hey")

$(document).ready(function () {
    $("#submit").click(function (){
        console.log("call python script")

        $.ajax({
            type: "POST",
            url: "../../test.py",
            // data: { "a": 5}
          }).done(function( o ) {
              console.log(o)
             // do something
          });
    });
});
