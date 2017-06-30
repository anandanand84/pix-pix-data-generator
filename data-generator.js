const url = 'http://localhost:9527/sample-data-generator.html';
const fs = require('fs');

const CDP = require('chrome-remote-interface');

function loadForScrot(url) {
    return new Promise(async (fulfill, reject) => {
        const tab = await CDP.New();
        const client = await CDP({tab});
        const {Page} = client;
        Page.loadEventFired(() => {
            fulfill({client, tab});
        });
        await Page.enable();
        await Page.navigate({url});
    });
}

function delay(duration) {
    return new Promise((fulfill, reject) => {
        setTimeout(fullfill, duration);
    })
}

async function process(urls) {
    try {
        const handlers = await Promise.all(urls.map(loadForScrot));
        for (const {client, tab} of handlers) {
            const {Page} = client;
            await CDP.Activate({id: tab.id});
            await delay(400);
            const filename = `/tmp/scrot_${tab.id}.png`;
            const result = await Page.captureScreenshot();
            const image = Buffer.from(result.data, 'base64');
            fs.writeFileSync(filename, image);
            console.log(filename);
            await client.close();
        }
    } catch (err) {
        console.error(err);
    }
}

process([url,
         url,
         url,
         url,
         url,
         url,
         url,
         url]);
