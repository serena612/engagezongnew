var times = 0;
function CheckStatus(data) {

    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/api/auth/reload_data/',
            
            headers: {
                "X-CSRFToken": xtoken,
            },
            type: "post",
            data: {
                msisdn: data.msisdn,
                idnetwork: data.idnetwork
                //csrfmiddlewaretoken: '{{ csrf_token }}' //data.csrfmiddlewaretoken
            },
            error: function (value) {
                reject(value);
            },
            success: function (value) {
                resolve(value);
            },
        });
    });
}

function keepUpdated() {
    times += 1;
    console.log("times = "+times);
    if (times>50)
        return;
    // console.log("Updating using token "+xtoken);
    data = {}
    data.msisdn = $(".user_mobile").text();
    // important must add header check here
    data.idnetwork = '1';
    response_msg = $('.sub_status');
    CheckStatus(data).then(res => {
        //setBtnLoading(btn, false);
        //$(".login-otp-form").show();
        response_msg.html("Subscription Success !").show();
        window.location.href = '/clear'
    }).catch(e => {
        if(e.status==472) //406 ?
        response_msg.html('The number you have provided is invalid!').show();
        else if(e.status==475)
        response_msg.html('Subscription Request pending...').show();
        else if(e.status==476)
        response_msg.html('Unsubscription Request pending...').show();
        else if(e.status==456)
        response_msg.html('Profile Creation pending...').show();
        else
        response_msg.html('Unkown error! Please contact the site administrator. '+e.status).show();
        //setBtnLoading(btn, false); 
        setTimeout(keepUpdated, 5000);
    });
    //setTimeout(keepUpdated(), 5000);
}
setTimeout(keepUpdated, 5000);