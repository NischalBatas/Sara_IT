/**
 * Sitech
 * HTML template with high-quality content and latest design trends that fit product market for SaaS, App Solutions Promo Campaigns, Development Studios, Digital Marketing Agencies, Startups and other rising internet technology services
 * Exclusively on https://1.envato.market/sitech-html
 *
 * @encoding        UTF-8
 * @version         1.0.0
 * @copyright       (C) 2018 - 2022 Merkulove ( https://merkulov.design/ ). All rights reserved.
 * @license         Envato License https://1.envato.market/KYbje
 * @contributors    Lilith Lamber (winter.rituel@gmail.com)
 * @support         help@merkulov.design
 **/
"use strict";

import Headroom from "headroom.js";
import {validateForm} from "./forms";
import {initModal} from "./modal";

export function drawNav() {
    const header = document.querySelector('.header');
    const menuTrigger = document.querySelector('#headerTrigger');
    const menuWrapper = document.querySelector('.header_nav');

    menuTrigger.addEventListener('click', () => {
        menuTrigger.classList.toggle('active');
        if (menuTrigger.classList.contains('active')) {
            openMenu();
        } else {
            closeMenu();
        }
    })

    function openMenu() {
        menuWrapper.classList.add('active');
        header.classList.add('opened');
        header.classList.add('sticky');
        document.documentElement.classList.add('fixed');
    }

    function closeMenu() {
        menuTrigger.classList.remove('active');
        menuWrapper.classList.remove('active', 'show');
        header.classList.remove('opened');
        document.documentElement.classList.remove('fixed');
    }

    initHeadroom(header);
    setActivePageClass(document.querySelector('.header'));
    setDropdownMenu();

    window.addEventListener('scroll', () => makeNavSticky(header, menuTrigger));
    window.addEventListener('resize', closeMenu);
    window.addEventListener('resize', setDropdownMenu);

    function drawSignUpPopup() {
        const triggerElems = document.querySelectorAll('.signUpTrigger');
        triggerElems.forEach(el => {
            el.addEventListener('click', () => {
                closeMenu();
                initModal({
                    customClass: {
                        container: 'signup_container',
                        htmlContainer: 'signup_wrapper',
                    },
                    html: `
                    <div class="signup_popup-shapes">
                        <img class="speaker" src="svg/speaker.svg" alt="Get Your Free Demo">
                        <div class="group">
                            <img class="oval" src="svg/ovals-line_group.svg" alt="Get Your Free Demo">
                            <img class="shape" src="svg/lineshape.svg" alt="Get Your Free Demo">
                        </div>
                    </div>
                    <div class="signup_popup-header">
                        <h3 class="title">Get Your Free Demo</h3>
                        <h5 class="subtitle">Sign Up to Sitech</h5>
                    </div>
                    <ul class="signup_popup-list d-flex flex-column flex-md-row justify-content-md-center">
                        <li class="list-item">
                            <i class="icon-check icon"></i>
                            No credit card required
                        </li>
                        <li class="list-item">
                            <i class="icon-check icon"></i>
                            14-day free trial
                        </li>
                        <li class="list-item">
                            <i class="icon-check icon"></i>
                            Cancel Anytime
                        </li>
                    </ul>
                    <forms class="signup_popup-forms forms d-flex flex-column" action="#" method="post" data-type="signup">
                        <input class="field required" type="text" placeholder="Name">
                        <input class="field required" type="text" data-type="email" placeholder="E-mail">
                        <input class="field required" type="password" placeholder="Password">
                        <input class="field required" type="password"  placeholder="Confirm Password">
                        <div class="">
                            <input type="checkbox" name="sendDemoCheck" id="sendDemoCheck" checked>
                            <label for="sendDemoCheck">
                                <i class="icon-check icon"></i>
                                send me invite to the free demo by email
                            </label>
                        </div>
                        <button class="btn btn--neon" type="submit">Send</button>
                    </forms>
        `
                }, 'signup_popup')
                validateForm('[data-type="signup"]');
            })
        })
    }

    drawSignUpPopup();
}

// hide header on scroll
function initHeadroom(headerEl) {
    const headroom = new Headroom(headerEl, {
        offset: 500,
        classes: {
            pinned: "header--pinned",
            unpinned: "header--unpinned",
        }
    });
    headroom.init();
}

// set activity class for the current page
function setActivePageClass(headerEl) {
    const menuListItems = document.querySelectorAll('.nav-item');

    menuListItems.forEach((item, i) => {
        if (item.dataset.page === headerEl.dataset.page || item.dataset.mainLink && item.dataset.pageParent === headerEl.dataset.pageParent) {
            item.classList.add('current');
        }
    })

}

// change header on scroll

// dropdown menus (mobile/desktop)
function setDropdownMenu() {
    const dropdownElems = document.querySelectorAll('.dropdown');
    const triggers = document.querySelectorAll('.dropdown-toggle');
    const menuLists = document.querySelectorAll('.dropdown-menu');

    triggers.forEach((el, i) => {

        function closeMenu() {
            el.classList.remove('active');
            menuLists[i].classList.remove('active');
        }

        if (window.innerWidth > 991.98) {
            el.style.pointerEvents = 'default';
            el.dataset.bsToggle = '0';
            menuLists[i].classList.remove('collapse');
            window.addEventListener('resize', closeMenu)
        } else {
            el.dataset.bsToggle = 'collapse';
            menuLists[i].classList.add('collapse');
            el.addEventListener('click', () => {
                el.classList.toggle('active');
                menuLists[i].classList.toggle('active');
            })
            window.addEventListener('resize', closeMenu);
            window.addEventListener('scroll', closeMenu)
        }

    })


    dropdownElems.forEach(el => {

        el.addEventListener('mouseover', function (e) {
            let trigger = this.querySelector('a[data-trigger="dropdown"]');
            let menu = trigger.nextElementSibling;
            trigger.classList.add('active');
            menu.classList.add('active');
        });

        el.addEventListener('mouseleave', function (e) {
            let trigger = this.querySelector('a[data-trigger="dropdown"]');
            let menu = trigger.nextElementSibling;
            trigger.classList.remove('active');
            menu.classList.remove('active');
        })
    })

}

function makeNavSticky(headerEl, triggerEL) {
    if (window.scrollY > 0 || triggerEL.classList.contains('active')) {
        headerEl.classList.add('sticky');

    } else if (!triggerEL.classList.contains('active')) {
        headerEl.classList.remove('sticky');
    }
}

export function scrollToTop() {
    const btn = document.querySelector('#scrollToTop');

    btn.addEventListener('click', () => {
        window.scrollTo(0, 0);
    })
}
