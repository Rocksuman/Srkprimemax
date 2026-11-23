class Script:
    # Start message
    START_TXT = """
<b>Join @SRKPRIMEMAX
Free content, movies, files & services — all in one place.Daily Updates
✅ By SRKSupports ⚡<b>"""

    # Premium information shown in the upgrade menu
    UPGRADE_TEXT = """
<b>
👉 प्रीमियम user के फायदे ✅

1. किसी भी तरह का टोकन नई लेना होगा
2. Direclty मूवी फाइल मिलेगा
3. फास्ट डाउनलोड कर सकते हे
4. ऑनलाइन देख सकते हे
5. किस भी तरह का लिमिट नई आयेगा

6. आपको एक न्यू ग्रुप में add किया जाएगा
7. वहां पर रोज नया मूवी अपलोड किया जाएगा
8. मूवी के directly फाइल ही अपलोड होगे
9. अनलिमिटेड मूवी डाउनलोड कर के देख सकते है
9. कभी कभी फास्ट डाउनलोड लिंक भी मिलेगा

🎁 Premium Plan Cost 📩

💎 ₹060/1 Month | 💎 ₹110/2 Month
💎 ₹155/3 Month | 💎 ₹300/6 Month

पेमेंट का स्क्रीनशॉट यह पर भेजे, फिर आपको प्रीमियम ग्रुप के add किया जाएगा 👇
</b>
"""

    # Premium menu text and buttons
    PREMIUM_TEXT = (
        "**💎 Premium User Benefits:**\n\n"
        "✅ Premium Channel and Group\n"
        "✅ No ads, ever\n"
        "✅ Instant movie files\n"
        "✅ Ai language scanning\n"
        "✅ Chrome Download & Streaming\n"
        "✅ No daily verification required.\n\n"
        "**📩 Premium Plan Cost**\n\n"
        "💠 Plan 1: ₹99 – 1 Month\n"
        "💠 Plan 3: ₹149 – 3 Months\n"
        "💠 Plan 4: ₹269 – 6 Months\n"
        "💠 Plan 5: ₹499 – 12 Months\n\n"
        "<b>📤 After completing the payment, click the button below and send your payment screenshot. Your premium access will be activated shortly.</b>"
    )
    PREMIUM_DEMO_BUTTON = ("📌 Buy Premium ~ Demo Video 📌", "https://t.me/srkmax/11")
    PREMIUM_PLAN_BUTTONS = [
        ("1 Month - ₹99", "phonpeapi_99_30"),
        ("3 Month - ₹149", "phonpeapi_149_90"),
        ("6 Month - ₹269", "phonpeapi_269_180"),
        ("1 Year - ₹499", "phonpeapi_499_365"),
    ]
    PREMIUM_BACK_BUTTON = ("← Back", "home")

    # Payment messages
    CNFRM_TEXT = """
**To Confirm Payment Process, Please Send Your Transaction Screenshot To <a href=https://t.me/PrimiumSupportbot>A D M I N</a>**\n
**Admin little delays may occur, request refund if plan activation fails.\nㅤ**
"""
    PAYMENT_SELECTED_TEXT = (
        "🌟 **Selected Plan Information**\n\n"
        "💰 **Plan Price:** ₹{amount} INR\n"
        "📆 **Duration:** {days} days\n\n"
        "🍁 **Link expires in 10 minutes**"
    )
    PAYMENT_EXPIRED_TEXT = (
        "⚠️ **This order has expired !\n\n"
        "If you've already completed the payment, please click the button below to verify your payment.\n\n"
        "Otherwise, create a <a href='https://telegram.me/{bot_username}?start=upgrade'>new order...</a>**"
    )
    PAYMENT_SUCCESS_TEXT = (
        "🎊 <b>Congratulations {first_name}!</b>\n"
        "✅ <b>Your payment is verified</b>\n\n"
        "🎁 <b>Plan Activated:</b>\n"
        "• 💰 Amount: ₹{amount} INR\n"
        "• ⏳ Valid for: {days} days\n\n"
        "Thank you for joining the SRK Family! ❤‍🩹\n\n"
        "Please send your payment screenshot to the bot. After verification, you will receive access to the Premium Channel and Group. 👇\n\n"
        "🤖 Bot: @SRKPremium_Channel_bot"
    )

    # Premium activation success messages
    ADMIN_PREMIUM_SUCCESS_TEXT = (
        "**⭐ Congratulations** **{name}**\n\n"
        "You’re now a premium member for **{duration} days.**\n"
        "**🗓 Expiry Date:** {expiry_date}\n\n"
        "Use /info to check your premium status."
    )
    CODE_PREMIUM_SUCCESS_TEXT = (
        "✅ Successfully activated premium!\n"
        "👤 User: {user_mention}\n"
        "⏱ Duration: {duration} days\n"
        "📅 Expires: {expiry_date}\n\n"
        "🎉 Enjoy your premium features!"
    )
