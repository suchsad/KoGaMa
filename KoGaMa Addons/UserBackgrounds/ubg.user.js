// ==UserScript==
// @name         Custom Profile Backgrounds
// @version      1.3
// @author       Devork, ⛧ sim
// @description  KoGaMa Custom Profile Background Support.
// @namespace    discord//@simonvhs
// @match        https://www.kogama.com/profile/*
// @run-at       document-start
// @grant        none
// ==/UserScript==

(async function() {
    'use strict';

    console.log("Tampermonkey script started.");

    const waitForElement = async (selector) => {
        while (!document.querySelector(selector)) {
            await new Promise(resolve => requestAnimationFrame(resolve));
        }
        return document.querySelector(selector);
    };

    const InsertBeforeLoad = async () => {
        try {
            const DESCRIPTION_ELEMENT = await waitForElement('div._9smi2 > div.MuiPaper-root._1rJI8.MuiPaper-rounded > div._1aUa_');
            const DESCRIPTION_TEXT = DESCRIPTION_ELEMENT.innerHTML;
            const BACKGROUND_AVATAR = document.querySelector('._33DXe');
            const BACKGROUND_SECTION = document.querySelector('._33DXe');
            const BACKGROUND_REGEXP = /background:\s*(\d+)(?:,\s*filter:\s*(light|dark|blur|none))?;/i;
            const BACKGROUND_DETAILS = BACKGROUND_REGEXP.exec(DESCRIPTION_TEXT);

            if (typeof BACKGROUND_DETAILS == 'object') {
                const gameId = BACKGROUND_DETAILS[1];
                const embedUrl = `https://www.kogama.com/games/play/${gameId}/embed`;
                console.log("Fetched embed URL:", embedUrl);

                const imageSrc = await fetchImageSource(gameId);

                BACKGROUND_AVATAR.style.transition = 'opacity 0.3s ease-in';
                BACKGROUND_AVATAR.style.opacity = '0';

                BACKGROUND_SECTION.style.transition = 'opacity 0.3s ease-in';
                BACKGROUND_SECTION.style.opacity = '0';

                setTimeout(() => {
                    BACKGROUND_AVATAR.style.opacity = '1';
                    BACKGROUND_SECTION.style.opacity = '1';
                }, 1000);

                BACKGROUND_AVATAR.style.backgroundImage = `url(${imageSrc})`;

                switch (BACKGROUND_DETAILS[2]) {
                    case 'blur':
                        BACKGROUND_AVATAR.style.filter = 'none';
                        BACKGROUND_SECTION.style.filter = 'blur(5px)';
                        break;
                    case 'none':
                        BACKGROUND_AVATAR.style.opacity = 'unset';
                        BACKGROUND_AVATAR.style.filter = 'none';
                        BACKGROUND_SECTION.style.backgroundImage = 'none';
                        BACKGROUND_SECTION.style.filter = 'none';
                        break;
                    case 'dark':
                        BACKGROUND_SECTION.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url(${imageSrc})`;
                        break;
                }
            }
        } catch (error) {
            console.error('Error:', error.message);
        }
    };

    async function fetchImageSource(gameId) {
        try {
            const url = `https://www.kogama.com/games/play/${gameId}/embed`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`Failed to fetch. Status: ${response.status}`);
            }

            const htmlText = await response.text();
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = htmlText;

            const imageSrc = tempDiv.querySelector('li.large img').getAttribute('src');
            return imageSrc;
        } catch (error) {
            throw new Error(`Error fetching image source: ${error.message}`);
        }
    }

    InsertBeforeLoad();
})();
