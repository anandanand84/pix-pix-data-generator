const url = 'http://localhost:8000/sample-data-generator.html';
const fs = require('fs');
const viewportWidth = 400;
const viewportHeight = 400;
const CDP = require('chrome-remote-interface');

function loadForScrot(url, tab) {
    return new Promise(async (fulfill, reject) => {
        try {
            console.log(url);
            console.log(tab);
            const client = await CDP({ tab });
            
        } catch (e) {
            console.log(e.message);
        }
    });
}

function delay(duration) {
    return new Promise((fulfill, reject) => {
        setTimeout(fulfill, duration);
    })
}
let i = 1;
async function process(urls) {
    let options = {
        format : 'jpeg',
        quality : 100,
    }
    const tab = await CDP.New();
    const client = await CDP({ tab });
    const { Page, Runtime, Emulation } = client;
    const deviceMetrics = {
        width: viewportWidth,
        height: viewportHeight,
        deviceScaleFactor: 0,
        mobile: false,
        fitWindow: false,
    };
    await Emulation.setDeviceMetricsOverride(deviceMetrics);
    await Emulation.setVisibleSize({width: viewportWidth, height: viewportHeight});

    try {
        while (i < 1000) {
            i++;
            await Page.enable();
            await Page.navigate({ url });
            await CDP.Activate({ id: tab.id });
            await delay(400);
            await Runtime.evaluate({ expression: 'generator.createNoise()' });
            await delay(400);
            const filename2 = `${__dirname}/out/noised/${i}.jpg`;
            const result2 = await Page.captureScreenshot();
            const image2 = Buffer.from(result2.data, 'base64');
            await Runtime.evaluate({ expression: 'generator.clean()' });
            await delay(400);
            const filename = `${__dirname}/out/original/${i}.jpg`;
            const result = await Page.captureScreenshot();
            const image = Buffer.from(result.data, 'base64');
            fs.writeFileSync(filename, image);
            fs.writeFileSync(filename2, image2);
        }
    } catch (err) {
        console.error(err);
    }
    await client.close();
}

process([url]);
