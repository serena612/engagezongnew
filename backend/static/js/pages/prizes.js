var selectedPackageId = null;
var selectedCoinsPlan = null;

$(function () {
    //load prizes on page load
    if(location.href.indexOf('#redeem-coins')==-1)
    $(".prize-1-btn").click();

    // scroll to 'buy coins section' when user clicks the buy btn
    $(document).on("click", ".buy-btn", function () {
        $([document.documentElement, document.body]).animate(
            {
                scrollTop: $("#buy-section").offset().top - 200,
            },
            900
        );
    });
});

$(document).on('show.bs.modal', '#redeem-modal', function (e) {
    var relatedTarget = $(e.relatedTarget);

    selectedPackageId = relatedTarget.data('package-id')
    var selectedPackageAmount = relatedTarget.data('package-amount')
    var message = `You need  ${selectedPackageAmount} coins to Redeem. Confirm to proceed?`

    $(e.currentTarget).find('p.message').html(message);
});

$(document).on('show.bs.modal', '#buy-coins-modal', function (e) {
    var relatedTarget = $(e.relatedTarget);

    selectedCoinsPlan = relatedTarget.data('purchase-id')
    var selectedCoinsAmount = relatedTarget.data('purchase-amount')
    var message = `You are about to get ${selectedCoinsAmount} additional coins added to your balance. Press Confirm to proceed.`

    $(e.currentTarget).find('p.message').html(message);
});
$("#purchase-btn").click(function (e) {
    $('.buy-btn').click();
});

$("#redeem-package-btn").click(function (e) {
    setBtnLoading($(this), true);

    $.ajax({
        type: 'POST',
        url: redeem_package_url,
        headers: {
            "X-CSRFToken": xtoken,
        },
        data: {package: selectedPackageId},
        success: function (data) {
            setBtnLoading($("#redeem-package-btn"), false);
            const coins = data.amount;
            const packageName = data.package_name;
            $("#redeem-modal").modal("hide");

            const user_coins = parseInt($("#actual-user-coins").text()) - parseInt(coins);
            $("#actual-user-coins, .user-coins").html(user_coins);

            showInfoModal('Successful', `<p>Congratulations! You have successfully redeemed ${coins} for item ${packageName}</p>`)
            
        },
        error: function (response) {
            setBtnLoading($("#redeem-package-btn"), false);
            var {
                responseText,
                status
            } = response;

            $("#redeem-modal").modal("hide");
            if (status === 406) {
                showPurchaseModal('Not Enough Coins!', `<p>${JSON.parse(responseText).detail}</p>`)
            } else {
                showInfoModal('Error!', '<p>Something went wrong, please try again later.</p>')
            }
            
        }
    })
})

// $("#buy-coins-btn").click(function (e) {
//     setBtnLoading($(this), true);

//     $.ajax({
//         type: 'POST',
//         url: buy_coins_url,
//         headers: {
//             "X-CSRFToken": xtoken,
//         },
//         data: {coins_plan: selectedCoinsPlan},
//         success: function (data) {
//             setBtnLoading($("#buy-coins-btn"), false);
//             const coins = data.amount;
//             $("#buy-coins-modal").modal("hide");

//             const user_coins = parseInt($("#actual-user-coins").text()) + parseInt(coins);
//             $("#actual-user-coins, .user-coins").html(user_coins);

//             showInfoModal('Successful', `<p>Congratulations, ${coins} coins are added to your balance. Your total balance is now ${user_coins}</p>`)
            
//         },
//         error: function (response) {
//             setBtnLoading($("#buy-coins-btn"), false);
//             var {
//                 responseText,
//                 status
//             } = response;

//             $("#buy-coins-modal").modal("hide");
//             if (status === 406) {
//                 showInfoModal('Error!', `<p>${JSON.parse(responseText).detail}</p>`)
//             } else {
//                 showInfoModal('Error!', '<p>Something went wrong, please try again later.</p>')
//             }
            
//         }
//     })
// })
