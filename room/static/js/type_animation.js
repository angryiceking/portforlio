import Typed from '/static/js/typed.js';

$('document').ready(function(){

    var options = {
        strings: ["hi, i'm carl. nice to meet you.", "i work as a software developer.",  "i like sweets.", "i like it simple and minimal.", "i love watching movies.", "i love challenges."],
        typeSpeed: 60,
        loop: !0,
        backDelay: 1500,
    };

    var typed = new Typed('#typed', options);

})