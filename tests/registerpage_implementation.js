/* globals gauge*/
"use strict";
const path = require('path');
const {
    alert,
    write,
    goto,
    press,
    toRightOf,
    screenshot,
    click,
    checkBox,
    into,
    textBox,
    button,
} = require('taiko');

gauge.screenshot = async function () {
    const screenshotFilePath = path.join(process.env['gauge_screenshots_dir'],
        `screenshot-${process.hrtime.bigint()}.png`);

    await screenshot({
        path: screenshotFilePath
    });
    return path.basename(screenshotFilePath);
};

step("Open ProfilePrint website", async function () {
    await goto("https://hub.profileprint.ai/auth/register");
});

step("Key in name as <name>", async function (name) {
    await write(name, into(textBox({id:'name'})),{force:true});
});

step("Key in display name as <display_name>", async function (display_name) {
    await write(display_name, into(textBox({id:'display-name'}),{force:true}));
});

step("Key in email as <email>", async function (email) {
    await click('Email', { navigationTimeout: 60000,  force: true })
    await write(email, into(textBox({id:'email'}),{force:true}));
});

step("Key in password as <password>", async function (password) {
    await write(password, into(textBox({id:'password'}),{force:true}));
    await click(button(toRightOf(textBox({id:'password'}))));
});

step("Key in confirm password as <password>", async function (password) {
    await write(password, into(textBox({id:'password-confirm'}),{force:true}));
    await click(button(toRightOf(textBox({id:'password-confirm'}))));
});

step("Key in country as <country>", async function (country) {
    await write(country, into(textBox({id:'country'}),{force:true}));
    await press('Enter');
});

step("Key in country code as <countrycode> and number as <number>", async function (countrycode, number) {
    await write(countrycode, into(textBox({id:'input-124'}),{force:true}));
    await press('Enter');
    await write(number, into(textBox({id:'input-129'}),{force:true}));
});

step("Agree to terms and conditions", async function() {
    await click(checkBox({id:'input-100'}));
});

step("Register profile (success)", async function() {
    await click(button('Register'));
    alert(/^back to homepage*$/, async () => await accept());
    await gauge.screenshot();
});

step("Register profile (pop up)", async function() {
    await click(button('Register'));
    alert(/^close*$/, async () => await accept());
    await gauge.screenshot();
});
