/*  */

var script = document.createElement("script");
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(script);

/*  */

var LanguageList = {
  EN: "English",
  PL: "Polski",
};

// global common phrases

var WORDS_G_EN = {
  login: "Log In",
  logoff: "Log Off",
  register: "Register",
  upload: "Upload",
  logRegSwitch1: "",
  logRegSwitch2: "",
};

var WORDS_G_PL = {
  login: "Zaloguj Się",
  logoff: "Wyloguj Się",
  register: "Zarejestruj Się",
  upload: "Załaduj",
  logRegSwitch1: "",
  logRegSwitch2: "",
};

/*  */

var sessionLang = window.sessionStorage.getItem("sessionLanguage");

/*  */

function loadsLanguage(lang) {
  window.sessionStorage.setItem("sessionLanguage", lang);
  $('span[class^="lang"]').each(function () {
    var LangVar;
    var Text = "???";

    if (this.className.includes("lang-g-")) {
      LangVar = this.className.replace("lang-g-", "");
      Text = window["WORDS_G_" + lang][LangVar];
    } else if (this.className.includes("lang-l-")) {
      LangVar = this.className.replace("lang-l-", "");
      Text = window["WORDS_L_" + lang][LangVar];
    }
    $(this).text(Text.replace(/\n/g, '<br>'));
  });
}

function initialize() {
  var $dropdown = $("#country_select");

  $.each(LanguageList, function (key, value) {
    $dropdown.append($("<option/>").val(key).text(value));
  });

  if (sessionLang === null) {
    loadsLanguage("EN");
    $("#country_select").val("EN");
  } else {
    loadsLanguage(sessionLang);
    $("#country_select").val(sessionLang);
  }
}

/*  */

window.onload = initialize;

/*  */
