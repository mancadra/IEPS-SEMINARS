from lxml import html
import re

html_content = """
<html>
  <body>
    <div class="article">
      <h2>Sample Article</h2>
      <p>This is a test paragraph.</p>
    </div>
  </body>
</html>
"""

html_c = """
<html lang="sl"><!-- InstanceBegin template="/Templates/ogrodje3.dwt.asp" codeOutsideHTMLIsLocked="false" --><head>
<meta charset="utf-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

/* Raleway Light */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  src: url('/fonts/Raleway-Light.woff2') format('woff2');
  font-display: swap;
}

/* Raleway Regular */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 400;
  src: url('/fonts/Raleway-Regular.woff2') format('woff2');
  font-display: swap;
}

/* Raleway Italic */
@font-face {
  font-family: 'Raleway';
  font-style: italic;
  font-weight: 400;
  src: url('/fonts/Raleway-Italic.woff2') format('woff2');
  font-display: swap;
}

/* Raleway SemiBold */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 600;
  src: url('/fonts/Raleway-SemiBold.woff2') format('woff2');
  font-display: swap;
}

</style>

<link href="/css/normalize.css" rel="stylesheet" type="text/css">
<link href="/css/skupaj-css.css?rel=4.0502524229335" rel="stylesheet" type="text/css">
<link href="/stiliprint.css" rel="stylesheet" type="text/css" media="print">


<link rel="stylesheet" href="/css/flickity.css" media="screen">

<script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202504010101/show_ads_impl_with_ama_fy2021.js?client=ca-pub-3352501607232481&amp;plah=www.kulinarika.net"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/plugins/ua/linkid.js"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script src="/js/lazysizes.min.js" async=""></script>
<link href="/css/new-responsive.css?v=1.03" rel="stylesheet" type="text/css">

<link rel="apple-touch-icon" sizes="180x180" href="/grafika6/favicons/apple-touch-icon.png">
<link rel="icon" type="image/png" href="/grafika6/favicons/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/grafika6/favicons/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="/grafika6/favicons/manifest.json">
<link rel="mask-icon" href="/grafika6/favicons/safari-pinned-tab.svg" color="#5bbad5">
<link rel="shortcut icon" href="/grafika6/favicons/favicon.ico">
<meta name="msapplication-config" content="/grafika6/favicons/browserconfig.xml">
<meta name="theme-color" content="#ffffff">

<meta property="og:locale" content="sl_SI">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kulinarika.net">
<meta property="fb:app_id" content="182018238801081">





<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "WebSite",
  "name": "Kulinarika.net",
  "url": "http://www.kulinarika.net",
  "image": "http://www.kulinarika.net/grafika6/logotipi/logo4.png",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.kulinarika.net/iskanje/?splosno_besede={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}

</script>

<link href="/css/recepti.css?v=4.0502524229335" rel="stylesheet" type="text/css">
<!-- InstanceBeginEditable name="stili" -->

<!-- InstanceEndEditable -->


<script>

	

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-15823371-4', {'storage': 'none', 'clientId': 'c9993b1a8e5f8da0d8b8de4e2140076d'});
  ga('require', 'linkid', 'linkid.js');
  ga('require', 'displayfeatures');

	
	// Creates an adblock detection plugin.
	ga('provide', 'adblockTracker', function(tracker, opts) {
	  var ad = document.createElement('ins');
	  ad.className = 'AdSense';
	  ad.style.display = 'block';
	  ad.style.position = 'absolute';
	  ad.style.top = '-1px';
	  ad.style.height = '1px';
	  document.body.appendChild(ad);
	  tracker.set('dimension' + opts.dimensionIndex, !ad.clientHeight);
	  document.body.removeChild(ad);
	});
	
	ga('require', 'adblockTracker', {dimensionIndex: 1});
    ga('send', 'pageview'), {'anonymizeIp': true};
  

</script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-3MTV8XXHPL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3MTV8XXHPL');
</script>

<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>

<script src="https://code.jquery.com/jquery-migrate-3.4.0.min.js" integrity="sha256-mBCu5+bVfYzOqpYyK4jm30ZxAZRomuErKEFJFIyrwvM=" crossorigin="anonymous"></script>

<!--    -->



<script data-ad-client="ca-pub-3352501607232481" async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" data-checked-head="true"></script>

<script>




$(function(){
	$('#menu .main-menu #menu02').addClass("selected");
	
		if (!isMobile) {
			$( "#zid-include" ).load( "/inc/ajax-funkcije.asp?akcija=zid-include&Menu=0202&sponzor=0", function() {
			console.log( "Load was performed." );
			});
		}
	
	$('.mobileslider').css('visibility', 'visible');
	
	enquire.register("screen and (max-width: 768px)", {
    match : function() {
		
		

		 
    },
	
	 unmatch : function() {

	  

 		}
	});
	
	
})

  $(window).on('load resize', function() {


	$(".spinner-container").delay(100).fadeOut(600).remove();
	
	
	
})

jQuery.uaMatch = function( ua ) {
        ua = ua.toLowerCase();

        var match = /(chrome)[ /]([w.]+)/.exec( ua ) ||
                /(webkit)[ /]([w.]+)/.exec( ua ) ||
                /(opera)(?:.*version|)[ /]([w.]+)/.exec( ua ) ||
                /(msie) ([w.]+)/.exec( ua ) ||
                ua.indexOf("compatible") < 0 && /(mozilla)(?:.*? rv:([w.]+)|)/.exec( ua ) ||
                [];

        return {
                browser: match[ 1 ] || "",
                version: match[ 2 ] || "0"
        };
};

// Don't clobber any existing jQuery.browser in case it's different
if ( !jQuery.browser ) {
        matched = jQuery.uaMatch( navigator.userAgent );
        browser = {};

        if ( matched.browser ) {
                browser[ matched.browser ] = true;
                browser.version = matched.version;
        }

        // Chrome is Webkit, but Webkit is also Safari.
        if ( browser.chrome ) {
                browser.webkit = true;
        } else if ( browser.webkit ) {
                browser.safari = true;
        }

        jQuery.browser = browser;
}




</script>

<script src="/js/funkcije-skupaj.js?v=1.043222"></script>

<script src="/js/flickity.min.js?v=1.043222"></script>

<script src="/js/new-responsive.js?v=1.043222"></script>
 <script src="/js/jquery.cookiecuttr.js"></script>
<script>
$(document).ready(function () {
	// activate cookie cutter
    $.cookieCuttr({
		cookieAnalytics:false,
		cookieCutter: true,
		
    	cookieDeclineButton: false,
		cookieOverlayEnabled:true,
		
		cookieDisable: '.piskotki',
		cookieDomain: 'kulinarika.net',
		cookieNotificationLocationBottom: false,
		cookieWhatAreTheyLink:'/zasebnost/',
		cookiePolicyLink: '/zasebnost/'
    });
}); 	
</script>

<!-- InstanceBeginEditable name="napis" -->
<!--<link href="/css/ajax-dynamic-list.css" rel="stylesheet" type="text/css" /> -->

<meta name="robots" content="index,follow">


<title>Recept: Potratna rolada - Kulinarika.net</title>

<link rel="canonical" href="https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/"><meta name="robots" content="max-image-preview:large">
<meta name="Description" content="Potratna rolada je prava praznična lepotička, pa še povsem enostavna za pripravo!">
<meta name="Keywords" content="rulada, potica, potratna potica,božič,martinovo,miklavževo,novo leto,velika noč,pečenje,jesen,zima,sladice,Martinovo">


<meta property="og:title" content="Recept: Potratna rolada - Kulinarika.net">
<meta property="og:description" content="Potratna rolada je prava praznična lepotička, pa še povsem enostavna za pripravo!">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/">
<meta property="og:image" content="https://www.kulinarika.net/slikerecepti/22765/1.webp?0.7055475"><meta property="og:image:type" content="image/webp">


<script src="/js/mnenja.js"></script><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9wSqI5i0iwGdf6L1CERNdmsTPgVu44ewj8QxTBYgsv1LCPUVF7YmWOvTappqB1139jAymxUW/RO8zmMqo4zlAAAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A+d7vJfYtay4OUbdtRPZA3y7bKQLsxaMEPmxgfhBGqKXNrdkCQeJlUwqa6EBbSfjwFtJWTrWIioXeMW+y8bWAgQAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9">
<script src="/js/knjiga.js"></script>
<link href="/p7epm/epm5/p7EPM05.css" rel="stylesheet" type="text/css" media="all">
<script src="/p7epm/p7EPMscripts.js"></script>
<style type="text/css">
.p7epm_cwrapper {height:0px;overflow:hidden;}

</style>
<script>

	if (isMobile) 
	{
		var head = document.getElementsByTagName('head')[0];
		var script = document.createElement('script');
		script.type = 'text/javascript';
		script.src = '/js/nosleep.min.js';
		head.appendChild(script);
		
	}


</script>
  <link href="/css/venobox/venobox.css?v=4.0502524229335" type="text/css" rel="stylesheet">
  <script src="/js/jquery.venobox.js?v=1.043222"></script>
 <link href="/css/slider-pro.min.css?v=4.0502524229335" type="text/css" rel="stylesheet">
 <script src="/js/jquery.sliderpro.min.js?v=1.043222"></script> 
  <script type="application/ld+json">
   [{
     "@context": "http://schema.org",
     "@type": "BreadcrumbList",
     "itemListElement":
     [
      {
       "@type": "ListItem",
       "position": 1,
	   "item": 
	   {
		  "name": "portal",
		  "@id": "https://www.kulinarika.net"
		}
      },
      {
       "@type": "ListItem",
      "position": 2,
      "item": {
			"name": "recepti",
			"@id": "/recepti/"
      }
	  }
	  ,
	  {
       "@type": "ListItem",
      "position": 3,

      "item": 
	  {
		  "name": "sladice",
		  "@id": "/recepti/seznam/sladice/"
      }
	  }
	  
	  ,
	  {
       "@type": "ListItem",
      "position": 4,
      "item": 
	  {
		 "name": "pecivo",
		 "@id": "/recepti/seznam/sladice/pecivo/"
	  }
      }
	  
	  ,
	  {
       "@type": "ListItem",
      "position": 5,
      "item": 
	  {
		 "name": "Potratna rolada",
		 "@id": "/recepti/sladice/pecivo/potratna-rolada/22765/"
	  }
      }
     ]
    }
	,
	

	{
	  "@context": "https://schema.org/",
	  "@type": "Recipe",
	  "name": "Potratna rolada",
	  "description": "Potratna rolada je prava praznična lepotička, pa še povsem enostavna za pripravo!",
	  
	  "image": ["https://www.kulinarika.net/slikerecepti/22765/1-200x150.webp","https://www.kulinarika.net/slikerecepti/22765/1-400x300.webp","https://www.kulinarika.net/slikerecepti/22765/1.webp"],
	  
	  "author": {
		"@type": "Person",
		"name": "CakeOClock_Urška"
	  },
	  
	  "aggregateRating": {"@type": "AggregateRating","ratingValue": "5","ratingCount": "3","reviewCount": "1"},
	  
	  
	  
	  "recipeCuisine": "",
	  "totalTime": "PT60M","keywords": "rulada, potica, potratna potica,božič,martinovo,miklavževo,novo leto,velika noč,pečenje,jesen,zima,sladice,Martinovo","recipeYield": "Sestavine ustrezajo gospodinjskemu pekaču (pekač o",
	  
	  "recipeCategory": "sladice: pecivo",
	  "recipeIngredient": [
		"​4 jajca M velikosti","120 g sladkorja","110 g moke","1 žlička kakava v prahu","​250 ml mleka","200 g mletih orehov","1 rumov sladkor (10 g)","50 g sladkorja","​100 g kisle smetane","20 g sladkorja v prahu"
	  ],
	  "recipeInstructions": [
		{"@type": "HowToStep","text":"Jajci s sladkorjem na najvišji hitrosti stepamo 10 minut. Na jajčno maso presejemo moko in z lopatko nežno vmešamo. 3/4 mase enakomerno premažemo po pekaču, ki smo ga obložili s papirjem za peko; en trak (četrtino) po dolžini pekača pustimo prazen. Ostali masi primešamo žličko kakava in premažemo po prostem delu pekača. Biskvit pečemo na 200 stopinj 7 minut."},{"@type": "HowToStep","text":"Na pult raztegnemo kuhinjsko krpo in nanjo položimo list peki papirja. Pečeno rolado zvrnemo na peki papir tako, da je čokoladni del biskvita na robu krpe (tako, da začnemo zvijati čokoladni del) in biskvit zvijemo v rolado. Ohladimo."},{"@type": "HowToStep","text":"Mleko zavremo in mu dodamo ostale sestavine. Zmešamo v gladko kremo in ohladimo."},{"@type": "HowToStep","text":"Smetano s sladkorjem z metlico premešamo."},{"@type": "HowToStep","text":"Ohlajeno testo za rolado odvijemo in previdno odlepimo vrhnjo plast peki papirja, na katerem se je pekel biskvit. S pomočjo paletnega noža biskvit enakomerno premažemo z orehovim nadevom. Po orehovem nadevu premažemo kislo smetano in s pomočjo spodnjega peki papirja tesno zavijemo v rolado. Rolado ovijemo v plastično živilsko folijo in za nekaj ur damo v hladilnik, da se učvrsti. Ohlajeno rolado posipamo s sladkorjem v prahu in postrežemo."}
		
		
	  ]
	}
]

	
	
	
	
	</script>

    


<script>
//<![CDATA[
hs.preserveContent = false;

$(window).on('load resize', function(){
	
	if ($(window).width() <= 500) {
	//$('#oglasi-stranski').insertAfter($('#receptSestavine'));
  } else {
    //$('#oglasi-stranski').insertAfter($('.info-kuha'));
  }
	
})

$(document).on({
		click: function(){
			var IDMnenje = $(this).data('id');
			$(this).prev('.like-stevilo').load("/inc/ajax-funkcije.asp?akcija=like_add_delete&s=1&IDMnenje=" + IDMnenje + "&rand=" + Math.round(new Date().getTime()/1000), function() {
				//reFacebook();
				$(this).parent().children('.likes-holder').toggleClass('on');
				});
		}
	},
 	'div.likes a.likes-holder');

$(document).on({
		click: function(){
		event.preventDefault();
			$.ajax({
				type: "get",
				url: "/inc/ajax-funkcije.asp?akcija=recepti_priljubljeni",
				data: {
					id: 22765,
					rand: Math.round(new Date().getTime()/1000)
				},
				success: function(response) {
					if (response==0) {
						$('#priljubljeni-recept img').attr('src', '/grafika7/icon-heart-off.svg');
						$('#zabelezka').removeClass('show').addClass('hide');
					}
					else
					{
						$('#priljubljeni-recept img').attr('src', '/grafika7/icon-heart-on.svg');
						$('#zabelezka').removeClass('hide').addClass('show');
					}
				}
			})
		}
	},
 	'#priljubljeni-recept');



$(document).ready(function() {

	enquire.register("screen and (max-width: 768px)", { // Mobile
		match : function() {

			$('#info-praznik').insertAfter('#receptPostopek').addClass('mobile');
			//$('#oglasi-stranski').insertAfter('footer').addClass('mobile');
			$('#oglas-aside2').insertBefore('#receptPostopek').addClass('enrecept');
			$('label#zaslon').removeClass('hide_important');
			
		},
		unmatch : function() { // Desktop

			$('#info-praznik').insertBefore('.info-kuha').removeClass('mobile');
			$('#oglas-aside2').appendTo('#oglasi-stranski').removeClass('enrecept');
			$('label#zaslon').addClass('hide_important');
	
		}
	});


		
	

	/* Preoader */

	function loadingStart(dividor) {
		$("#" + dividor).show();	
	}

	function loadingStop(dividor) {
		$("#" + dividor).hide();	
	}

	if (isMobile) {
	
		var noSleep = new NoSleep();
		
		
		
		$('#zaslon .toggle-checkbox').on('click', function() {
		
			
			varState=$('.toggle-checkbox').is(':checked');
			
			// Klik se izvrši 2x (label for in input, zato preveri ravno obratno stanje, kot je :-)
			if (!varState) {
				// daj na off
				noSleep.disable();
				$('.toggle-checkbox').prop('checked', false);

				$("#sestavine p:not('.empty,.poglavje') .input-narejeno").remove();
				$("#sestavine p:not('.empty,.poglavje')").removeClass("narejeno");
				$("#sestavine span.label").removeClass("narejeno");
				$("#sestavine span.label-value").removeClass("narejeno");	

				$("#postopek").removeClass("naredi");
				$("#postopek p:not('.edini_korak_postopek') .input-narejeno").remove();
				$("#postopek p:not('.edini_korak_postopek') .data").removeClass("narejeno");
				$("#postopek p:not('.edini_korak_postopek')").removeClass("narejeno");
				
				$("ul.priljubljeni").removeClass("hide");
				$("#oglasi-stranski").removeClass("hide");
				bannerModule.toggleParallax();
			
			} else {
				noSleep.enable();
				$('.toggle-checkbox').prop('checked', true);
				$("#sestavine p:not('.empty,.poglavje') .label-value").prepend(function(index, htmlContent) {return "<span class='input-narejeno'><input type='checkbox' class='style1 semzenaredil' name='semzenaredil' id='sestavina"+ index +"' /><label for='sestavina"+ index +"'>&nbsp;</label></span>"});
				$("#sestavine span.label").addClass("narejeno");
				$("#sestavine span.label-value").addClass("narejeno");
				
				$("#postopek").addClass("naredi");
				$("#postopek p:not('.edini_korak_postopek') .data").prepend(function(index, htmlContent) {return "<span class='input-narejeno'><input type='checkbox' class='style1 semzenaredil' name='semzenaredil' id='postopek"+ index +"' /><label for='postopek"+ index +"'>&nbsp;</label></span>"});		
				$("#postopek p:not('.edini_korak_postopek') .data").addClass("narejeno");
				$("ul.priljubljeni").addClass("hide");
				$("#oglasi-stranski").addClass("hide");
				bannerModule.toggleParallax();
			};

		
		});
	
		$('#zaslon').removeClass('hide_important');
		
	};
	
	$(document).on('click', '.semzenaredil', function() {
		
		varState=$(this).is(':checked');
		
		if (varState) {
		
			$(this).parent().parent().parent().addClass('narejeno');
			
		} else {
			$(this).parent().parent().parent().removeClass('narejeno');
			$(this).blur();
		}
	})
		

	$('.venobox').venobox(); 

	$(document).on('click', 'img.figlio', function(e){
        $('.vbox-close').click();
    });
	
	$('.odpirac-dodaj-zabelezko').venobox({
		post_close_callback: function(event){
			window.location.reload()
		}
   		 });
		

	
	$('#popup-oceneseznam-holder').venobox();
	$('#popup-zanimivosti-holder').venobox();
	$('#popup-prispevaj-holder').venobox();
		
	
	
	

	$('#popup-ocene-holder').bind('click', function () {
		return hs.htmlExpand(this, { width:385, height: 173, contentId: 'popup-ocene', objectType: 'iframe', preserveContent: false} )
	})



	$('#TekneIDSubmit').bind('click', function() {
		loadingStart("loadingRecipeID");
		$('#recipename').load('/inc/ajax-checkrecipename.asp?akcija=priporocilo&IDRecept=22765&ID=' + $('#TekneID').val(), function() {
			loadingStop("loadingRecipeID");
			});
	})
	
	$('#TekneNameSubmit').bind('click', function() {
		loadingStart("loadingRecipeName");
		$('#recipename2').load('/inc/ajax-checkrecipename.asp?akcija=priporocilo&IDRecept=22765&ImeRecepta=' + encodeURI($('#TekneName').val()), function() {
			loadingStop("loadingRecipeName");	
		});
	})
	
	var optionsSubmit = {
		target:	'#telo',
		beforeSubmit:  showRequest,
		success: function(responseText, statusText, xhr, $form) {
			napisgumb = $form.find('[name=napisgumb]').val();
			if (napisgumb==1){
					$form.find('input[type=submit]').css('display', 'none')
					$form.find('[name=napisgumb]').val('2');
				}
			loadingStop('loadingOddajPriporocilo');
			}	
		
	}
	
	$(document).on("submit", ".PriporociRecept", function() {
			$(this).ajaxSubmit(optionsSubmit)
			return false;
	})
	
	var optionsSubmit2 = {
		target:	'#telo',
		beforeSubmit:  showRequest,
		success: function(responseText, statusText, xhr, $form) {
			IDPriporocilo = $form.find('[name=IDpriporocilo]').val();
			$('#submit' + IDPriporocilo).css('display', 'inline');
			$('#PriporociRecept' + IDPriporocilo).find('[name=napisgumb]').val('1');
			loadingStop('#loadingOddajPriporocilo');
			}	
		
	}
	
	$(document).on("submit", ".PriporociRecept2", function() {	
			$(this).ajaxSubmit(optionsSubmit2)
			return false;
	})
	
	


	
	function showRequest() {
		loadingStart('loadingOddajPriporocilo')
		}
		
	
	$('#posljiprijatelju').on("click", function() {
	
		$.ajax({
			url: '/inc/ajax-funkcije.asp?id=22765&akcija=posljiprijatelju',
			success: function(text)
				{

				}
		})	
	
	})
	
	$('#receptiFotkePostopki').show();
	
		$('.vinoslider').flickity({
	// options
		cellAlign: 'left',
		contain: true,
		prevNextButtons: true,
		freeScroll: true,
		setGallerySize: false
	});

		
	
})




	


	
$(document).ready(function() {

	if (navigator.share) {
		$('#webShare').css("display", "inline-block");
		$("#ingredientsShare").css("display", "inline-block");
		
		$("#webShare").on("click", function(){
				navigator.share({
					title: 'Recept: Potratna rolada - Kulinarika.net',
					text: 'Našel sem tale izvrsten recept',
					url: 'https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/'

				});	
		});
		
		$("#ingredientsShare").on("click", function(){
				navigator.share({
					title: 'Recept: Potratna rolada - Kulinarika.net',
					text: '​Biskvit:\n\n​4 jajca M velikosti\n120 g sladkorja\n110 g moke\n1 žlička kakava v prahu\n\nOrehov nadev:\n\n​250 ml mleka\n200 g mletih orehov\n1 rumov sladkor (10 g)\n50 g sladkorja\n\nPremaz iz kisle smetane:\n\n​100 g kisle smetane\n20 g sladkorja v prahu\n\n\n',
					url: 'https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/'

				});

				$.ajax({
					url: '/inc/ajax-funkcije.asp?id=22765&akcija=deljenjesestavin&storitev=1'
				});
				
		});		
		
	}

	
	
	$(".vinoslider").css('visibility', 'visible');


	enquire.register("screen and (max-width: 768px)", {
		match : function() {
		   
		   $('.mobileslider').flickity({
				// options
				cellAlign: 'left',
				contain: true,
				prevNextButtons: false,
				setGallerySize: false
			});
			
			$('#receptSestavine a.prazniki_teaser').insertBefore('h1');
			
		},
		
		 unmatch : function() {
 
		   
		   $('.mobileslider').flickity('destroy');
		   $('#recept-main a.prazniki_teaser').insertAfter('#sestavine');
		   
		   		 
		}
	});
		
		
		$('#telo').load("/inc/ajax-priporocamo.asp?ID=22765");
		
		


	 
});

function mycarousel_itemAddCallback(xml)
{
	
	$( '#sliderRecepti' ).sliderPro({
			width: 640,
			height: 480,
			thumbnailWidth: 140,
			thumbnailHeight: 105,
			imageScaleMode: 'cover',
			arrows: true,
			buttons: false,
			loop:false,
			fullScreen: true,
			shuffle: false,
			smallSize: 500,
			mediumSize: 1000,
			largeSize: 3000,
			thumbnailArrows: true,
			autoplay: false,
			aspectRatio: 4/3,
			allowScaleUp: false,
			reachVideoAction: 'playVideo',
				breakpoints: {
					768: {
						thumbnailWidth: 120,
						thumbnailHeight: 90
					}
				},
			init: function() {

				var slides = $(this).get(0).slides.length;
				$( '#sliderRecepti' ).append('<div class="counter"><span class="active">1</span>/' + slides + '</div>');
				
				$( '#sliderRecepti img.sp-thumbnail.sp-video' ).removeClass('sp-video').parent().addClass('sp-video');
				
				$('.slider-pro .sp-image-container').css('background', '#000');
			
			}
		});
	
   	$( '.sp-slide' ).click(function(){
		 var slider = $( this ).parents( '.slider-pro' );
		 if( ! slider.hasClass('sp-swiping') && ! $(this).find('a').hasClass('sp-video') ) {
			  slider.find( '.sp-full-screen-button' ).trigger( 'click' );
		 }
	});

	$( '#sliderRecepti' ).on( 'sliderResize', function() {

			var slider = $(this),
			scaleMode = slider.data('sliderPro').settings.imageScaleMode;
			scaleUp=slider.data('sliderPro').settings.allowScaleUp;
			
			if ( slider.hasClass( 'sp-full-screen' ) && scaleMode !== 'contain' ) {
				slider.sliderPro( 'imageScaleMode', 'contain' );
				
			} else if ( ! slider.hasClass( 'sp-full-screen' ) && scaleMode !== 'cover' ) {
				slider.sliderPro( 'imageScaleMode', 'cover' );
			}
	});
	

	
	$( '#sliderRecepti' ).on( 'gotoSlide', function(event) {
		$(this).find('.counter .active').text(event.index + 1);
		
	});
	$( '#sliderRecepti' ).on( 'videoPlay', function(event) {
		$('.sp-caption-container .video').addClass('hide');
		
	});
	$( '#sliderRecepti' ).on( 'videoEnd', function(event) {
		$('.sp-caption-container .video').removeClass('hide');
		
	});	


	

}

</script>
<!-- InstanceEndEditable -->
<!-- InstanceBeginEditable name="head" -->
<!-- <script src="/ad/intext/intext2.js"></script> -->

    <!-- Add the ad-system.js script -->
	<script src="/ad-admin/js/ad-system.js" type="text/javascript" charset="utf-8"></script>

<!-- InstanceEndEditable -->



<!-- InstanceParam name="onload" type="text" value="" -->
<style type="text/css">.highslide img {cursor: url(/images/zoomin.cur), pointer !important;}.highslide-viewport-size {position: fixed; width: 100%; height: 100%; left: 0; top: 0}</style></head>

<body onload="">
<div id="fb-root"></div>
<div id="ozadjeReklamaContainer"><div id="ozadjeReklama" class=""><iframe id="banner16" name="banner16" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="1600" height="1200" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=16&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=sq9ta0eo0an1tequ&amp;target=_blank&amp;refresh=240&amp;cb=0,425819"></iframe><script>$(document).ready(function() {$('#banner16').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=16&kanal=recepti&kat=sladice&podkat=pecivo&user=sq9ta0eo0an1tequ&target=_blank&refresh=240&cb=0,425819');});</script></div></div><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_0_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?client=ca-pub-3352501607232481&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;abgtt=8&amp;lmt=1743779940&amp;plat=1%3A16777216%2C2%3A16777216%2C3%3A16%2C4%3A16%2C9%3A134250504%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32%2C41%3A32%2C42%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.kulinarika.net%2Frecepti%2Fsladice%2Fpecivo%2Fpotratna-rolada%2F22765%2F&amp;pra=5&amp;wgl=1&amp;aihb=0&amp;asro=0&amp;ailel=1~2~4~7~8~9~10~11~12~13~14~15~16~17~18~19~20~21~24~29~30~34&amp;aiael=1~2~3~4~7~8~9~10~11~12~13~14~15~16~17~18~19~20~21~24~29~30~34&amp;aicel=33~38&amp;aifxl=29_18~30_19&amp;aiixl=29_5~30_6&amp;itsi=-1&amp;aiapm=0.15&amp;aiapmi=0.33938&amp;aiact=0.7&amp;ailct=0.7&amp;uach=WyJtYWNPUyIsIjEzLjQuMCIsImFybSIsIiIsIjEzMy4wLjY5NDMuMTI3IixudWxsLDAsbnVsbCwiNjQiLFtbIk5vdChBOkJyYW5kIiwiOTkuMC4wLjAiXSxbIkdvb2dsZSBDaHJvbWUiLCIxMzMuMC42OTQzLjEyNyJdLFsiQ2hyb21pdW0iLCIxMzMuMC42OTQzLjEyNyJdXSwwXQ..&amp;dt=1743779940497&amp;bpp=20&amp;bdt=24&amp;idt=20&amp;shv=r20250403&amp;mjsv=m202504010101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eoidce=1&amp;nras=1&amp;correlator=2870691415985&amp;frm=20&amp;pv=2&amp;u_tz=120&amp;u_his=4&amp;u_h=956&amp;u_w=1470&amp;u_ah=850&amp;u_aw=1470&amp;u_cd=30&amp;u_sd=2&amp;dmc=8&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1470&amp;bih=763&amp;scr_x=0&amp;scr_y=0&amp;eid=95355973%2C95355975%2C95356929&amp;oid=2&amp;pvsid=1517653241833810&amp;tmod=1545610094&amp;uas=0&amp;nvt=1&amp;fsapi=1&amp;ref=https%3A%2F%2Fwww.kulinarika.net%2Frecepti%2Fseznam%2Fsladice%2F&amp;fc=1920&amp;brdim=0%2C37%2C0%2C37%2C1470%2C37%2C1470%2C850%2C1470%2C763&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;bz=1&amp;td=1&amp;tdf=2&amp;nt=1&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;dtd=24" data-google-container-id="a!1" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true"></iframe></div></ins><div id="MegaContainer"><div id="Container" class="cf">




<div id="kul-glava">
    <header class="header header-hidden">
        <div class="container">
            <nav class="nav-container">
                <div class="close-menu">×</div>
                <div class="nav-items">
                    <div class="dropdown-container">
                        <a class="dropbtn izbrano" href="#">Recepti</a>
                        <div class="dropdown-content" style="display: none;">
                            <div class="dropdown-content-inner">
								<div class="special-wrapper">
									<a class="special portal" href="/recepti/"><img loading="lazy" alt="vsi recepti" src="/grafika6/recepti-portal.webp"><span>Vsi recepti</span></a>
									<a class="special oddaj" href="/mojakulinarika/recepti/oddaj/"><img loading="lazy" alt="prispevaj svoj recept" src="/grafika6/recepti-poslji.webp"><span>Prispevajte svoj recept</span></a>
									<a class="special zdravo" href="/recepti/seznam/?zdravo=1"><img loading="lazy" alt="zdravi recepti" src="/grafika6/recepti-zdravo.webp"><span><span>Zdrave jedi</span></span></a>
								</div>
								<a class="menu" href="/recepti/seznam/sladice/"><img loading="lazy" alt="recepti za sladice" src="/grafika6/recepti18.webp"><span>Sladice</span></a>
								<a class="menu" href="/recepti/seznam/zelenjavne-jedi/"><img loading="lazy" alt="recepti za zelenjavne jedi" src="/grafika6/recepti21.webp"><span>Zelenjavne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/testenine/"><img loading="lazy" alt="recepti za testenine" src="/grafika6/recepti20.webp"><span>Testenine<span></span></span></a>
								<a class="menu" href="/recepti/seznam/solate/"><img loading="lazy" alt="recepti za solate" src="/grafika6/recepti19.webp"><span>Solate<span></span></span></a>
								<a class="menu" href="/recepti/seznam/juhe-in-zakuhe/"><img loading="lazy" alt="recepti za juhe in zakuhe" src="/grafika6/recepti05.webp"><span>Juhe in zakuhe<span></span></span></a>
								<a class="menu" href="/recepti/seznam/mesne-jedi/"><img loading="lazy" alt="recepti za mesne jedi" src="/grafika6/recepti07.webp"><span>Mesne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/kruh/"><img loading="lazy" alt="recepti za kruh" src="/grafika6/recepti06.webp"><span>Kruh<span></span></span></a>
								<a class="menu" href="/recepti/seznam/prikuhe/"><img loading="lazy" alt="recepti za prikuhe" src="/grafika6/recepti15.webp"><span>Prikuhe<span></span></span></a>
								<a class="menu" href="/recepti/seznam/priloge/"><img loading="lazy" alt="recepti za priloge" src="/grafika6/recepti16.webp"><span>Priloge<span></span></span></a> 
								<a class="menu" href="/recepti/seznam/jajcne-jedi/"><img loading="lazy" alt="recepti za jajčne jedi" src="/grafika6/recepti04.webp"><span>Jajčne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/eksotika/"><img loading="lazy" alt="eksotični recepti" src="/grafika6/recepti01.webp"><span>Eksotika<span></span></span></a>
								<a class="menu" href="/recepti/seznam/enloncnice/"><img loading="lazy" alt="recepti za enolončnice" src="/grafika6/recepti02.webp"><span>Enolončnice<span></span></span></a>
								<a class="menu" href="/recepti/seznam/gobje-jedi/"><img loading="lazy" alt="recepti za gobje jedi" src="/grafika6/recepti03.webp"><span>Gobje jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/morska-hrana/"><img loading="lazy" alt="recepti za morsko hrano" src="/grafika6/recepti08.webp"><span>Morska hrana<span></span></span></a>
								<a class="menu" href="/recepti/seznam/napitki/"><img loading="lazy" alt="recepti za napitke" src="/grafika6/recepti09.webp"><span>Napitki<span></span></span></a>
								<a class="menu" href="/recepti/seznam/omake/"><img loading="lazy" alt="recepti za omake" src="/grafika6/recepti10.webp"><span>Omake<span></span></span></a>
								<a class="menu" href="/recepti/seznam/otroska-hrana/"><img loading="lazy" alt="recepti za otroško hrano" src="/grafika6/recepti12.webp"><span>Otroška hrana<span></span></span></a>
								<a class="menu" href="/recepti/seznam/ozimnica/"><img loading="lazy" alt="recepti za ozimnico" src="/grafika6/recepti13.webp"><span>Ozimnica<span></span></span></a>
								<a class="menu" href="/recepti/seznam/predjedi/"><img loading="lazy" alt="recepti za predjedi" src="/grafika6/recepti14.webp"><span>Predjedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/sirove-jedi/"><img loading="lazy" alt="recepti za sirove jedi" src="/grafika6/recepti17.webp"><span>Jajčne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/zar/"><img loading="lazy" alt="recepti za žar" src="/grafika6/recepti04.webp"><span>Žar<span></span></span></a>
								<a class="menu" href="/recepti/seznam/ostale-jedi/"><img loading="lazy" alt="recepti za ostale jedi" src="/grafika6/recepti11.webp"><span>Ostale jedi<span></span></span></a>
								
		
                            </div>
                        </div>
                    </div>
					<a href="/vino/">Vino</a>
                        <a href="/forumi/" class="dropbtn">Forumi</a>

					
					
                    <a href="/fotoalbumi/">Albumi</a>
                    <a href="/zid/">Zid</a>
                    <a href="/blogi/">Blogi</a>
                    <a href="/zdravje/">Zdravo</a>
                    <a href="/zanimivo/">Zanimivo</a>
                    <a href="/iskanje/?datumi=tridni#novosti">Novosti</a>
				    

					
					
					
                </div>
            </nav>
            <div class="icon-line">
                <div class="hamburger">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </div>
                <div class="logo"><a href="/"><img src="https://www.kulinarika.net/grafika6/logotipi/kul.svg" alt="Kulinarika.net logo"></a></div>
				<form class="search-container" name="FormIskanje" id="FormIskanje" action="/iskanje/" method="GET" autocomplete="off">
					<input type="text" class="search-field" name="splosno_besede" placeholder="Išči recepte...">
					<button type="submit" class="search-submit">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
							<circle cx="11" cy="11" r="8"></circle>
							<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
						</svg>
						Išči
					</button>
					<div class="search-dropdown" style="display: none;">
						<a href="/recepti/seznam/?iskanje=1" class="search-link">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<circle cx="11" cy="11" r="8"></circle>
								<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
							</svg>
							Napredno iskanje po receptih
						</a>
						<a href="/forumi/forum/?vec=1" class="search-link">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<line x1="8" y1="6" x2="21" y2="6"></line>
								<line x1="8" y1="12" x2="21" y2="12"></line>
								<line x1="8" y1="18" x2="21" y2="18"></line>
								<line x1="3" y1="6" x2="3.01" y2="6"></line>
								<line x1="3" y1="12" x2="3.01" y2="12"></line>
								<line x1="3" y1="18" x2="3.01" y2="18"></line>
							</svg>
							Iskanje po forumih
						</a>
					</div>
				</form>
                <div class="mobile-right-icons">
                    <div class="search-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </div>
				
					
				
                    <div class="user-info">
                        <div class="avatar" alt="avatar slika">
                        <span class="ime">prijava</span>
						</div>
                        <div class="user-dropdown" style="display: none;">
							<div class="close-menu">×</div>
							


							 <form action="/mojakulinarika/prijava/" method="post" name="prijava" id="form-prijava" class="form-dizajn1 cf">
							 <h3>Prijava v Kulinarika.net</h3>
								 <div id="mojakulslo-login-wrapper" class="cf">
								 <input type="hidden" name="portal" value="1">
									<label for="loginuser">Uporabnik:</label><input id="loginuser" name="uporabnik" type="text"><br>
									<label for="loginpassword">Geslo:</label><input id="loginpassword" name="geslo" type="password"><br>
								 </div>
							
							
						
					   
							 <input name="Submit" type="submit" class="submit" value="Prijava">
						
								<a href="/mojakulinarika/pozabljeno/" class="noborder">Pozabljeno geslo</a>
						  <a class="noborder" href="/mojakulinarika/vpis/">Nov uporabnik</a>
						
							 </form>

						  
				  

							
							
							
							
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

</div>




<script>
(function() {
    document.addEventListener('DOMContentLoaded', function() {
        const kulGlava = document.getElementById('kul-glava');
        const header = kulGlava.querySelector('.header');
        const navContainer = kulGlava.querySelector('.nav-container');
        const hamburger = kulGlava.querySelector('.hamburger');
        const closeMenuButtons = kulGlava.querySelectorAll('.close-menu');
        const userInfo = kulGlava.querySelector('.user-info');
        const userDropdown = kulGlava.querySelector('.user-dropdown');
        const searchIcon = kulGlava.querySelector('.search-icon');
        const searchContainer = kulGlava.querySelector('.search-container');
        const dropdowns = kulGlava.querySelectorAll('.dropdown-container');
        const searchField = kulGlava.querySelector('.search-field');
        const searchDropdown = kulGlava.querySelector('.search-dropdown');

        let scrollPosition = 0;
        const body = document.body;

        function lockScroll() {
            if (!body.classList.contains('scroll-locked')) {
                scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
                body.classList.add('scroll-locked');
                body.style.overflow = 'hidden';
                body.style.position = 'fixed';
                body.style.top = `-${scrollPosition}px`;
                body.style.width = '100%';
            }
        }

        function unlockScroll() {
            if (body.classList.contains('scroll-locked')) {
                body.classList.remove('scroll-locked');
                body.style.removeProperty('overflow');
                body.style.removeProperty('position');
                body.style.removeProperty('top');
                body.style.removeProperty('width');
                window.scrollTo(0, scrollPosition);
            }
        }

        function closeAllMenus() {
            userDropdown.classList.remove('show');
            userDropdown.style.display = 'none';

            dropdowns.forEach(dropdown => {
                const dropdownContent = dropdown.querySelector('.dropdown-content');
                const dropbtn = dropdown.querySelector('.dropbtn');
                dropdownContent.style.display = 'none';
                dropbtn.classList.remove('active');
            });

            navContainer.classList.remove('show');
            searchContainer.classList.remove('show');

            searchDropdown.classList.remove('show');
            searchDropdown.style.display = 'none';

            unlockScroll();
        }

        function openMenu(menu) {
            menu.classList.add('show');
            document.body.classList.add('menu-open');
            lockScroll();
        }

        function closeMenu(menu) {
            menu.classList.remove('show');
            document.body.classList.remove('menu-open');
            unlockScroll();
        }

        function toggleUserDropdown(e) {
            e.stopPropagation();
            if (window.innerWidth <= 768) {
                userDropdown.style.removeProperty('display');
                userDropdown.classList.toggle('show');
                if (userDropdown.classList.contains('show')) {
                    lockScroll();
                } else {
                    unlockScroll();
                }
            } else {
                userDropdown.classList.remove('show');
                userDropdown.style.display = userDropdown.style.display === 'block' ? 'none' : 'block';
            }
        }

        function handleResize() {
            if (window.innerWidth <= 768) {
                userDropdown.style.removeProperty('display');
                if (userDropdown.classList.contains('show')) {
                    userDropdown.style.display = 'flex';
                }
            } else {
                userDropdown.classList.remove('show');
                userDropdown.style.display = 'none';
                unlockScroll();
            }
        }

        function closeUserDropdown() {
            if (window.innerWidth <= 768) {
                userDropdown.classList.remove('show');
            } else {
                userDropdown.style.display = 'none';
            }
            unlockScroll();
        }

        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            openMenu(navContainer);
        });

        userInfo.addEventListener('click', toggleUserDropdown);

        searchIcon.addEventListener('click', () => {
            searchContainer.classList.toggle('show');
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.dropdown') && !e.target.closest('.user-info') && !navContainer.contains(e.target) && !hamburger.contains(e.target)) {
                dropdowns.forEach(dropdown => {
                    dropdown.querySelector('.dropdown-content').style.display = 'none';
                    dropdown.querySelector('.dropbtn').classList.remove('active');
                });
                closeUserDropdown();
                unlockScroll();
            }
            if (!searchContainer.contains(e.target) && !searchIcon.contains(e.target)) {
                searchContainer.classList.remove('show');
            }
        });

        closeMenuButtons.forEach(button => {
            button.addEventListener('click', () => {
                closeMenu(navContainer);
                closeUserDropdown();
            });
        });

        const userDropdownCloseButton = userDropdown.querySelector('.close-menu');
        if (userDropdownCloseButton) {
            userDropdownCloseButton.addEventListener('click', (e) => {
                e.stopPropagation();
                closeUserDropdown();
            });
        }

        userDropdown.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        dropdowns.forEach(dropdown => {
            const dropbtn = dropdown.querySelector('.dropbtn');
            const dropdownContent = dropdown.querySelector('.dropdown-content');

            dropbtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                if (window.innerWidth <= 768) {
                    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
                    dropbtn.classList.toggle('active');
                    if (dropdownContent.style.display === 'block') {
                        lockScroll();
                    } else {
                        unlockScroll();
                    }
                } else {
                    closeUserDropdown();
                    dropdowns.forEach(otherDropdown => {
                        if (otherDropdown !== dropdown) {
                            otherDropdown.querySelector('.dropdown-content').style.display = 'none';
                            otherDropdown.querySelector('.dropbtn').classList.remove('active');
                        }
                    });
                    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
                    dropbtn.classList.toggle('active');
                }
            });

            dropdownContent.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        });

        searchField.addEventListener('focus', () => {
            searchDropdown.style.display = 'block';
            setTimeout(() => {
                searchDropdown.classList.add('show');
            }, 10);
            closeUserDropdown();
        });

        searchField.addEventListener('blur', (e) => {
            setTimeout(() => {
                if (!searchDropdown.contains(document.activeElement)) {
                    searchDropdown.classList.remove('show');
                    setTimeout(() => {
                        searchDropdown.style.display = 'none';
                    }, 300);
                }
            }, 100);
        });

        document.addEventListener('click', (e) => {
            if (!searchField.contains(e.target) && !searchDropdown.contains(e.target)) {
                searchDropdown.classList.remove('show');
                setTimeout(() => {
                    searchDropdown.style.display = 'none';
                }, 300);
            }
        });

        // New optimized scroll handling
        let lastKnownScrollPosition = 0;
        let ticking = false;
        const SCROLL_THRESHOLD = 5;

        function handleScroll(scrollPos) {
            if (Math.abs(scrollPos - lastKnownScrollPosition) > SCROLL_THRESHOLD) {
                if (scrollPos > lastKnownScrollPosition && scrollPos > 0) {
                    if (!header.classList.contains('header-hidden')) {
                        closeAllMenus();
                    }
                    header.classList.add('header-hidden');
                } else if (scrollPos < lastKnownScrollPosition) {
                    header.classList.remove('header-hidden');
                }
                lastKnownScrollPosition = scrollPos;
            }
        }

        window.addEventListener('scroll', (e) => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    handleScroll(window.scrollY);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        window.addEventListener('resize', debounce(handleResize, 150));
    });

    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            const later = () => {
                clearTimeout(timeout);
                func.apply(this, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
})();
    </script>


<div id="bodyContainer" class="cf">

    <div id="breadcrumbs">
          <div id="breadcrumbsPortal">
               
          </div>
        <!-- InstanceBeginEditable name="breadcrumbs" -->

<p class="breadcrumbs"><a href="/">domov</a> » <a href="/recepti/">recepti</a> » <a href="/recepti/seznam/sladice/">sladice</a> » <a href="/recepti/seznam/sladice/pecivo/">pecivo</a> » <span class="trenutno">Potratna rolada</span></p>
<!-- InstanceEndEditable -->
    
    </div>
<main id="vsebina" class="cf">
<!-- InstanceBeginEditable name="Main" -->

<section id="recepti" class="recept main-left">

<div id="recept-main">

<span style="display:none">rulada, potica, potratna potica,božič,martinovo,miklavževo,novo leto,velika noč,pečenje,jesen,zima,sladice,Martinovo</span><h1>Potratna rolada</h1><p class="podnaslov">Potratna rolada je prava praznična lepotička, pa še povsem enostavna za pripravo!</p><div class="podatki linki"><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/sq9ta0eo0an1tequ/">CakeOClock_Urška</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=CakeOClock_Urška"><img title="Pošljite uporabniku CakeOClock_Urška zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<span class="after1">ogledov: 59 196</span></div><span class="hide"></span> 
   






<div id="fotografije" class="cf">

	

			
			
			<div id="sliderRecepti" class="slider-pro sp-no-js no-thumbs">

				<div class="sp-slides">
					
					<a class="venobox vbox-item" href="/slikerecepti/22765/1.webp"><img title="Potratna rolada" alt="Potratna rolada" class="single rounded-all lazyautosizes ls-is-cached lazyloaded" data-sizes="auto" data-srcset="/slikerecepti/22765/1-200x150.webp 200w, /slikerecepti/22765/1-400x300.webp 400w, /slikerecepti/22765/1.webp " src="/grafika7/slika-se-nalaga.png" sizes="640px" srcset="/slikerecepti/22765/1-200x150.webp 200w, /slikerecepti/22765/1-400x300.webp 400w, /slikerecepti/22765/1.webp "></a>
				</div>
			</div> 	
				</div><ul class="servis cf linki"><span style="display:none">sladice: pecivo</span><li class="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"></li><li><img class="ura" src="/grafika6/ikona-ura.png" alt="1 ura" title="1 ura">&nbsp;<span class="cas">1 ura</span><time datetime="PT60M"></time></li><li id="ocene"><a href="/inc/popup-ocene.asp?ID=22765" id="popup-oceneseznam-holder" data-type="ajax" data-width="340" data-height="500" data-fullscreen_mobile="true" title="Ocenite recept" class="vbox-item"><img src="/grafika6/ikona-ocena.png" title="3 ocene">&nbsp;<span title="povprečna ocena: 5">5</span></a></li><li class="zanimivosti"><a href="/inc/ajax-funkcije.asp?akcija=recepti-zanimivosti&amp;ID=22765" id="popup-zanimivosti-holder" data-type="ajax" data-width="300" data-height="290" data-fullscreen_mobile="true" class="vbox-item"><img title="Zanimivosti" alt="Zanimivosti" src="/grafika7/icon-info.svg" width="24" height="24"></a></li>

</ul>

<ul class="priljubljeni"><a class="neopazen vbox-item" href="/inc/popup-prispevaj.asp?id=22765" id="popup-prispevaj-holder" data-type="ajax" data-width="300" data-height="290" data-fullscreen_mobile="true" title="Prispevaj" alt="Prispevaj"><li><img title="prispevajte" src="/grafika7/icon-add-photo.svg" height="24">&nbsp;Prispevaj</li></a><a class="neopazen" href="/mojakulinarika/nisemclan/"><li><img src="/grafika7/icon-heart-off.svg" title="shranite med priljubljene" height="28">&nbsp;Shrani</li></a><a class="neopazen" href="/recepti/tiskanje/?id=22765" target="_blank"><li><img title="natisnite recept" src="/grafika7/icon-printer.svg" height="24">&nbsp;Natisni</li></a></ul>

<div id="uvod" class="linki">

	

</div>




<div id="receptSestavine"><h2>Sestavine

<span id="ingredientsShare" style="display: inline-block;">
<img title="shranite sestavine" src="/grafika7/icon-share.svg" height="36">
</span>

</h2>
<div class="kolicina">Količina:  Sestavine ustrezajo gospodinjskemu pekaču (pekač o</div>
      <div id="sestavine" class="articlesize linki ">
        
           <p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>​Biskvit:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value">​<span class="label-inline">4</span> jajca M velikosti</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">120 g </span><span class="label-value">sladkorja</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">110 g </span><span class="label-value">moke</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">1 žlička </span><span class="label-value">kakava v prahu</span></p><p class="cf poglavje" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>Orehov nadev:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value">​<span class="label-inline">250 ml</span> mleka</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">200 g </span><span class="label-value">mletih orehov</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">1 </span><span class="label-value">rumov sladkor (10 g)</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">50 g </span><span class="label-value">sladkorja</span></p><p class="cf poglavje" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>Premaz iz kisle smetane:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value">​<span class="label-inline">100 g</span> kisle smetane</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">20 g </span><span class="label-value">sladkorja v prahu</span></p> 
</div>




</div>


<label class="toggle hide_important" id="zaslon">
	<input class="toggle-checkbox" type="checkbox">
	<div class="toggle-switch"></div>
	<p class="toggle-label">Način za kuhanje</p>
</label>

<div id="oglas300LuknjaRecept"></div>

  <div id="receptPostopek"><h2>Postopek</h2>

    <div id="postopek" class="articlesize linki ">

  <div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth delimiter" itemprop="text"><span class="label"></span><span class="data"><b>Biskvit:</b></span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Jajci s sladkorjem na najvišji hitrosti stepamo 10 minut. Na jajčno maso presejemo moko in z lopatko nežno vmešamo. 3/4 mase enakomerno premažemo po pekaču, ki smo ga obložili s papirjem za peko; en trak (četrtino) po dolžini pekača pustimo prazen. Ostali masi primešamo žličko kakava in premažemo po prostem delu pekača. Biskvit pečemo na 200 stopinj 7 minut.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Na pult raztegnemo kuhinjsko krpo in nanjo položimo list peki papirja. Pečeno rolado zvrnemo na peki papir tako, da je čokoladni del biskvita na robu krpe (tako, da začnemo zvijati čokoladni del) in biskvit zvijemo v rolado. Ohladimo.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth delimiter" itemprop="text"><span class="label"></span><span class="data"><b>Orehov nadev:</b></span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Mleko zavremo in mu dodamo ostale sestavine. Zmešamo v gladko kremo in ohladimo.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth delimiter" itemprop="text"><span class="label"></span><span class="data"><b>​Premaz iz kisle smetane:</b></span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Smetano s sladkorjem z metlico premešamo.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth delimiter" itemprop="text"><span class="label"></span><span class="data"><b>Sestavljanje rolade:</b></span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Ohlajeno testo za rolado odvijemo in previdno odlepimo vrhnjo plast peki papirja, na katerem se je pekel biskvit. S pomočjo paletnega noža biskvit enakomerno premažemo z orehovim nadevom. Po orehovem nadevu premažemo kislo smetano in s pomočjo spodnjega peki papirja tesno zavijemo v rolado. Rolado ovijemo v plastično živilsko folijo in za nekaj ur damo v hladilnik, da se učvrsti. Ohlajeno rolado posipamo s sladkorjem v prahu in postrežemo.</span></p></div></div></div><br class="clear"><div id="videooglas" class="" style="height: 0px; display: block;"><iframe id="banner25" name="banner25" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="640" height="480" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=25&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=sq9ta0eo0an1tequ&amp;target=_blank&amp;refresh=240&amp;cb=0,6630824" style="overflow: hidden; transform: scale(1); height: 0px;"></iframe><script>$(document).ready(function() {$('#banner25').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=25&kanal=recepti&kat=sladice&podkat=pecivo&user=sq9ta0eo0an1tequ&target=_blank&refresh=240&cb=0,6630824');});</script></div><div id="opombe" class="articlesize linki"><h2>Opombe</h2> <p>Več receptov najdete na FB strani Cake O'Clock-Urška peče in na blogu <a class="linki2" href="http://www.cakeoclock-urskapece.com" target="_blank">www.cakeoclock-urskapece.com</a></p></div><section id="vino_container" class="Najnovejsi cf"><h2><a class="linki3" href="/vino/?kategorija=18&amp;kategorija1=140">Predlogi za vino</a></h2><div class="vinoslider flickity-enabled is-draggable" tabindex="0" style="visibility: visible;"><div class="flickity-viewport" style="touch-action: pan-y;"><div class="flickity-slider" style="left: 0px; transform: translateX(0%);"><article class="carousel-cell vino is-selected" style="position: absolute; left: 0px; transform: translateX(0%);"><a href="/vino/120/"><div class="flex"><img alt="fotografija vina" src="/grafika7/slika-se-nalaga-vino.png" data-src="/slike/vino/hc1kv6peca7lqdj5_small.png" data-sizes="auto" data-srcset="/slike/vino/hc1kv6peca7lqdj5_small.png 50w, /slike/vino/hc1kv6peca7lqdj5.png" class="lazyload mala50 enovino"><img alt="logotip vinarja" class="vinar" src="/slike/vinar/1zfnvf74.png"></div></a><p class="ime single-line textLeft"><a href="/vino/120/">Ventus Rumeni Muškat</a></p></article><article class="carousel-cell vino" aria-hidden="true" style="position: absolute; left: 0px; transform: translateX(97.25%);"><a href="/vino/98/"><div class="flex"><img alt="fotografija vina" src="/grafika7/slika-se-nalaga-vino.png" data-src="/slike/vino/kzkw9yszyal927g9_small.jpg" data-sizes="auto" data-srcset="/slike/vino/kzkw9yszyal927g9_small.jpg 50w, /slike/vino/kzkw9yszyal927g9.jpg" class="lazyload mala50 enovino"><img alt="logotip vinarja" class="vinar" src="/slike/vinar/hc3a48dy.png"></div></a><p class="ime single-line textLeft"><a href="/vino/98/">Rumeni muškat – verduc Quercus</a></p></article></div></div><button class="flickity-button flickity-prev-next-button previous" type="button" disabled="" aria-label="Previous"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow"></path></svg></button><button class="flickity-button flickity-prev-next-button next" type="button" aria-label="Next"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow" transform="translate(100, 100) rotate(180) "></path></svg></button><ol class="flickity-page-dots"><li class="dot is-selected" aria-label="Page dot 1" aria-current="step"></li><li class="dot" aria-label="Page dot 2"></li></ol></div><p class="vec"><a class="linki3" href="/vino/?kategorija=18&amp;kategorija1=140">Več predlogov </a></p></section>



</div>

<ul id="servis2" class="servis clearfix">

	<span class=""><a href="/recepti/seznam/?priloznost=2">#božič</a><a href="/recepti/seznam/?priloznost=1">#martinovo</a><a href="/recepti/seznam/?priloznost=9">#miklavževo</a><a href="/recepti/seznam/?priloznost=6">#novo leto</a><a href="/recepti/seznam/?priloznost=5">#velika noč</a></span><span class=""><a href="/recepti/seznam/?letnicas=3">#jesen</a><a href="/recepti/seznam/?letnicas=4">#zima</a></span><span class=""><a href="/recepti/seznam/?vrstajedi=3">#sladice</a></span>



    </ul>

<ul class="servis cf linki"><li><a rel="noreferrer" href="https://www.facebook.com/sharer.php?u=https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/" target="_blank"><img src="/grafika7/icon-facebook.svg" height="36" title="pošljite na Facebook"></a></li><li><a rel="noreferrer" href="https://twitter.com/intent/tweet?text=Potratna+rolada%3A+&amp;url=https://www.kulinarika.net/recepti/sladice/pecivo/potratna-rolada/22765/" target="_blank"><img title="pošljite na Twitter" src="/grafika7/icon-twitter.svg" height="36"></a></li><li id="webShare" style="display: inline-block;"><img title="delite recept" src="/grafika7/icon-share.svg" height="36"></li><li><a class="link prijatelj" id="posljiprijatelju" href="mailto:?subject=Zanimiv%20recept%20na%20KULINARIKA%2ENET&amp;body=Pozdravljen%2Da%21%0D%0A%0D%0ANa%20strani%20KULINARIKA%2Enet%20sem%20zasledil%28a%29%20zanimiv%20recept%2C%20ki%20bi%20te%20morda%20zanimal%28a%29%3A%0D%0A%0D%0Ahttps%3A%2F%2Fwww%2Ekulinarika%2Enet/recepti/sladice/pecivo/potratna-rolada/22765/"><img title="pošljite po emailu" alt="pošljite po emailu" src="/grafika7/icon-email.svg" height="24"></a></li></ul>

    



	<div id="malioglasi" class="cf">
    
    
    
    </div>

<div id="mnenja-container"><h2>Mnenja o receptu</h2><section id="mnenja" class="odprto">
										  <div class="telo2 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="1"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/eka58/">eka58</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=eka58"><img title="Pošljite uporabniku eka58 zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 16.10.2016</p>
                                                 <p class="stevilo no-mobile">Št. objav: 15</p>
												  </div><div class="msgbody">
                                                  <img src="/grafika/smile_rezanje.gif" alt="Zelo vesel" width="18" height="18" align="absbottom"> 
                                                   <p>Najboljša rolada, kar sem ji delala in jedla do sedaj</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"><a href="/inc/ajax-funkcije.asp?akcija=mnenja_likes&amp;s=1&amp;IDMnenje=141079&amp;rand=20250404171900" class="popup-likes-holder">1</a></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  </section><div class="preberivec linki" style="display: none;"><a href="javascript:void(null)">preberi več</a></div><p class="navigacijazg">Število mnenj: 1, prikazujem mnenja  od 1 do 1</p>

											<div id="pisite_skok"></div>
											
											<span class="pomembno">Za pošiljanje mnenj je potreben <a href="/mojakulinarika/vpis/">vpis</a> ali
											 <a href="/mojakulinarika/prijava/">prijava</a>!</span> 
											 
	
		<script>
		
			$(document).ready(function() {
	
				
				
				$(document).on("click", ".preberivec", function() {	
						$('#mnenja').addClass('odprto');
						$('.preberivec').hide();
				})


				if ($('#mnenja').height()>350 && isMobile)
					{
						$('#mnenja').removeClass('odprto');
						$('.preberivec').show();
					}
					
					else
					
					{
						$('.preberivec').hide();
					}
	
	})
		
		
		</script>
			
</div>
      
    </section>
	

<!-- InstanceEndEditable -->
<section id="servisniBlok" class="recepti">
<!-- InstanceBeginEditable name="neboticnik" -->

<div id="nadOglas">

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-pravila">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Pogoji sodelovanja v nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-nagrade">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Več o nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-nagrade-old">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Več o potekli nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-sponzor">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">O pokrovitelju nagradne igre</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>

</div><aside class="velikanoc cf" id="info-praznik"><div class="container"><div class="recepti"><h2><a class="linki3" href="/recepti/seznam/?sort=popularnost&amp;nacin=desc&amp;priloznost=5">Velikonočne jedi</a></h2><a class="linki3" href="/recepti/sladice/potice/orehova-potica/1176/">Orehova potica</a><a class="linki3" href="/recepti/sladice/potice/kokosova-potica/4255/">Kokosova potica</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica-st-2/1667/">Potratna potica št. 2</a><a class="linki3" href="/recepti/sladice/potice/orehova-rulada/5737/">Orehova rulada</a><a class="linki3" href="/recepti/sladice/potice/nocna-potica/2889/">Nočna potica</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica/18232/">Potratna potica</a><a class="linki3" href="/recepti/sladice/potice/pehtranova-potica/378/">Pehtranova potica</a><a class="linki3" href="/recepti/sladice/potice/marmorni-kolac-iz-jogurta-/14691/">Marmorni kolač (iz jogurta)</a><a class="linki3" href="/recepti/sladice/potice/domaci-prijatelj-tete-dragice/12332/">Domači prijatelj tete Dragice</a><a class="linki3" href="/recepti/sladice/potice/vsestransko-testo/11944/">Vsestransko testo</a><a class="linki3" href="/recepti/sladice/potice/krhka-pita-za-vsak-okus/6439/">Krhka pita za vsak okus</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica/1390/">Potratna potica</a></div></div><p class="vec"><a class="linki3" href="/recepti/seznam/?sort=popularnost&amp;nacin=desc&amp;priloznost=5">več receptov za Veliko noč</a></p></aside><aside class="info-kuha cf"><h2>Kaj se danes kuha</h2><p><span><a href="/iskanje/?splosno_besede=sladice z mandlji" title="136 zadetkov">sladice z mandlji</a></span> / <span><a href="/iskanje/?splosno_besede=kosila" title="3030 zadetkov">kosila</a></span> / <span><a href="/iskanje/?splosno_besede=prigrizki brez glutena" title="28 zadetkov">prigrizki brez glutena</a></span> / <span><a href="/iskanje/?splosno_besede=kisla smetana namaz" title="124 zadetkov">kisla smetana namaz</a></span> / <span><a href="/iskanje/?splosno_besede=kislo mleko z kumaricami" title="29 zadetkov">kislo mleko z kumaricami</a></span> / <span><a href="/iskanje/?splosno_besede=1kg" title="40 zadetkov">1kg</a></span> / <span><a href="/iskanje/?splosno_besede=bucke s sirom in šunko" title="3 zadetki">bucke s sirom in šunko</a></span> / <span><a href="/iskanje/?splosno_besede=keks" title="579 zadetkov">keks</a></span> / <span><a href="/iskanje/?splosno_besede=po štručke" title="53 zadetkov">po štručke</a></span> / <span><a href="/iskanje/?splosno_besede=ocvrti skutini žepki" title="1 zadetek">ocvrti skutini žepki</a></span> / <span><a href="/iskanje/?splosno_besede=kolac iz jagod" title="11 zadetkov">kolac iz jagod</a></span> / <span><a href="/iskanje/?splosno_besede=čemaž z olivnim oljem" title="22 zadetkov">čemaž z olivnim oljem</a></span></p></aside><a href="/inc/ajax-funkcije.asp?akcija=receptirandom&amp;id=18" class="ideja-recept"><aside id="ideja-recept"><p><span class="ideja">ideja</span> za<br>sladkosnede</p></aside></a><div class="cf" id="oglasi-stranski"><div id="oglas-aside2" class=""><iframe id="banner3" name="banner3" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="300" height="600" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=3&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=sq9ta0eo0an1tequ&amp;target=_blank&amp;refresh=240&amp;cb=0,1658701"></iframe><script>$(document).ready(function() {$('#banner3').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=3&kanal=recepti&kat=sladice&podkat=pecivo&user=sq9ta0eo0an1tequ&target=_blank&refresh=240&cb=0,1658701');});</script></div></div><aside class="ReceptiVroci cf"><h2><a href="/recepti/lestvica/?kat=18">Najbolj vroči: april</a></h2><div class="mobileslider najboljvroci" style="visibility: visible;"><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/skutino-pecivo-za-pozresne-sosede/8100/"><img alt="fotografija recepta" src="/grafika7/slika-se-nalaga-manjsa.png" data-src="/slikerecepti/8100/60-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/8100/60-200x150.webp 200w, /slikerecepti/8100/60-400x300.webp 400w" class="lazyload"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/skutino-pecivo-za-pozresne-sosede/8100/">Skutino pecivo za požrešne sosede</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/sladice/ostalo/biskvit-za-torto-ki-nikoli-ne-pade-dol/5814/"><img alt="fotografija recepta" src="/grafika7/slika-se-nalaga-manjsa.png" data-src="/slikerecepti/5814/157-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/5814/157-200x150.webp 200w, /slikerecepti/5814/157-400x300.webp 400w" class="lazyload"></a></div><a class="link single-line" href="/recepti/sladice/ostalo/biskvit-za-torto-ki-nikoli-ne-pade-dol/5814/">Biskvit za torto, ki nikoli ne pade dol</a></div><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/torte/cokoladna-torta-za-vsakogar/4788/"><img alt="fotografija recepta" src="/grafika7/slika-se-nalaga-manjsa.png" data-src="/slikerecepti/4788/4-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/4788/4-200x150.webp 200w, /slikerecepti/4788/4-400x300.webp 400w" class="lazyload"></a></div><a class="link single-line" href="/recepti/sladice/torte/cokoladna-torta-za-vsakogar/4788/">Čokoladna torta za vsakogar</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/cokoladno-mascarponejeve-kocke/12619/"><img alt="fotografija recepta" src="/grafika7/slika-se-nalaga-manjsa.png" data-src="/slikerecepti/12619/101-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/12619/101-200x150.webp 200w, /slikerecepti/12619/101-400x300.webp 400w" class="lazyload"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/cokoladno-mascarponejeve-kocke/12619/">Čokoladno - mascarponejeve kocke</a></div><div class="vroci levo"><div class="slika"><a class="image-wrap video" href="/recepti/sladice/pecivo/zmagovalni-bananin-kruh/17823/"><img alt="fotografija recepta" src="/grafika7/slika-se-nalaga-manjsa.png" data-src="/slikerecepti/17823/17-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/17823/17-200x150.webp 200w, /slikerecepti/17823/17-400x300.webp 400w" class="lazyload"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/zmagovalni-bananin-kruh/17823/">Zmagovalni bananin kruh</a></div><div class="vroci "><div class="slika"><a class="image-wrap video" href="/recepti/sladice/ostalo/kremsnite-kremne-rezine-kot-z-bleda-/13838/"><img alt="fotografija recepta" src="/grafika7/slika-se-nalaga-manjsa.png" data-src="/slikerecepti/13838/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/13838/1-200x150.webp 200w, /slikerecepti/13838/1-400x300.webp 400w" class="lazyload"></a></div><a class="link single-line" href="/recepti/sladice/ostalo/kremsnite-kremne-rezine-kot-z-bleda-/13838/">Kremšnite, kremne rezine - kot z Bleda </a></div></div></aside><aside class="clanek"><a href="/recepti/izpostavljeno/velikonocna-miza-polna-ljubezni-nasveti-za-popoln-jedilnik/1235/"><h2>Velikonočna miza, polna ljubezni: Nasveti za popoln jedilnik</h2></a><div class="image-wrap"><a href="/recepti/izpostavljeno/velikonocna-miza-polna-ljubezni-nasveti-za-popoln-jedilnik/1235/"><img class="lazyload" alt="fotografija članka" src="/grafika7/slika-se-nalaga-manjsa.png" data-srcset="/slikeclanki/b1l67la2-200x150.webp 200w, /slikeclanki/b1l67la2-400x300.webp 400w, /slikeclanki/b1l67la2.webp 640w" data-sizes="auto"></a></div><p class="vec"><a class="linki3" href="/recepti/izpostavljeno/velikonocna-miza-polna-ljubezni-nasveti-za-popoln-jedilnik/1235/">Več</a></p></aside><section id="forum_servis"><a href="/forum/" class="linki"><h2>Forumi <span>(vroče teme)</span></h2></a><table width="100%" class="single-line"><tbody><tr class="prva"><td><a href="/forumi/tema/1096/kaj-jutri-za-kosilo-/">Kaj jutri za kosilo?</a></td><td><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/mopsika/">johana</a></td></tr><tr class="druga"><td><a href="/forumi/tema/7237/malo-za-hec/">malo za hec</a></td><td><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/sijasaja/">sijasaja</a></td></tr><tr class="prva"><td><a href="/forumi/tema/16585/moj-vrt/">MOJ vrt</a></td><td><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/malaga/">malaga</a></td></tr><tr class="druga"><td><a href="/forumi/tema/22350/kaj-danes-za-zajtrk/">Kaj danes za zajtrk</a></td><td><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/mopsika/">johana</a></td></tr><tr class="prva"><td><a href="/forumi/tema/5043/locevanje-zivil-90-dni-5-del/">Ločevanje živil 90. dni - 5. del</a></td><td><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/thau0383cy97hcr2/">dočka</a></td></tr></tbody></table></section><div id="zid-include"><aside class="seznamSlik cf"><a href="/zid/"><h2>Zid</h2></a><div class="mobileslider"><div class="enaslika levo"><div class="slika"><a href="/zid/14333/"><img src="/slike/zid/di5fntzz58d38scg-200x150.jpg" alt="fotografija" loading="lazy" class=""></a></div><div class="avtor"><a class="username" href="/uporabniki/seznam/primozg/">primozg</a></div></div><div class="enaslika"><div class="slika"><a href="/zid/14313/"><img src="/slike/zid/29f6plt1ddju6dd5-200x150.jpg" alt="fotografija" loading="lazy" class=""></a></div><div class="avtor"><a class="username" href="/uporabniki/seznam/ribaracarak/">ribaracarak</a></div></div><div class="enaslika levo"><div class="slika"><a href="/zid/14321/"><img src="/slike/zid/22ohqt985r0h5saw-200x150.jpg" alt="fotografija" loading="lazy" class=""></a></div><div class="avtor"><a class="username" href="/uporabniki/seznam/primozg/">primozg</a></div></div><div class="enaslika"><div class="slika"><a href="/zid/14323/"><img src="/slike/zid/6wgyotreqrulujej-200x150.jpg" alt="fotografija" loading="lazy" class=""></a></div><div class="avtor"><a class="username" href="/uporabniki/seznam/mamamia/">mamamia</a></div></div><div class="enaslika levo"><div class="slika"><a href="/zid/14331/"><img src="/slike/zid/8177jo11fxkpx6vs-200x150.jpg" alt="fotografija" loading="lazy" class=""></a></div><div class="avtor"><a class="username" href="/uporabniki/seznam/trixi/">Trixi</a></div></div><div class="enaslika"><div class="slika"><a href="/zid/14329/"><img src="/slike/zid/f7h4hj5e3pz77203-200x150.jpg" alt="fotografija" loading="lazy" class=""></a></div><div class="avtor"><a class="username" href="/uporabniki/seznam/23dqt17rmaqm0jy4/">Dragička</a></div></div></div></aside></div><a href="/recepti/seznam/?video=1"><h2>Video recepti</h2></a><article class="enNajnovejsi videostranski"><a href="/recepti/sladice/pecivo/sahovnica/21046/"><div class="image-wrap video"><img src="/grafika7/slika-se-nalaga.png" alt="Fotografija se nalaga" data-sizes="auto" data-srcset="/slikerecepti/21046/1-400x300.webp 400w" class="lazyload"></div><p class="ime single-line">Šahovnica</p></a></article><article class="enNajnovejsi videostranski"><a href="/recepti/sirove-jedi/hacapuri-gruzijski-kruh/22801/"><div class="image-wrap video"><img src="/grafika7/slika-se-nalaga.png" alt="Fotografija se nalaga" data-sizes="auto" data-srcset="/slikerecepti/22801/1-400x300.webp 400w" class="lazyload"></div><p class="ime single-line">Hačapuri - gruzijski kruh</p></a></article>


<div id="facebook-plugin-container" style="width: 100%; height: 640px; border:none; overflow:hidden;">
    <iframe class="facebook-iframe" data-src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Fkulinarika%2F&amp;tabs=timeline&amp;width=320&amp;height=640&amp;small_header=true&amp;adapt_container_width=true&amp;lazy=true&amp;hide_cover=false&amp;show_facepile=true" width="100%" height="640" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
    </iframe>
</div>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        var lazyIframes = [].slice.call(document.querySelectorAll("iframe.facebook-iframe"));

        if ("IntersectionObserver" in window) {
            let iframeObserver = new IntersectionObserver(function(entries, observer) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        let iframe = entry.target;
                        iframe.src = iframe.getAttribute("data-src");
                        iframeObserver.unobserve(iframe);
                    }
                });
            });

            lazyIframes.forEach(function(iframe) {
                iframeObserver.observe(iframe);
            });
        } else {
            // Fallback for browsers without IntersectionObserver support
            lazyIframes.forEach(function(iframe) {
                iframe.src = iframe.getAttribute("data-src");
            });
        }
    });
</script>




    <div class="highslide-html-content highslide-my-standard-popup" id="prijatelj">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Pošlji prijatelju</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="my-ocena">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Ocenite recept</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="ocenerecepta">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Ocene recepta</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="pomoc-priporocamo">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Zraven tekne</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="pomoc-vino">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Vinski kotiček</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popupSubscribed">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Naročeni ste na nova mnenja</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body ">Ko bo nekdo napisal novo mnenje k temu receptu, boste o tem dobili e-mail obvestilo (le enkrat, dokler ne odprete spet tega recepta). Na naročanje se lahko odjavite na samem receptu ali pa iz beležke.</div>
    
    </div>


    <!-- InstanceEndEditable -->
</section>
</main>
</div>
<div class="push"></div>
</div>



<footer class="footer cf">

<!-- The Modal -->
	<div id="myModal" class="modal">

	  <!-- Modal content -->
	  <div class="modal-content">
	    	<div class="img_wrap"><img alt="prazno" src="/images/prazno.jpg"></div>
	    	<div class="txt_wrap">
	    		<h3>Zaznan je blokator oglasov</h3>
				<p>Vsebina Kulinarika.net je podprta z oglaševanjem. Če želite še naprej uživati v naših receptih, izklopite blokiranje oglasov.</p>
				<h4>Prosimo vas, da za našo spletno stran onemogočite blokiranje oglasov.</h4>
				<!-- <p>Onemogoči blokiranje oglasov<p> -->
				<a href="javascript:void(0);" class="close_modal">Nadaljujte z blokiranjem oglasov</a>
			</div>
	  </div>

	</div>

    <div id="footer-top">
      
    </div>
	<div class="cf" id="footer-main">
	<p>© 2025 Spletna kulinarika d.o.o.</p>
	<ul>
    
		<li><a href="/oglasevanje/">Trženje</a></li>	
		<li><a href="/pravo/">Pogoji uporabe</a></li>
		<li><a href="/zasebnost/">Zasebnost</a></li>
		
   		<li><a href="/faq/">Pomoč</a></li>
        <li><a href="/zanimivo/dogodki/">Dogodki</a></li>
        
		<li><a href="/uporabniki/seznam/">Člani</a></li>
	</ul>
</div>

  
</footer>

<script>
<!--//<![CDATA[
if (isMobile == true) {
var ox_u = 'https://oglasi2.kulinarika.net/www/delivery/al.php?zoneid=24&layerstyle=simple&align=left&valign=top&padding=0&padding=0&shifth=0&shiftv=0&closebutton=t&nobg=t&noborder=t';
if (document.context) ox_u += '&context=' + escape(document.context);
document.write("<scr"+"ipt src='" + ox_u +"'></scr"+"ipt>");
}
//]]>--></script>

<div id="bottomAdWrapper">

        <div id="adContainer" style="height: 128.711px; visibility: visible; bottom: 0px;">
            <div id="closeButton"></div>
            <div id="scaleContainer" style="transform: scale(0.494845); width: 970px; height: 250px;">
                <iframe id="banner1" name="banner1" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="980" height="250" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=1&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=sq9ta0eo0an1tequ&amp;target=_blank&amp;refresh=240&amp;cb=6,696117E-02"></iframe><script>$(document).ready(function() {$('#banner1').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=1&kanal=recepti&kat=sladice&podkat=pecivo&user=sq9ta0eo0an1tequ&target=_blank&refresh=240&cb=6,696117E-02');});</script>
            </div>
        </div>
</div>

<script>
        // Create a namespace for the ad functionality
        const bottomAD = window.bottomAD || {};

        (function(namespace) {
            function showAd() {
                const adContainer = document.getElementById('adContainer');
                if (adContainer) {
                    adContainer.style.visibility = 'visible';
                    adContainer.style.bottom = '0';
                }
            }

            function hideAd() {
                const adContainer = document.getElementById('adContainer');
                if (adContainer) {
                    adContainer.style.bottom = '-250px';
                }
            }

            function debounce(func, wait) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        clearTimeout(timeout);
                        func(...args);
                    };
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                };
            }

			function resizeAd() {
				const scaleContainer = document.getElementById('scaleContainer');
				const adContainer = document.getElementById('adContainer');
				
				if (!scaleContainer || !adContainer) {
					console.error('One or more ad elements not found');
					return;
				}

				try {
					const windowWidth = window.innerWidth;
					const maxWidth = 480;
					const originalWidth = 970;
					const originalHeight = 250;

					const scale = Math.min(maxWidth, windowWidth) / originalWidth;
					const scaledHeight = originalHeight * scale;

					scaleContainer.style.transform = `scale(${scale})`;
					scaleContainer.style.width = `${originalWidth}px`;
					scaleContainer.style.height = `${originalHeight}px`;
					adContainer.style.height = `${scaledHeight + 5}px`; // 5px for padding
				} catch (error) {
					console.error('Error resizing ad:', error);
				}
			}

            // Expose functions in the namespace
            namespace.showAd = showAd;
            namespace.hideAd = hideAd;

            // Trigger the ad after 5 seconds (as an example)
            setTimeout(namespace.showAd, 5000);

            // Add debounced event listener for resizing
            const debouncedResize = debounce(resizeAd, 250);
            window.addEventListener('resize', debouncedResize);
            resizeAd(); // Initial resize

            // Close button event listener
            const closeButton = document.getElementById('closeButton');
            if (closeButton) {
                closeButton.addEventListener('click', namespace.hideAd);
            }
        })(bottomAD);
    </script>


</div>

<!-- InstanceBeginEditable name="dno" -->

<script>
const bannerModule = (function() {
    let lastKnownScrollPosition = 0;
    let ticking = false;
    let container, iframe, bottomBanner;
    let isParallaxVisible = true;
    let parallaxActive = window.innerWidth < 768;

    function easeInOutCubic(t) {
        return t < 0.5
            ? 4 * t * t * t
            : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }

    function resetStyles() {
        if (iframe) {
            iframe.style.transform = '';
        }
        if (bottomBanner) {
            bottomBanner.style.opacity = '';
        }
    }

    function updateParallax() {
        if (!parallaxActive) return;
        if (!isParallaxVisible) return;
        const containerRect = container.getBoundingClientRect();
        const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
        const scrollPercentage =
            (viewportHeight - containerRect.top) /
            (viewportHeight + containerRect.height);
        // Parallax effect
        if (scrollPercentage > 0 && scrollPercentage < 1) {
            const easedScrollPercentage = easeInOutCubic(scrollPercentage);
            const moveY =
                (easedScrollPercentage - 0.5) * containerRect.height * 0.5;
            iframe.style.transform = `translate(-50%, -50%) translateY(${moveY}px)`;
        }
        // Bottom banner visibility
        const buffer = 200; // Buffer for smoother transition
        let opacity = 1;
        if (containerRect.bottom > 0 && containerRect.top < viewportHeight) {
            opacity = 0;
        } else if (containerRect.bottom <= 0) {
            opacity = Math.min(1, (-containerRect.bottom) / buffer);
        } else if (containerRect.top >= viewportHeight) {
            opacity = Math.min(1, (containerRect.top - viewportHeight) / buffer);
        }
        opacity = Math.max(0, Math.min(1, opacity));
        bottomBanner.style.opacity = opacity;
        ticking = false;
    }

    function onScroll() {
        lastKnownScrollPosition = window.pageYOffset;
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateParallax();
            });
            ticking = true;
        }
    }

    function toggleParallax() {
        isParallaxVisible = !isParallaxVisible;
        container.style.display = isParallaxVisible ? 'block' : 'none';
        bottomBanner.style.display = isParallaxVisible ? 'flex' : 'none';
        if (isParallaxVisible) {
            updateParallax();
        }
    }

    function onResize() {
        let newParallaxActive = window.innerWidth < 768;
        if (newParallaxActive && !parallaxActive) {
            // Switched from desktop to mobile
            parallaxActive = true;
            init();
        } else if (!newParallaxActive && parallaxActive) {
            // Switched from mobile to desktop
            parallaxActive = false;
            // Reset styles and remove event listeners
            resetStyles();
            window.removeEventListener('scroll', onScroll);
        }
    }

    function init() {
        container = document.querySelector('#oglas-aside2');
        iframe = document.querySelector('#banner3');
        bottomBanner = document.querySelector('#adContainer');

        if (window.innerWidth >= 768) {
            // Reset styles on larger screens
            resetStyles();
            parallaxActive = false;
            return;
        }
        parallaxActive = true;
        window.addEventListener('scroll', onScroll, { passive: true });
        // Initial update
        updateParallax();
    }

    // Public methods
    return {
        init: init,
        toggleParallax: toggleParallax,
        onResize: onResize
    };
})();

// Initialize the module
document.addEventListener('DOMContentLoaded', function() {
    bannerModule.init();
    window.addEventListener('resize', bannerModule.onResize);
});
    </script>

<!-- InstanceEndEditable -->
<a href="#0" class="cd-top" title="na vrh">↑</a>


<div id="ad-container" class="ad-container"></div></body><iframe id="google_esf" name="google_esf" src="https://pagead2.googlesyndication.com/pagead/html/r20250403/r20190131/zrt_lookup_fy2021.html" style="display: none;"></iframe><!-- InstanceEnd --></html>

"""


html2 = """
<html lang="sl"><!-- InstanceBegin template="/Templates/ogrodje3.dwt.asp" codeOutsideHTMLIsLocked="false" --><head>
<meta charset="utf-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

/* Raleway Light */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  src: url('/fonts/Raleway-Light.woff2') format('woff2');
  font-display: swap;
}

/* Raleway Regular */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 400;
  src: url('/fonts/Raleway-Regular.woff2') format('woff2');
  font-display: swap;
}

/* Raleway Italic */
@font-face {
  font-family: 'Raleway';
  font-style: italic;
  font-weight: 400;
  src: url('/fonts/Raleway-Italic.woff2') format('woff2');
  font-display: swap;
}

/* Raleway SemiBold */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 600;
  src: url('/fonts/Raleway-SemiBold.woff2') format('woff2');
  font-display: swap;
}

</style>

<link href="/css/normalize.css" rel="stylesheet" type="text/css">
<link href="/css/skupaj-css.css?rel=4.0502524229335" rel="stylesheet" type="text/css">
<link href="/stiliprint.css" rel="stylesheet" type="text/css" media="print">


<link rel="stylesheet" href="/css/flickity.css" media="screen">

<script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202504010101/show_ads_impl_with_ama_fy2021.js?client=ca-pub-3352501607232481&amp;plah=www.kulinarika.net"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/plugins/ua/linkid.js"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script src="/js/lazysizes.min.js" async=""></script>
<link href="/css/new-responsive.css?v=1.03" rel="stylesheet" type="text/css">

<link rel="apple-touch-icon" sizes="180x180" href="/grafika6/favicons/apple-touch-icon.png">
<link rel="icon" type="image/png" href="/grafika6/favicons/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/grafika6/favicons/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="/grafika6/favicons/manifest.json">
<link rel="mask-icon" href="/grafika6/favicons/safari-pinned-tab.svg" color="#5bbad5">
<link rel="shortcut icon" href="/grafika6/favicons/favicon.ico">
<meta name="msapplication-config" content="/grafika6/favicons/browserconfig.xml">
<meta name="theme-color" content="#ffffff">

<meta property="og:locale" content="sl_SI">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kulinarika.net">
<meta property="fb:app_id" content="182018238801081">





<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "WebSite",
  "name": "Kulinarika.net",
  "url": "http://www.kulinarika.net",
  "image": "http://www.kulinarika.net/grafika6/logotipi/logo4.png",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.kulinarika.net/iskanje/?splosno_besede={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}

</script>

<link href="/css/recepti.css?v=4.0502524229335" rel="stylesheet" type="text/css">
<!-- InstanceBeginEditable name="stili" -->

<!-- InstanceEndEditable -->


<script>

	

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-15823371-4', {'storage': 'none', 'clientId': 'c9993b1a8e5f8da0d8b8de4e2140076d'});
  ga('require', 'linkid', 'linkid.js');
  ga('require', 'displayfeatures');

	
	// Creates an adblock detection plugin.
	ga('provide', 'adblockTracker', function(tracker, opts) {
	  var ad = document.createElement('ins');
	  ad.className = 'AdSense';
	  ad.style.display = 'block';
	  ad.style.position = 'absolute';
	  ad.style.top = '-1px';
	  ad.style.height = '1px';
	  document.body.appendChild(ad);
	  tracker.set('dimension' + opts.dimensionIndex, !ad.clientHeight);
	  document.body.removeChild(ad);
	});
	
	ga('require', 'adblockTracker', {dimensionIndex: 1});
    ga('send', 'pageview'), {'anonymizeIp': true};
  

</script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-3MTV8XXHPL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3MTV8XXHPL');
</script>

<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>

<script src="https://code.jquery.com/jquery-migrate-3.4.0.min.js" integrity="sha256-mBCu5+bVfYzOqpYyK4jm30ZxAZRomuErKEFJFIyrwvM=" crossorigin="anonymous"></script>

<!--    -->



<script data-ad-client="ca-pub-3352501607232481" async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" data-checked-head="true"></script>

<script>




$(function(){
	$('#menu .main-menu #menu02').addClass("selected");
	
		if (!isMobile) {
			$( "#zid-include" ).load( "/inc/ajax-funkcije.asp?akcija=zid-include&Menu=0202&sponzor=1", function() {
			console.log( "Load was performed." );
			});
		}
	
	$('.mobileslider').css('visibility', 'visible');
	
	enquire.register("screen and (max-width: 768px)", {
    match : function() {
		
		

		 
    },
	
	 unmatch : function() {

	  

 		}
	});
	
	
})

  $(window).on('load resize', function() {


	$(".spinner-container").delay(100).fadeOut(600).remove();
	
	
	
})

jQuery.uaMatch = function( ua ) {
        ua = ua.toLowerCase();

        var match = /(chrome)[ /]([w.]+)/.exec( ua ) ||
                /(webkit)[ /]([w.]+)/.exec( ua ) ||
                /(opera)(?:.*version|)[ /]([w.]+)/.exec( ua ) ||
                /(msie) ([w.]+)/.exec( ua ) ||
                ua.indexOf("compatible") < 0 && /(mozilla)(?:.*? rv:([w.]+)|)/.exec( ua ) ||
                [];

        return {
                browser: match[ 1 ] || "",
                version: match[ 2 ] || "0"
        };
};

// Don't clobber any existing jQuery.browser in case it's different
if ( !jQuery.browser ) {
        matched = jQuery.uaMatch( navigator.userAgent );
        browser = {};

        if ( matched.browser ) {
                browser[ matched.browser ] = true;
                browser.version = matched.version;
        }

        // Chrome is Webkit, but Webkit is also Safari.
        if ( browser.chrome ) {
                browser.webkit = true;
        } else if ( browser.webkit ) {
                browser.safari = true;
        }

        jQuery.browser = browser;
}




</script>

<script src="/js/funkcije-skupaj.js?v=1.043222"></script>

<script src="/js/flickity.min.js?v=1.043222"></script>

<script src="/js/new-responsive.js?v=1.043222"></script>
 <script src="/js/jquery.cookiecuttr.js"></script>
<script>
$(document).ready(function () {
	// activate cookie cutter
    $.cookieCuttr({
		cookieAnalytics:false,
		cookieCutter: true,
		
    	cookieDeclineButton: false,
		cookieOverlayEnabled:true,
		
		cookieDisable: '.piskotki',
		cookieDomain: 'kulinarika.net',
		cookieNotificationLocationBottom: false,
		cookieWhatAreTheyLink:'/zasebnost/',
		cookiePolicyLink: '/zasebnost/'
    });
}); 	
</script>

<!-- InstanceBeginEditable name="napis" -->
<!--<link href="/css/ajax-dynamic-list.css" rel="stylesheet" type="text/css" /> -->

<meta name="robots" content="index,follow">


<title>Recept: Orehova potica z rozinami - Kulinarika.net</title>

<link rel="canonical" href="https://www.kulinarika.net/recepti/sladice/potice/orehova-potica-z-rozinami/21134/">
<meta name="Description" content="slovenska klasika">
<meta name="Keywords" content="božič,martinovo,miklavževo,novo leto,velika noč,pečenje,jesen,pomlad,zima,sladice,Božična večerja in običaji po svetu,Decembrski prazniki in kulinarika,Fala Slonček,Katere 4 jedi ne smejo manjkati na velikonočni miz,Martinovo,Novoletna kulinarika po svetu,Orehova potica,Zajec ne nosi jajc!,Zakaj je Velika noč vsako leto na drug datum?,Zgodba o svetem Miklavžu">


<meta property="og:title" content="Recept: Orehova potica z rozinami - Kulinarika.net">
<meta property="og:description" content="slovenska klasika">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.kulinarika.net/recepti/sladice/potice/orehova-potica-z-rozinami/21134/">
<meta property="og:image" content="https://www.kulinarika.net/slikerecepti/21134/1.webp?0.7055475"><meta property="og:image:type" content="image/webp">


<script src="/js/mnenja.js"></script>
<script src="/js/knjiga.js"></script>
<link href="/p7epm/epm5/p7EPM05.css" rel="stylesheet" type="text/css" media="all">
<script src="/p7epm/p7EPMscripts.js"></script>
<style type="text/css">
.p7epm_cwrapper {height:0px;overflow:hidden;}

</style>
<script>

	if (isMobile) 
	{
		var head = document.getElementsByTagName('head')[0];
		var script = document.createElement('script');
		script.type = 'text/javascript';
		script.src = '/js/nosleep.min.js';
		head.appendChild(script);
		
	}


</script>
  <link href="/css/venobox/venobox.css?v=4.0502524229335" type="text/css" rel="stylesheet">
  <script src="/js/jquery.venobox.js?v=1.043222"></script>
 <link href="/css/slider-pro.min.css?v=4.0502524229335" type="text/css" rel="stylesheet">
 <script src="/js/jquery.sliderpro.min.js?v=1.043222"></script> 
  <script type="application/ld+json">
   [{
     "@context": "http://schema.org",
     "@type": "BreadcrumbList",
     "itemListElement":
     [
      {
       "@type": "ListItem",
       "position": 1,
	   "item": 
	   {
		  "name": "portal",
		  "@id": "https://www.kulinarika.net"
		}
      },
      {
       "@type": "ListItem",
      "position": 2,
      "item": {
			"name": "recepti",
			"@id": "/recepti/"
      }
	  }
	  ,
	  {
       "@type": "ListItem",
      "position": 3,

      "item": 
	  {
		  "name": "sladice",
		  "@id": "/recepti/seznam/sladice/"
      }
	  }
	  
	  ,
	  {
       "@type": "ListItem",
      "position": 4,
      "item": 
	  {
		 "name": "potice",
		 "@id": "/recepti/seznam/sladice/potice/"
	  }
      }
	  
	  ,
	  {
       "@type": "ListItem",
      "position": 5,
      "item": 
	  {
		 "name": "Orehova potica z rozinami",
		 "@id": "/recepti/sladice/potice/orehova-potica-z-rozinami/21134/"
	  }
      }
     ]
    }
	,
	

	{
	  "@context": "https://schema.org/",
	  "@type": "Recipe",
	  "name": "Orehova potica z rozinami",
	  "description": "slovenska klasika",
	  
	  "image": ["https://www.kulinarika.net/slikerecepti/21134/1-200x150.webp","https://www.kulinarika.net/slikerecepti/21134/1-400x300.webp","https://www.kulinarika.net/slikerecepti/21134/1.webp"],
	  
	  "author": {
		"@type": "Person",
		"name": "Fala Slonček"
	  },
	  
	  "aggregateRating": {"@type": "AggregateRating","ratingValue": "5","ratingCount": "2","reviewCount": "4"},
	  
	  
	  
	  "recipeCuisine": "",
	  "totalTime": "PT60M","keywords": "božič,martinovo,miklavževo,novo leto,velika noč,pečenje,jesen,pomlad,zima,sladice,Božična večerja in običaji po svetu,Decembrski prazniki in kulinarika,Fala Slonček,Katere 4 jedi ne smejo manjkati na velikonočni miz,Martinovo,Novoletna kulinarika po svetu,Orehova potica,Zajec ne nosi jajc!,Zakaj je Velika noč vsako leto na drug datum?,Zgodba o svetem Miklavžu",
	  
	  "recipeCategory": "sladice: potice",
	  "recipeIngredient": [
		"½ kocke kvasa Fala","2 dl mleka","48 dag moke","10 dag kisle smetane","10 dag masla","4 dag sladkorja","2 rumenjaka","1,5 male žličke soli","40 dag orehov","15 dag sladkorja","2 dl mleka","2 beljaka","1 žlica mlete kave","sok polovice limone","lupinica cele limone","10 dag rozin","jajce za premaz"
	  ],
	  "recipeInstructions": [
		{"@type": "HowToStep","text":"kVas Fala in sladkor raztopimo v toplem mleku. V posodo odmerimo sol, moko, kislo smetano, dodamo rumenjake in zamesimo kvašeno testo. Med mešanjem dodajamo na lističe narezano maslo. Ko so sestavine res dobro povezane med seboj in je testo gladko, posodo pokrijemo in damo testo na toplo vzhajati."},{"@type": "HowToStep","text":"Med vzhajanjem pripravimo nadev. Mlete orehe zmešamo s kavo in polovico sladkorja ter jih poparimo z vrelim mlekom ter dobro premešamo. Beljaka stepemo v trd sneg ob postopnem dodajanju preostalega sladkorja. V mlačen nadev vmešamo limonin sok, lupinico in sneg."},{"@type": "HowToStep","text":"Vzhajano testo stresemo na pult, ga pregnetemo in pustimo počivati nekaj minut. Nato testo razvaljamo, ga premažemo z nadevom, posujemo rozine in tesno zvijemo v zavitek. Tega položimo v pomaščen model in damo na toplo vzhajati."},{"@type": "HowToStep","text":"Vzhajano potico premažemo s stepenim jajcem, na več mestih prebodemo in prestavimo v vročo pečico. Potico pečemo približno eno uro pri 180 °C. Po potrebi jo pokrijemo, da bi se na vrhu ne zapekla preveč. Ko jo pokrijemo, moramo na foliji narediti na sredini luknjo, da bo zrak lahko krožil skozi odprtino modela. Sicer lahko ostane na sredini potica premalo pečena."}
		
		
	  ]
	}
]

	
	
	
	
	</script>

    


<script>
//<![CDATA[
hs.preserveContent = false;

$(window).on('load resize', function(){
	
	if ($(window).width() <= 500) {
	//$('#oglasi-stranski').insertAfter($('#receptSestavine'));
  } else {
    //$('#oglasi-stranski').insertAfter($('.info-kuha'));
  }
	
})

$(document).on({
		click: function(){
			var IDMnenje = $(this).data('id');
			$(this).prev('.like-stevilo').load("/inc/ajax-funkcije.asp?akcija=like_add_delete&s=1&IDMnenje=" + IDMnenje + "&rand=" + Math.round(new Date().getTime()/1000), function() {
				//reFacebook();
				$(this).parent().children('.likes-holder').toggleClass('on');
				});
		}
	},
 	'div.likes a.likes-holder');

$(document).on({
		click: function(){
		event.preventDefault();
			$.ajax({
				type: "get",
				url: "/inc/ajax-funkcije.asp?akcija=recepti_priljubljeni",
				data: {
					id: 21134,
					rand: Math.round(new Date().getTime()/1000)
				},
				success: function(response) {
					if (response==0) {
						$('#priljubljeni-recept img').attr('src', '/grafika7/icon-heart-off.svg');
						$('#zabelezka').removeClass('show').addClass('hide');
					}
					else
					{
						$('#priljubljeni-recept img').attr('src', '/grafika7/icon-heart-on.svg');
						$('#zabelezka').removeClass('hide').addClass('show');
					}
				}
			})
		}
	},
 	'#priljubljeni-recept');



$(document).ready(function() {

	enquire.register("screen and (max-width: 768px)", { // Mobile
		match : function() {

			$('#info-praznik').insertAfter('#receptPostopek').addClass('mobile');
			//$('#oglasi-stranski').insertAfter('footer').addClass('mobile');
			$('#oglas-aside2').insertBefore('#receptPostopek').addClass('enrecept');
			$('label#zaslon').removeClass('hide_important');
			
		},
		unmatch : function() { // Desktop

			$('#info-praznik').insertBefore('.info-kuha').removeClass('mobile');
			$('#oglas-aside2').appendTo('#oglasi-stranski').removeClass('enrecept');
			$('label#zaslon').addClass('hide_important');
	
		}
	});


		
	

	/* Preoader */

	function loadingStart(dividor) {
		$("#" + dividor).show();	
	}

	function loadingStop(dividor) {
		$("#" + dividor).hide();	
	}

	if (isMobile) {
	
		var noSleep = new NoSleep();
		
		
		
		$('#zaslon .toggle-checkbox').on('click', function() {
		
			
			varState=$('.toggle-checkbox').is(':checked');
			
			// Klik se izvrši 2x (label for in input, zato preveri ravno obratno stanje, kot je :-)
			if (!varState) {
				// daj na off
				noSleep.disable();
				$('.toggle-checkbox').prop('checked', false);

				$("#sestavine p:not('.empty,.poglavje') .input-narejeno").remove();
				$("#sestavine p:not('.empty,.poglavje')").removeClass("narejeno");
				$("#sestavine span.label").removeClass("narejeno");
				$("#sestavine span.label-value").removeClass("narejeno");	

				$("#postopek").removeClass("naredi");
				$("#postopek p:not('.edini_korak_postopek') .input-narejeno").remove();
				$("#postopek p:not('.edini_korak_postopek') .data").removeClass("narejeno");
				$("#postopek p:not('.edini_korak_postopek')").removeClass("narejeno");
				
				$("ul.priljubljeni").removeClass("hide");
				$("#oglasi-stranski").removeClass("hide");
				bannerModule.toggleParallax();
			
			} else {
				noSleep.enable();
				$('.toggle-checkbox').prop('checked', true);
				$("#sestavine p:not('.empty,.poglavje') .label-value").prepend(function(index, htmlContent) {return "<span class='input-narejeno'><input type='checkbox' class='style1 semzenaredil' name='semzenaredil' id='sestavina"+ index +"' /><label for='sestavina"+ index +"'>&nbsp;</label></span>"});
				$("#sestavine span.label").addClass("narejeno");
				$("#sestavine span.label-value").addClass("narejeno");
				
				$("#postopek").addClass("naredi");
				$("#postopek p:not('.edini_korak_postopek') .data").prepend(function(index, htmlContent) {return "<span class='input-narejeno'><input type='checkbox' class='style1 semzenaredil' name='semzenaredil' id='postopek"+ index +"' /><label for='postopek"+ index +"'>&nbsp;</label></span>"});		
				$("#postopek p:not('.edini_korak_postopek') .data").addClass("narejeno");
				$("ul.priljubljeni").addClass("hide");
				$("#oglasi-stranski").addClass("hide");
				bannerModule.toggleParallax();
			};

		
		});
	
		$('#zaslon').removeClass('hide_important');
		
	};
	
	$(document).on('click', '.semzenaredil', function() {
		
		varState=$(this).is(':checked');
		
		if (varState) {
		
			$(this).parent().parent().parent().addClass('narejeno');
			
		} else {
			$(this).parent().parent().parent().removeClass('narejeno');
			$(this).blur();
		}
	})
		

	$('.venobox').venobox(); 

	$(document).on('click', 'img.figlio', function(e){
        $('.vbox-close').click();
    });
	
	$('.odpirac-dodaj-zabelezko').venobox({
		post_close_callback: function(event){
			window.location.reload()
		}
   		 });
		

	
	$('#popup-oceneseznam-holder').venobox();
	$('#popup-zanimivosti-holder').venobox();
	$('#popup-prispevaj-holder').venobox();
		
	
	
	

	$('#popup-ocene-holder').bind('click', function () {
		return hs.htmlExpand(this, { width:385, height: 173, contentId: 'popup-ocene', objectType: 'iframe', preserveContent: false} )
	})



	$('#TekneIDSubmit').bind('click', function() {
		loadingStart("loadingRecipeID");
		$('#recipename').load('/inc/ajax-checkrecipename.asp?akcija=priporocilo&IDRecept=21134&ID=' + $('#TekneID').val(), function() {
			loadingStop("loadingRecipeID");
			});
	})
	
	$('#TekneNameSubmit').bind('click', function() {
		loadingStart("loadingRecipeName");
		$('#recipename2').load('/inc/ajax-checkrecipename.asp?akcija=priporocilo&IDRecept=21134&ImeRecepta=' + encodeURI($('#TekneName').val()), function() {
			loadingStop("loadingRecipeName");	
		});
	})
	
	var optionsSubmit = {
		target:	'#telo',
		beforeSubmit:  showRequest,
		success: function(responseText, statusText, xhr, $form) {
			napisgumb = $form.find('[name=napisgumb]').val();
			if (napisgumb==1){
					$form.find('input[type=submit]').css('display', 'none')
					$form.find('[name=napisgumb]').val('2');
				}
			loadingStop('loadingOddajPriporocilo');
			}	
		
	}
	
	$(document).on("submit", ".PriporociRecept", function() {
			$(this).ajaxSubmit(optionsSubmit)
			return false;
	})
	
	var optionsSubmit2 = {
		target:	'#telo',
		beforeSubmit:  showRequest,
		success: function(responseText, statusText, xhr, $form) {
			IDPriporocilo = $form.find('[name=IDpriporocilo]').val();
			$('#submit' + IDPriporocilo).css('display', 'inline');
			$('#PriporociRecept' + IDPriporocilo).find('[name=napisgumb]').val('1');
			loadingStop('#loadingOddajPriporocilo');
			}	
		
	}
	
	$(document).on("submit", ".PriporociRecept2", function() {	
			$(this).ajaxSubmit(optionsSubmit2)
			return false;
	})
	
	


	
	function showRequest() {
		loadingStart('loadingOddajPriporocilo')
		}
		
	
	$('#posljiprijatelju').on("click", function() {
	
		$.ajax({
			url: '/inc/ajax-funkcije.asp?id=21134&akcija=posljiprijatelju',
			success: function(text)
				{

				}
		})	
	
	})
	
	$('#receptiFotkePostopki').show();
	
		$('.vinoslider').flickity({
	// options
		cellAlign: 'left',
		contain: true,
		prevNextButtons: true,
		freeScroll: true,
		setGallerySize: false
	});

		
	
})




	


	
$(document).ready(function() {

	if (navigator.share) {
		$('#webShare').css("display", "inline-block");
		$("#ingredientsShare").css("display", "inline-block");
		
		$("#webShare").on("click", function(){
				navigator.share({
					title: 'Recept: Orehova potica z rozinami - Kulinarika.net',
					text: 'Našel sem tale izvrsten recept',
					url: 'https://www.kulinarika.net/recepti/sladice/potice/orehova-potica-z-rozinami/21134/'

				});	
		});
		
		$("#ingredientsShare").on("click", function(){
				navigator.share({
					title: 'Recept: Orehova potica z rozinami - Kulinarika.net',
					text: 'Testo:\n½ kocke \n2 dl mleka\n48 dag moke\n10 dag kisle smetane\n10 dag masla\n4 dag sladkorja\n2 rumenjaka\n1,5 male žličke soli\n\nNadev:\n40 dag orehov\n15 dag sladkorja\n2 dl mleka\n2 beljaka\n1 žlica mlete kave\nsok polovice limone\nlupinica cele limone \n10 dag rozin\njajce za premaz\n',
					url: 'https://www.kulinarika.net/recepti/sladice/potice/orehova-potica-z-rozinami/21134/'

				});

				$.ajax({
					url: '/inc/ajax-funkcije.asp?id=21134&akcija=deljenjesestavin&storitev=1'
				});
				
		});		
		
	}

	
	
	$(".vinoslider").css('visibility', 'visible');


	enquire.register("screen and (max-width: 768px)", {
		match : function() {
		   
		   $('.mobileslider').flickity({
				// options
				cellAlign: 'left',
				contain: true,
				prevNextButtons: false,
				setGallerySize: false
			});
			
			$('#receptSestavine a.prazniki_teaser').insertBefore('h1');
			
		},
		
		 unmatch : function() {
 
		   
		   $('.mobileslider').flickity('destroy');
		   $('#recept-main a.prazniki_teaser').insertAfter('#sestavine');
		   
		   		 
		}
	});
		
		
		$('#telo').load("/inc/ajax-priporocamo.asp?ID=21134");
		
		

				  
		  		$.ajax({
					url: '/inc/ajax-receptislike.asp',
					data: {
						IDRecept: 21134,
						fetch: 3,
						first: 1,
						type: 'HTML'
					},
					success: function(HTML) {
						$('.sp-slides').html(HTML);
						mycarousel_itemAddCallback();
					},
					datatype: 'HTML'
				});

	
				$('#receptiFotke').bind("click", function() {
						
						$( '#sliderRecepti' ).sliderPro( 'gotoSlide', 0 );
						$('#receptiFotke').hide();
						$('#receptiFotkePostopki').show();
				});
				
				$('#receptiFotkePostopki').bind("click", function() {
					$( '#sliderRecepti' ).sliderPro( 'gotoSlide', 3 );
					$('#receptiFotkePostopki').hide();
					$('#receptiFotke').show();
				});

				
	
		



	 
});

function mycarousel_itemAddCallback(xml)
{
	
	$( '#sliderRecepti' ).sliderPro({
			width: 640,
			height: 480,
			thumbnailWidth: 140,
			thumbnailHeight: 105,
			imageScaleMode: 'cover',
			arrows: true,
			buttons: false,
			loop:false,
			fullScreen: true,
			shuffle: false,
			smallSize: 500,
			mediumSize: 1000,
			largeSize: 3000,
			thumbnailArrows: true,
			autoplay: false,
			aspectRatio: 4/3,
			allowScaleUp: false,
			reachVideoAction: 'playVideo',
				breakpoints: {
					768: {
						thumbnailWidth: 120,
						thumbnailHeight: 90
					}
				},
			init: function() {

				var slides = $(this).get(0).slides.length;
				$( '#sliderRecepti' ).append('<div class="counter"><span class="active">1</span>/' + slides + '</div>');
				
				$( '#sliderRecepti img.sp-thumbnail.sp-video' ).removeClass('sp-video').parent().addClass('sp-video');
				
				$('.slider-pro .sp-image-container').css('background', '#000');
			
			}
		});
	
   	$( '.sp-slide' ).click(function(){
		 var slider = $( this ).parents( '.slider-pro' );
		 if( ! slider.hasClass('sp-swiping') && ! $(this).find('a').hasClass('sp-video') ) {
			  slider.find( '.sp-full-screen-button' ).trigger( 'click' );
		 }
	});

	$( '#sliderRecepti' ).on( 'sliderResize', function() {

			var slider = $(this),
			scaleMode = slider.data('sliderPro').settings.imageScaleMode;
			scaleUp=slider.data('sliderPro').settings.allowScaleUp;
			
			if ( slider.hasClass( 'sp-full-screen' ) && scaleMode !== 'contain' ) {
				slider.sliderPro( 'imageScaleMode', 'contain' );
				
			} else if ( ! slider.hasClass( 'sp-full-screen' ) && scaleMode !== 'cover' ) {
				slider.sliderPro( 'imageScaleMode', 'cover' );
			}
	});
	

	
	$( '#sliderRecepti' ).on( 'gotoSlide', function(event) {
		$(this).find('.counter .active').text(event.index + 1);
		
	});
	$( '#sliderRecepti' ).on( 'videoPlay', function(event) {
		$('.sp-caption-container .video').addClass('hide');
		
	});
	$( '#sliderRecepti' ).on( 'videoEnd', function(event) {
		$('.sp-caption-container .video').removeClass('hide');
		
	});	


	

}

</script>
<!-- InstanceEndEditable -->
<!-- InstanceBeginEditable name="head" -->
<!-- <script src="/ad/intext/intext2.js"></script> -->

    <!-- Add the ad-system.js script -->
	<script src="/ad-admin/js/ad-system.js" type="text/javascript" charset="utf-8"></script>

<!-- InstanceEndEditable -->



<!-- InstanceParam name="onload" type="text" value="" -->
<meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9wSqI5i0iwGdf6L1CERNdmsTPgVu44ewj8QxTBYgsv1LCPUVF7YmWOvTappqB1139jAymxUW/RO8zmMqo4zlAAAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A+d7vJfYtay4OUbdtRPZA3y7bKQLsxaMEPmxgfhBGqKXNrdkCQeJlUwqa6EBbSfjwFtJWTrWIioXeMW+y8bWAgQAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><style type="text/css">.highslide img {cursor: url(/images/zoomin.cur), pointer !important;}.highslide-viewport-size {position: fixed; width: 100%; height: 100%; left: 0; top: 0}</style></head>

<body onload="">
<div id="fb-root"></div>
<div id="ozadjeReklamaContainer"><div id="ozadjeReklama" class=""><iframe id="banner16" name="banner16" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="1600" height="1200" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=16&amp;kanal=recepti&amp;kat=sladice&amp;podkat=potice&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,1796643"></iframe><script>$(document).ready(function() {$('#banner16').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=16&kanal=recepti&kat=sladice&podkat=potice&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,1796643');});</script></div></div><div id="MegaContainer" data-sponzor="69740"><div id="Container" class="cf">




<div id="kul-glava">
    <header class="header">
        <div class="container">
            <nav class="nav-container">
                <div class="close-menu">×</div>
                <div class="nav-items">
                    <div class="dropdown-container">
                        <a class="dropbtn izbrano" href="#">Recepti</a>
                        <div class="dropdown-content" style="display: none;">
                            <div class="dropdown-content-inner">
								<div class="special-wrapper">
									<a class="special portal" href="/recepti/"><img loading="lazy" alt="vsi recepti" src="/grafika6/recepti-portal.webp"><span>Vsi recepti</span></a>
									<a class="special oddaj" href="/mojakulinarika/recepti/oddaj/"><img loading="lazy" alt="prispevaj svoj recept" src="/grafika6/recepti-poslji.webp"><span>Prispevajte svoj recept</span></a>
									<a class="special zdravo" href="/recepti/seznam/?zdravo=1"><img loading="lazy" alt="zdravi recepti" src="/grafika6/recepti-zdravo.webp"><span><span>Zdrave jedi</span></span></a>
								</div>
								<a class="menu" href="/recepti/seznam/sladice/"><img loading="lazy" alt="recepti za sladice" src="/grafika6/recepti18.webp"><span>Sladice</span></a>
								<a class="menu" href="/recepti/seznam/zelenjavne-jedi/"><img loading="lazy" alt="recepti za zelenjavne jedi" src="/grafika6/recepti21.webp"><span>Zelenjavne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/testenine/"><img loading="lazy" alt="recepti za testenine" src="/grafika6/recepti20.webp"><span>Testenine<span></span></span></a>
								<a class="menu" href="/recepti/seznam/solate/"><img loading="lazy" alt="recepti za solate" src="/grafika6/recepti19.webp"><span>Solate<span></span></span></a>
								<a class="menu" href="/recepti/seznam/juhe-in-zakuhe/"><img loading="lazy" alt="recepti za juhe in zakuhe" src="/grafika6/recepti05.webp"><span>Juhe in zakuhe<span></span></span></a>
								<a class="menu" href="/recepti/seznam/mesne-jedi/"><img loading="lazy" alt="recepti za mesne jedi" src="/grafika6/recepti07.webp"><span>Mesne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/kruh/"><img loading="lazy" alt="recepti za kruh" src="/grafika6/recepti06.webp"><span>Kruh<span></span></span></a>
								<a class="menu" href="/recepti/seznam/prikuhe/"><img loading="lazy" alt="recepti za prikuhe" src="/grafika6/recepti15.webp"><span>Prikuhe<span></span></span></a>
								<a class="menu" href="/recepti/seznam/priloge/"><img loading="lazy" alt="recepti za priloge" src="/grafika6/recepti16.webp"><span>Priloge<span></span></span></a> 
								<a class="menu" href="/recepti/seznam/jajcne-jedi/"><img loading="lazy" alt="recepti za jajčne jedi" src="/grafika6/recepti04.webp"><span>Jajčne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/eksotika/"><img loading="lazy" alt="eksotični recepti" src="/grafika6/recepti01.webp"><span>Eksotika<span></span></span></a>
								<a class="menu" href="/recepti/seznam/enloncnice/"><img loading="lazy" alt="recepti za enolončnice" src="/grafika6/recepti02.webp"><span>Enolončnice<span></span></span></a>
								<a class="menu" href="/recepti/seznam/gobje-jedi/"><img loading="lazy" alt="recepti za gobje jedi" src="/grafika6/recepti03.webp"><span>Gobje jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/morska-hrana/"><img loading="lazy" alt="recepti za morsko hrano" src="/grafika6/recepti08.webp"><span>Morska hrana<span></span></span></a>
								<a class="menu" href="/recepti/seznam/napitki/"><img loading="lazy" alt="recepti za napitke" src="/grafika6/recepti09.webp"><span>Napitki<span></span></span></a>
								<a class="menu" href="/recepti/seznam/omake/"><img loading="lazy" alt="recepti za omake" src="/grafika6/recepti10.webp"><span>Omake<span></span></span></a>
								<a class="menu" href="/recepti/seznam/otroska-hrana/"><img loading="lazy" alt="recepti za otroško hrano" src="/grafika6/recepti12.webp"><span>Otroška hrana<span></span></span></a>
								<a class="menu" href="/recepti/seznam/ozimnica/"><img loading="lazy" alt="recepti za ozimnico" src="/grafika6/recepti13.webp"><span>Ozimnica<span></span></span></a>
								<a class="menu" href="/recepti/seznam/predjedi/"><img loading="lazy" alt="recepti za predjedi" src="/grafika6/recepti14.webp"><span>Predjedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/sirove-jedi/"><img loading="lazy" alt="recepti za sirove jedi" src="/grafika6/recepti17.webp"><span>Jajčne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/zar/"><img loading="lazy" alt="recepti za žar" src="/grafika6/recepti04.webp"><span>Žar<span></span></span></a>
								<a class="menu" href="/recepti/seznam/ostale-jedi/"><img loading="lazy" alt="recepti za ostale jedi" src="/grafika6/recepti11.webp"><span>Ostale jedi<span></span></span></a>
								
		
                            </div>
                        </div>
                    </div>
					<a href="/vino/">Vino</a>
                        <a href="/forumi/" class="dropbtn">Forumi</a>

					
					
                    <a href="/fotoalbumi/">Albumi</a>
                    <a href="/zid/">Zid</a>
                    <a href="/blogi/">Blogi</a>
                    <a href="/zdravje/">Zdravo</a>
                    <a href="/zanimivo/">Zanimivo</a>
                    <a href="/iskanje/?datumi=tridni#novosti">Novosti</a>
				    

					
					
					
                </div>
            </nav>
            <div class="icon-line">
                <div class="hamburger">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </div>
                <div class="logo"><a href="/"><img src="https://www.kulinarika.net/grafika6/logotipi/kul.svg" alt="Kulinarika.net logo"></a></div>
				<form class="search-container" name="FormIskanje" id="FormIskanje" action="/iskanje/" method="GET" autocomplete="off">
					<input type="text" class="search-field" name="splosno_besede" placeholder="Išči recepte...">
					<button type="submit" class="search-submit">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
							<circle cx="11" cy="11" r="8"></circle>
							<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
						</svg>
						Išči
					</button>
					<div class="search-dropdown" style="display: none;">
						<a href="/recepti/seznam/?iskanje=1" class="search-link">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<circle cx="11" cy="11" r="8"></circle>
								<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
							</svg>
							Napredno iskanje po receptih
						</a>
						<a href="/forumi/forum/?vec=1" class="search-link">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<line x1="8" y1="6" x2="21" y2="6"></line>
								<line x1="8" y1="12" x2="21" y2="12"></line>
								<line x1="8" y1="18" x2="21" y2="18"></line>
								<line x1="3" y1="6" x2="3.01" y2="6"></line>
								<line x1="3" y1="12" x2="3.01" y2="12"></line>
								<line x1="3" y1="18" x2="3.01" y2="18"></line>
							</svg>
							Iskanje po forumih
						</a>
					</div>
				</form>
                <div class="mobile-right-icons">
                    <div class="search-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </div>
				
					
				
                    <div class="user-info">
                        <div class="avatar" alt="avatar slika">
                        <span class="ime">prijava</span>
						</div>
                        <div class="user-dropdown" style="display: none;">
							<div class="close-menu">×</div>
							


							 <form action="/mojakulinarika/prijava/" method="post" name="prijava" id="form-prijava" class="form-dizajn1 cf">
							 <h3>Prijava v Kulinarika.net</h3>
								 <div id="mojakulslo-login-wrapper" class="cf">
								 <input type="hidden" name="portal" value="1">
									<label for="loginuser">Uporabnik:</label><input id="loginuser" name="uporabnik" type="text"><br>
									<label for="loginpassword">Geslo:</label><input id="loginpassword" name="geslo" type="password"><br>
								 </div>
							
							
						
					   
							 <input name="Submit" type="submit" class="submit" value="Prijava">
						
								<a href="/mojakulinarika/pozabljeno/" class="noborder">Pozabljeno geslo</a>
						  <a class="noborder" href="/mojakulinarika/vpis/">Nov uporabnik</a>
						
							 </form>

						  
				  

							
							
							
							
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

</div>




<script>
(function() {
    document.addEventListener('DOMContentLoaded', function() {
        const kulGlava = document.getElementById('kul-glava');
        const header = kulGlava.querySelector('.header');
        const navContainer = kulGlava.querySelector('.nav-container');
        const hamburger = kulGlava.querySelector('.hamburger');
        const closeMenuButtons = kulGlava.querySelectorAll('.close-menu');
        const userInfo = kulGlava.querySelector('.user-info');
        const userDropdown = kulGlava.querySelector('.user-dropdown');
        const searchIcon = kulGlava.querySelector('.search-icon');
        const searchContainer = kulGlava.querySelector('.search-container');
        const dropdowns = kulGlava.querySelectorAll('.dropdown-container');
        const searchField = kulGlava.querySelector('.search-field');
        const searchDropdown = kulGlava.querySelector('.search-dropdown');

        let scrollPosition = 0;
        const body = document.body;

        function lockScroll() {
            if (!body.classList.contains('scroll-locked')) {
                scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
                body.classList.add('scroll-locked');
                body.style.overflow = 'hidden';
                body.style.position = 'fixed';
                body.style.top = `-${scrollPosition}px`;
                body.style.width = '100%';
            }
        }

        function unlockScroll() {
            if (body.classList.contains('scroll-locked')) {
                body.classList.remove('scroll-locked');
                body.style.removeProperty('overflow');
                body.style.removeProperty('position');
                body.style.removeProperty('top');
                body.style.removeProperty('width');
                window.scrollTo(0, scrollPosition);
            }
        }

        function closeAllMenus() {
            userDropdown.classList.remove('show');
            userDropdown.style.display = 'none';

            dropdowns.forEach(dropdown => {
                const dropdownContent = dropdown.querySelector('.dropdown-content');
                const dropbtn = dropdown.querySelector('.dropbtn');
                dropdownContent.style.display = 'none';
                dropbtn.classList.remove('active');
            });

            navContainer.classList.remove('show');
            searchContainer.classList.remove('show');

            searchDropdown.classList.remove('show');
            searchDropdown.style.display = 'none';

            unlockScroll();
        }

        function openMenu(menu) {
            menu.classList.add('show');
            document.body.classList.add('menu-open');
            lockScroll();
        }

        function closeMenu(menu) {
            menu.classList.remove('show');
            document.body.classList.remove('menu-open');
            unlockScroll();
        }

        function toggleUserDropdown(e) {
            e.stopPropagation();
            if (window.innerWidth <= 768) {
                userDropdown.style.removeProperty('display');
                userDropdown.classList.toggle('show');
                if (userDropdown.classList.contains('show')) {
                    lockScroll();
                } else {
                    unlockScroll();
                }
            } else {
                userDropdown.classList.remove('show');
                userDropdown.style.display = userDropdown.style.display === 'block' ? 'none' : 'block';
            }
        }

        function handleResize() {
            if (window.innerWidth <= 768) {
                userDropdown.style.removeProperty('display');
                if (userDropdown.classList.contains('show')) {
                    userDropdown.style.display = 'flex';
                }
            } else {
                userDropdown.classList.remove('show');
                userDropdown.style.display = 'none';
                unlockScroll();
            }
        }

        function closeUserDropdown() {
            if (window.innerWidth <= 768) {
                userDropdown.classList.remove('show');
            } else {
                userDropdown.style.display = 'none';
            }
            unlockScroll();
        }

        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            openMenu(navContainer);
        });

        userInfo.addEventListener('click', toggleUserDropdown);

        searchIcon.addEventListener('click', () => {
            searchContainer.classList.toggle('show');
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.dropdown') && !e.target.closest('.user-info') && !navContainer.contains(e.target) && !hamburger.contains(e.target)) {
                dropdowns.forEach(dropdown => {
                    dropdown.querySelector('.dropdown-content').style.display = 'none';
                    dropdown.querySelector('.dropbtn').classList.remove('active');
                });
                closeUserDropdown();
                unlockScroll();
            }
            if (!searchContainer.contains(e.target) && !searchIcon.contains(e.target)) {
                searchContainer.classList.remove('show');
            }
        });

        closeMenuButtons.forEach(button => {
            button.addEventListener('click', () => {
                closeMenu(navContainer);
                closeUserDropdown();
            });
        });

        const userDropdownCloseButton = userDropdown.querySelector('.close-menu');
        if (userDropdownCloseButton) {
            userDropdownCloseButton.addEventListener('click', (e) => {
                e.stopPropagation();
                closeUserDropdown();
            });
        }

        userDropdown.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        dropdowns.forEach(dropdown => {
            const dropbtn = dropdown.querySelector('.dropbtn');
            const dropdownContent = dropdown.querySelector('.dropdown-content');

            dropbtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                if (window.innerWidth <= 768) {
                    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
                    dropbtn.classList.toggle('active');
                    if (dropdownContent.style.display === 'block') {
                        lockScroll();
                    } else {
                        unlockScroll();
                    }
                } else {
                    closeUserDropdown();
                    dropdowns.forEach(otherDropdown => {
                        if (otherDropdown !== dropdown) {
                            otherDropdown.querySelector('.dropdown-content').style.display = 'none';
                            otherDropdown.querySelector('.dropbtn').classList.remove('active');
                        }
                    });
                    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
                    dropbtn.classList.toggle('active');
                }
            });

            dropdownContent.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        });

        searchField.addEventListener('focus', () => {
            searchDropdown.style.display = 'block';
            setTimeout(() => {
                searchDropdown.classList.add('show');
            }, 10);
            closeUserDropdown();
        });

        searchField.addEventListener('blur', (e) => {
            setTimeout(() => {
                if (!searchDropdown.contains(document.activeElement)) {
                    searchDropdown.classList.remove('show');
                    setTimeout(() => {
                        searchDropdown.style.display = 'none';
                    }, 300);
                }
            }, 100);
        });

        document.addEventListener('click', (e) => {
            if (!searchField.contains(e.target) && !searchDropdown.contains(e.target)) {
                searchDropdown.classList.remove('show');
                setTimeout(() => {
                    searchDropdown.style.display = 'none';
                }, 300);
            }
        });

        // New optimized scroll handling
        let lastKnownScrollPosition = 0;
        let ticking = false;
        const SCROLL_THRESHOLD = 5;

        function handleScroll(scrollPos) {
            if (Math.abs(scrollPos - lastKnownScrollPosition) > SCROLL_THRESHOLD) {
                if (scrollPos > lastKnownScrollPosition && scrollPos > 0) {
                    if (!header.classList.contains('header-hidden')) {
                        closeAllMenus();
                    }
                    header.classList.add('header-hidden');
                } else if (scrollPos < lastKnownScrollPosition) {
                    header.classList.remove('header-hidden');
                }
                lastKnownScrollPosition = scrollPos;
            }
        }

        window.addEventListener('scroll', (e) => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    handleScroll(window.scrollY);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        window.addEventListener('resize', debounce(handleResize, 150));
    });

    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            const later = () => {
                clearTimeout(timeout);
                func.apply(this, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
})();
    </script>


<div id="bodyContainer" class="cf">

    <div id="breadcrumbs">
          <div id="breadcrumbsPortal">
               
          </div>
        <!-- InstanceBeginEditable name="breadcrumbs" -->

<p class="breadcrumbs"><a href="/">domov</a> » <a href="/recepti/">recepti</a> » <a href="/recepti/seznam/sladice/">sladice</a> » <a href="/recepti/seznam/sladice/potice/">potice</a> » <span class="trenutno">Orehova potica z rozinami</span></p>
<!-- InstanceEndEditable -->
    
    </div>
<main id="vsebina" class="cf">
<!-- InstanceBeginEditable name="Main" -->

<section id="recepti" class="recept main-left">

<div id="recept-main">

<span style="display:none">božič,martinovo,miklavževo,novo leto,velika noč,pečenje,jesen,pomlad,zima,sladice,Božična večerja in običaji po svetu,Decembrski prazniki in kulinarika,Fala Slonček,Katere 4 jedi ne smejo manjkati na velikonočni miz,Martinovo,Novoletna kulinarika po svetu,Orehova potica,Zajec ne nosi jajc!,Zakaj je Velika noč vsako leto na drug datum?,Zgodba o svetem Miklavžu</span><h1>Orehova potica z rozinami</h1><p class="podnaslov">slovenska klasika</p><div class="podatki linki"><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/ms4mp69e30x9541q/">Fala Slonček</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=Fala Slonček"><img title="Pošljite uporabniku Fala Slonček zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<span class="after1">ogledov: 37 613</span></div><span class="hide"></span> 
   






<div id="fotografije" class="cf">

	

			
			
			<div id="sliderRecepti" class="slider-pro thumbs sp-horizontal" style="width: 100%; max-width: 640px;">

				
			<div class="sp-slides-container"><div class="sp-mask sp-grab" style="width: 640px; height: 480px;"><div class="sp-slides"><div class="sp-slide sp-selected" data-index="0" data-init="true" data-retina-loaded="true" data-loaded="true" style="width: 640px; height: 480px; left: 0px;"><div class="sp-image-container" style="width: 640px; height: 480px; background: rgb(0, 0, 0);"><img class="sp-image" data-default="/slikerecepti/21134/1.webp" alt="Orehova potica z rozinami" title="Orehova potica z rozinami" src="/slikerecepti/21134/1.webp" style="max-width: 900px; max-height: 600px; width: auto; height: 100%; margin-left: -40px; margin-top: 0px;"></div><div class="sp-caption" style="display: none;"><p class="desc"><span class="datum">1.12.2016 | </span> <a class="username" href="/uporabniki/seznam/ms4mp69e30x9541q/">Fala Slonček</a></p></div></div><div class="sp-slide" data-index="1" data-init="true" data-retina-loaded="true" data-loaded="true" style="width: 640px; height: 480px; left: 650px;"><div class="sp-image-container" style="width: 640px; height: 480px; background: rgb(0, 0, 0);"><img class="sp-image" data-default="/slikerecepti/21134/3.webp" alt="placeholder" src="/slikerecepti/21134/3.webp" style="max-width: 900px; max-height: 675px; width: 100%; height: auto; margin-left: 0px; margin-top: 0px;"></div><div class="sp-caption" style="display: none;"><p class="desc"><span class="datum">22.1.2018 | </span> <a class="username" href="/uporabniki/seznam/liiu/">Liiu</a></p></div></div><div class="sp-slide" data-index="2" data-init="true" data-retina-loaded="true" style="width: 640px; height: 480px; left: 1300px;"><div class="sp-image-container" style="width: 640px; height: 480px; background: rgb(0, 0, 0);"><img class="sp-image" src="/css/slider-pro-images/blank.gif" alt="placeholder" data-src="/slikerecepti/21134/2.webp" data-default="/slikerecepti/21134/2.webp"></div><div class="sp-caption" style="display: none;"><p class="desc"><span class="datum">22.1.2018 | </span> <a class="username" href="/uporabniki/seznam/liiu/">Liiu</a></p></div></div></div></div><div class="sp-arrows sp-fade-arrows"><div class="sp-arrow sp-previous-arrow" style="display: none;"></div><div class="sp-arrow sp-next-arrow" style="display: block;"></div></div></div><div class="sp-thumbnails-container sp-bottom-thumbnails" style="width: 428px;"><div class="sp-thumbnails sp-grab" style="width: 428px; height: 105px;"><div class="sp-thumbnail-container sp-selected-thumbnail" data-loaded="true" data-retina-loaded="true" style="width: 140px; height: 105px;"><img class="sp-thumbnail" data-init="true" data-index="0" alt="Fotografija recepta: Orehova potica z rozinami" src="/slikerecepti/21134/1-200x150.webp" style="width: 100%; height: auto; margin-left: 0px; margin-top: -1px;"></div><div class="sp-thumbnail-container" data-retina-loaded="true" data-loaded="true" style="width: 140px; height: 105px;"><img class="sp-thumbnail" data-init="true" data-index="1" alt="Fotografija recepta: Orehova potica z rozinami" src="/slikerecepti/21134/3-200x150.webp" style="width: 100%; height: auto; margin-left: 0px; margin-top: 0px;"></div><div class="sp-thumbnail-container" data-retina-loaded="true" data-loaded="true" style="width: 140px; height: 105px;"><img class="sp-thumbnail" data-init="true" data-index="2" alt="Fotografija recepta: Orehova potica z rozinami" src="/slikerecepti/21134/2-200x150.webp" style="width: 100%; height: auto; margin-left: 0px; margin-top: 0px;"></div></div><div class="sp-thumbnail-arrows sp-fade-thumbnail-arrows"><div class="sp-thumbnail-arrow sp-previous-thumbnail-arrow" style="display: none;"></div><div class="sp-thumbnail-arrow sp-next-thumbnail-arrow" style="display: none;"></div></div></div><div class="sp-caption-container" style="opacity: 1;"><p class="desc"><span class="datum">1.12.2016 | </span> <a class="username" href="/uporabniki/seznam/ms4mp69e30x9541q/">Fala Slonček</a></p></div><div class="sp-full-screen-button sp-fade-full-screen"></div><div class="counter"><span class="active">1</span>/3</div></div> 	
				</div><ul class="servis cf linki"><span style="display:none">sladice: potice</span><li class="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"></li><li><img class="ura" src="/grafika6/ikona-ura.png" alt="1 ura" title="1 ura">&nbsp;<span class="cas">1 ura</span><time datetime="PT60M"></time></li><li id="ocene"><a href="/inc/popup-ocene.asp?ID=21134" id="popup-oceneseznam-holder" data-type="ajax" data-width="340" data-height="500" data-fullscreen_mobile="true" title="Ocenite recept" class="vbox-item"><img src="/grafika6/ikona-ocena.png" title="2 oceni">&nbsp;<span title="povprečna ocena: 5">5</span></a></li><li class="zanimivosti"><a href="/inc/ajax-funkcije.asp?akcija=recepti-zanimivosti&amp;ID=21134" id="popup-zanimivosti-holder" data-type="ajax" data-width="300" data-height="290" data-fullscreen_mobile="true" class="vbox-item"><img title="Zanimivosti" alt="Zanimivosti" src="/grafika7/icon-info.svg" width="24" height="24"></a></li>

</ul>

<ul class="priljubljeni"><a class="neopazen vbox-item" href="/inc/popup-prispevaj.asp?id=21134" id="popup-prispevaj-holder" data-type="ajax" data-width="300" data-height="290" data-fullscreen_mobile="true" title="Prispevaj" alt="Prispevaj"><li><img title="prispevajte" src="/grafika7/icon-add-photo.svg" height="24">&nbsp;Prispevaj</li></a><a class="neopazen" href="/mojakulinarika/nisemclan/"><li><img src="/grafika7/icon-heart-off.svg" title="shranite med priljubljene" height="28">&nbsp;Shrani</li></a><a class="neopazen" href="/recepti/tiskanje/?id=21134" target="_blank"><li><img title="natisnite recept" src="/grafika7/icon-printer.svg" height="24">&nbsp;Natisni</li></a></ul>

<div id="uvod" class="linki">

	

</div>




<div id="receptSestavine"><h2>Sestavine

<span id="ingredientsShare" style="display: inline-block;">
<img title="shranite sestavine" src="/grafika7/icon-share.svg" height="36">
</span>

</h2>

      <div id="sestavine" class="articlesize linki ">
        
           <p class="cf poglavje" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>Testo:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">½ kocke </span><span class="label-value"><a href="https://www.facebook.com/fala.sloncek?fref=ts" target="_blank">kvasa Fala</a></span></p><p class="cf" itemprop="recipeIngredient"><span class="label">2 dl </span><span class="label-value">mleka</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">48 dag </span><span class="label-value">moke</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">10 dag </span><span class="label-value">kisle smetane</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">10 dag </span><span class="label-value">masla</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">4 dag </span><span class="label-value">sladkorja</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">2 </span><span class="label-value">rumenjaka</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">1,5 male žličke </span><span class="label-value">soli</span></p> <p class="cf poglavje" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>Nadev:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">40 dag </span><span class="label-value">orehov</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">15 dag </span><span class="label-value">sladkorja</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">2 dl </span><span class="label-value">mleka</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">2 </span><span class="label-value">beljaka</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">1 žlica </span><span class="label-value">mlete kave</span></p><p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value">sok polovice limone</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value">lupinica cele limone</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">10 dag </span><span class="label-value">rozin</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label"></span><span class="label-value">jajce za premaz</span></p> 
</div>




</div>


<label class="toggle hide_important" id="zaslon">
	<input class="toggle-checkbox" type="checkbox">
	<div class="toggle-switch"></div>
	<p class="toggle-label">Način za kuhanje</p>
</label>

<div id="oglas300LuknjaRecept"></div>

  <div id="receptPostopek"><h2>Postopek</h2>

    <div id="postopek" class="articlesize linki ">

  <div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data"><a href="https://www.facebook.com/fala.sloncek?fref=ts" target="_blank">kVas Fala</a> in sladkor raztopimo v toplem mleku. V posodo odmerimo sol, moko, kislo smetano, dodamo rumenjake in zamesimo kvašeno testo. Med mešanjem dodajamo na lističe narezano maslo. Ko so sestavine res dobro povezane med seboj in je testo gladko, posodo pokrijemo in damo testo na toplo vzhajati.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Med vzhajanjem pripravimo nadev. Mlete orehe zmešamo s kavo in polovico sladkorja ter jih poparimo z vrelim mlekom ter dobro premešamo. Beljaka stepemo v trd sneg ob postopnem dodajanju preostalega sladkorja. V mlačen nadev vmešamo limonin sok, lupinico in sneg.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Vzhajano testo stresemo na pult, ga pregnetemo in pustimo počivati nekaj minut. Nato testo razvaljamo, ga premažemo z nadevom, posujemo rozine in tesno zvijemo v zavitek. Tega položimo v pomaščen model in damo na toplo vzhajati.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf fullwidth en_korak_postopek" itemprop="text"><span class="label"></span><span class="data">Vzhajano potico premažemo s stepenim jajcem, na več mestih prebodemo in prestavimo v vročo pečico. Potico pečemo približno eno uro pri 180 °C. Po potrebi jo pokrijemo, da bi se na vrhu ne zapekla preveč. Ko jo pokrijemo, moramo na foliji narediti na sredini luknjo, da bo zrak lahko krožil skozi odprtino modela. Sicer lahko ostane na sredini potica premalo pečena.</span></p></div></div></div><br class="clear"><div id="videooglas" class="" style="height: 360px; display: block;"><iframe id="banner25" name="banner25" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="640" height="480" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=25&amp;kanal=recepti&amp;kat=sladice&amp;podkat=potice&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,3546107" style="overflow: hidden; transform: scale(1); height: 360px;"></iframe><script>$(document).ready(function() {$('#banner25').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=25&kanal=recepti&kat=sladice&podkat=potice&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,3546107');});</script></div><div id="opombe" class="articlesize linki"><h2>Opombe</h2> <p>SPONZORIRANO SPOROČILO</p></div><section id="vino_container" class="Najnovejsi cf"><h2><a class="linki3" href="/vino/?kategorija=18&amp;kategorija1=137">Predlogi za vino</a></h2><div class="vinoslider flickity-enabled is-draggable" tabindex="0" style="visibility: visible;"><div class="flickity-viewport" style="touch-action: pan-y;"><div class="flickity-slider" style="left: 0px; transform: translateX(0%);"><article class="carousel-cell vino is-selected" style="position: absolute; left: 0px; transform: translateX(0%);"><a href="/vino/117/"><div class="flex"><img alt="fotografija vina" src="/slike/vino/c2zfbxaz9bq6hm63_small.png" data-src="/slike/vino/c2zfbxaz9bq6hm63_small.png" data-sizes="auto" data-srcset="/slike/vino/c2zfbxaz9bq6hm63_small.png 50w, /slike/vino/c2zfbxaz9bq6hm63.png" class="mala50 enovino lazyautosizes lazyloaded" sizes="50px" srcset="/slike/vino/c2zfbxaz9bq6hm63_small.png 50w, /slike/vino/c2zfbxaz9bq6hm63.png"><img alt="logotip vinarja" class="vinar" src="/slike/vinar/1zfnvf74.png"></div></a><p class="ime single-line textLeft"><a href="/vino/117/">Ventus Chardonnay</a></p></article><article class="carousel-cell vino" aria-hidden="true" style="position: absolute; left: 0px; transform: translateX(94.44%);"><a href="/vino/98/"><div class="flex"><img alt="fotografija vina" src="/slike/vino/kzkw9yszyal927g9_small.jpg" data-src="/slike/vino/kzkw9yszyal927g9_small.jpg" data-sizes="auto" data-srcset="/slike/vino/kzkw9yszyal927g9_small.jpg 50w, /slike/vino/kzkw9yszyal927g9.jpg" class="mala50 enovino lazyautosizes lazyloaded" sizes="50px" srcset="/slike/vino/kzkw9yszyal927g9_small.jpg 50w, /slike/vino/kzkw9yszyal927g9.jpg"><img alt="logotip vinarja" class="vinar" src="/slike/vinar/hc3a48dy.png"></div></a><p class="ime single-line textLeft"><a href="/vino/98/">Rumeni muškat – verduc Quercus</a></p></article></div></div><button class="flickity-button flickity-prev-next-button previous" type="button" disabled="" aria-label="Previous"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow"></path></svg></button><button class="flickity-button flickity-prev-next-button next" type="button" aria-label="Next"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow" transform="translate(100, 100) rotate(180) "></path></svg></button><ol class="flickity-page-dots"><li class="dot is-selected" aria-label="Page dot 1" aria-current="step"></li><li class="dot" aria-label="Page dot 2"></li></ol></div><p class="vec"><a class="linki3" href="/vino/?kategorija=18&amp;kategorija1=137">Več predlogov </a></p></section>



</div>

<ul id="servis2" class="servis clearfix">

	<span class=""><a href="/recepti/seznam/?priloznost=2">#božič</a><a href="/recepti/seznam/?priloznost=1">#martinovo</a><a href="/recepti/seznam/?priloznost=9">#miklavževo</a><a href="/recepti/seznam/?priloznost=6">#novo leto</a><a href="/recepti/seznam/?priloznost=5">#velika noč</a></span><span class=""><a href="/recepti/seznam/?letnicas=3">#jesen</a><a href="/recepti/seznam/?letnicas=1">#pomlad</a><a href="/recepti/seznam/?letnicas=4">#zima</a></span><span class=""><a href="/recepti/seznam/?vrstajedi=3">#sladice</a></span>



    </ul>

<ul class="servis cf linki"><li><a rel="noreferrer" href="https://www.facebook.com/sharer.php?u=https://www.kulinarika.net/recepti/sladice/potice/orehova-potica-z-rozinami/21134/" target="_blank"><img src="/grafika7/icon-facebook.svg" height="36" title="pošljite na Facebook"></a></li><li><a rel="noreferrer" href="https://twitter.com/intent/tweet?text=Orehova+potica+z+rozinami%3A+&amp;url=https://www.kulinarika.net/recepti/sladice/potice/orehova-potica-z-rozinami/21134/" target="_blank"><img title="pošljite na Twitter" src="/grafika7/icon-twitter.svg" height="36"></a></li><li id="webShare" style="display: inline-block;"><img title="delite recept" src="/grafika7/icon-share.svg" height="36"></li><li><a class="link prijatelj" id="posljiprijatelju" href="mailto:?subject=Zanimiv%20recept%20na%20KULINARIKA%2ENET&amp;body=Pozdravljen%2Da%21%0D%0A%0D%0ANa%20strani%20KULINARIKA%2Enet%20sem%20zasledil%28a%29%20zanimiv%20recept%2C%20ki%20bi%20te%20morda%20zanimal%28a%29%3A%0D%0A%0D%0Ahttps%3A%2F%2Fwww%2Ekulinarika%2Enet/recepti/sladice/potice/orehova-potica-z-rozinami/21134/"><img title="pošljite po emailu" alt="pošljite po emailu" src="/grafika7/icon-email.svg" height="24"></a></li></ul>

    



	<div id="malioglasi" class="cf">
    
    
    
    </div>

<div id="mnenja-container"><h2>Mnenja o receptu</h2><section id="mnenja" class="odprto">
										  <div class="telo2 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="1"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/Katrin11/">katrin11</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=katrin11"><img title="Pošljite uporabniku katrin11 zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 3.1.2010</p>
                                                 <p class="stevilo no-mobile">Št. objav: 2368</p>
												  </div><div class="msgbody"> <p>Tole je taprava potica, nadev in testo po pečenju 50/50! </p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  
										  <div class="telo1 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="2"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/ssilva/">ssilva</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=ssilva"><img title="Pošljite uporabniku ssilva zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 23.2.2005</p>
                                                 <p class="stevilo no-mobile">Št. objav: 428</p>
												  </div><div class="msgbody"> <p>Odlična! Ničesar preveč in ničesar premalo.</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  
										  <div class="telo2 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="3"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/liiu/">Liiu</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=Liiu"><img title="Pošljite uporabniku Liiu zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 18.7.2010</p>
                                                 <p class="stevilo no-mobile">Št. objav: 363</p>
												  </div><div class="msgbody">
                                                  <img src="/grafika/smile_veselje.gif" alt="Vesel" width="23" height="18" align="absbottom"> 
                                                   <p>Več receptov sem že ,,probala,, vendar mi je ta najboljši.</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"><a href="/inc/ajax-funkcije.asp?akcija=mnenja_likes&amp;s=1&amp;IDMnenje=138414&amp;rand=20250404184914" class="popup-likes-holder">1</a></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  
										  <div class="telo1 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="4"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/jgrdadolnik/">jgrdadolnik</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=jgrdadolnik"><img title="Pošljite uporabniku jgrdadolnik zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 7.2.2010</p>
                                                 <p class="stevilo no-mobile">Št. objav: 2</p>
												  </div><div class="msgbody"> <p>Lahko bi bilo več orehov  in kakšna rozina vmes.</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  </section><div class="preberivec linki" style="display: none;"><a href="javascript:void(null)">preberi več</a></div><p class="navigacijazg">Število mnenj: 4, prikazujem mnenja  od 1 do 4</p>

											<div id="pisite_skok"></div>
											
											<span class="pomembno">Za pošiljanje mnenj je potreben <a href="/mojakulinarika/vpis/">vpis</a> ali
											 <a href="/mojakulinarika/prijava/">prijava</a>!</span> 
											 
	
		<script>
		
			$(document).ready(function() {
	
				
				
				$(document).on("click", ".preberivec", function() {	
						$('#mnenja').addClass('odprto');
						$('.preberivec').hide();
				})


				if ($('#mnenja').height()>350 && isMobile)
					{
						$('#mnenja').removeClass('odprto');
						$('.preberivec').show();
					}
					
					else
					
					{
						$('.preberivec').hide();
					}
	
	})
		
		
		</script>
			
</div>
      
    </section>
	

<!-- InstanceEndEditable -->
<section id="servisniBlok" class="recepti">
<!-- InstanceBeginEditable name="neboticnik" -->

<div id="nadOglas">

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-pravila">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Pogoji sodelovanja v nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-nagrade">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Več o nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-nagrade-old">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Več o potekli nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-sponzor">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">O pokrovitelju nagradne igre</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>

</div><aside class="velikanoc cf" id="info-praznik"><div class="container"><div class="recepti"><h2><a class="linki3" href="/recepti/seznam/?sort=popularnost&amp;nacin=desc&amp;priloznost=5">Velikonočne jedi</a></h2><a class="linki3" href="/recepti/sladice/potice/orehova-potica/1176/">Orehova potica</a><a class="linki3" href="/recepti/sladice/potice/kokosova-potica/4255/">Kokosova potica</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica-st-2/1667/">Potratna potica št. 2</a><a class="linki3" href="/recepti/sladice/potice/orehova-rulada/5737/">Orehova rulada</a><a class="linki3" href="/recepti/sladice/potice/nocna-potica/2889/">Nočna potica</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica/18232/">Potratna potica</a><a class="linki3" href="/recepti/sladice/potice/pehtranova-potica/378/">Pehtranova potica</a><a class="linki3" href="/recepti/sladice/potice/marmorni-kolac-iz-jogurta-/14691/">Marmorni kolač (iz jogurta)</a><a class="linki3" href="/recepti/sladice/potice/domaci-prijatelj-tete-dragice/12332/">Domači prijatelj tete Dragice</a><a class="linki3" href="/recepti/sladice/potice/vsestransko-testo/11944/">Vsestransko testo</a><a class="linki3" href="/recepti/sladice/potice/krhka-pita-za-vsak-okus/6439/">Krhka pita za vsak okus</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica/1390/">Potratna potica</a></div></div><p class="vec"><a class="linki3" href="/recepti/seznam/?sort=popularnost&amp;nacin=desc&amp;priloznost=5">več receptov za Veliko noč</a></p></aside><div class="cf" id="oglasi-stranski"><div id="oglas-aside2" class=""><iframe id="banner3" name="banner3" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="300" height="600" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=3&amp;kanal=recepti&amp;kat=sladice&amp;podkat=potice&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,7624583"></iframe><script>$(document).ready(function() {$('#banner3').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=3&kanal=recepti&kat=sladice&podkat=potice&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,7624583');});</script></div></div><aside class="ReceptiVroci cf"><h2><a href="/recepti/seznam/?avtor=Fala Slonček">Več receptov - Fala Slonček</a></h2><div class="mobileslider najboljvroci" style="visibility: visible;"><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/potice/cokoladna-pogaca-s-cimetom/22070/"><img alt="fotografija recepta" src="/slikerecepti/22070/1-200x150.webp" data-src="/slikerecepti/22070/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/22070/1-200x150.webp 200w, /slikerecepti/22070/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/22070/1-200x150.webp 200w, /slikerecepti/22070/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/potice/cokoladna-pogaca-s-cimetom/22070/">Čokoladna pogača s cimetom</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/skutno-pecivo-s-cokolado-in-malinami/22634/"><img alt="fotografija recepta" src="/slikerecepti/22634/1-200x150.webp" data-src="/slikerecepti/22634/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/22634/1-200x150.webp 200w, /slikerecepti/22634/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/22634/1-200x150.webp 200w, /slikerecepti/22634/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/skutno-pecivo-s-cokolado-in-malinami/22634/">Skutno pecivo s čokolado in malinami</a></div><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/flancati/21442/"><img alt="fotografija recepta" src="/slikerecepti/21442/2-200x150.webp" data-src="/slikerecepti/21442/2-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/21442/2-200x150.webp 200w, /slikerecepti/21442/2-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/21442/2-200x150.webp 200w, /slikerecepti/21442/2-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/flancati/21442/">Flancati</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/sladice/potice/makova-potica-s-suhimi-slivami/21520/"><img alt="fotografija recepta" src="/slikerecepti/21520/1-200x150.webp" data-src="/slikerecepti/21520/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/21520/1-200x150.webp 200w, /slikerecepti/21520/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/21520/1-200x150.webp 200w, /slikerecepti/21520/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/potice/makova-potica-s-suhimi-slivami/21520/">Makova potica s suhimi slivami</a></div><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/"><img alt="fotografija recepta" src="/slikerecepti/21526/1-200x150.webp" data-src="/slikerecepti/21526/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/21526/1-200x150.webp 200w, /slikerecepti/21526/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/21526/1-200x150.webp 200w, /slikerecepti/21526/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/">Rogljički s skuto </a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/kruh/sladke-velikonocne-pogacice/22485/"><img alt="fotografija recepta" src="/slikerecepti/22485/1-200x150.webp" data-src="/slikerecepti/22485/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/22485/1-200x150.webp 200w, /slikerecepti/22485/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/22485/1-200x150.webp 200w, /slikerecepti/22485/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/kruh/sladke-velikonocne-pogacice/22485/">Sladke velikonočne pogačice</a></div></div></aside><div id="zid-include"></div>

    <div class="highslide-html-content highslide-my-standard-popup" id="prijatelj">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Pošlji prijatelju</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="my-ocena">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Ocenite recept</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="ocenerecepta">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Ocene recepta</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="pomoc-priporocamo">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Zraven tekne</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="pomoc-vino">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Vinski kotiček</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popupSubscribed">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Naročeni ste na nova mnenja</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body ">Ko bo nekdo napisal novo mnenje k temu receptu, boste o tem dobili e-mail obvestilo (le enkrat, dokler ne odprete spet tega recepta). Na naročanje se lahko odjavite na samem receptu ali pa iz beležke.</div>
    
    </div>


    <!-- InstanceEndEditable -->
</section>
</main>
</div>
<div class="push"></div>
</div>



<footer class="footer cf">

<!-- The Modal -->
	<div id="myModal" class="modal">

	  <!-- Modal content -->
	  <div class="modal-content">
	    	<div class="img_wrap"><img alt="prazno" src="/images/prazno.jpg"></div>
	    	<div class="txt_wrap">
	    		<h3>Zaznan je blokator oglasov</h3>
				<p>Vsebina Kulinarika.net je podprta z oglaševanjem. Če želite še naprej uživati v naših receptih, izklopite blokiranje oglasov.</p>
				<h4>Prosimo vas, da za našo spletno stran onemogočite blokiranje oglasov.</h4>
				<!-- <p>Onemogoči blokiranje oglasov<p> -->
				<a href="javascript:void(0);" class="close_modal">Nadaljujte z blokiranjem oglasov</a>
			</div>
	  </div>

	</div>

    <div id="footer-top">
      
    </div>
	<div class="cf" id="footer-main">
	<p>© 2025 Spletna kulinarika d.o.o.</p>
	<ul>
    
		<li><a href="/oglasevanje/">Trženje</a></li>	
		<li><a href="/pravo/">Pogoji uporabe</a></li>
		<li><a href="/zasebnost/">Zasebnost</a></li>
		
   		<li><a href="/faq/">Pomoč</a></li>
        <li><a href="/zanimivo/dogodki/">Dogodki</a></li>
        
		<li><a href="/uporabniki/seznam/">Člani</a></li>
	</ul>
</div>

  
</footer>

<script>
<!--//<![CDATA[
if (isMobile == true) {
var ox_u = 'https://oglasi2.kulinarika.net/www/delivery/al.php?zoneid=24&layerstyle=simple&align=left&valign=top&padding=0&padding=0&shifth=0&shiftv=0&closebutton=t&nobg=t&noborder=t';
if (document.context) ox_u += '&context=' + escape(document.context);
document.write("<scr"+"ipt src='" + ox_u +"'></scr"+"ipt>");
}
//]]>--></script>

<div id="bottomAdWrapper">

        <div id="adContainer" style="height: 128.711px; visibility: visible; bottom: 0px;">
            <div id="closeButton"></div>
            <div id="scaleContainer" style="transform: scale(0.494845); width: 970px; height: 250px;">
                <iframe id="banner1" name="banner1" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="980" height="250" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=1&amp;kanal=recepti&amp;kat=sladice&amp;podkat=potice&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=5,376232E-02"></iframe><script>$(document).ready(function() {$('#banner1').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=1&kanal=recepti&kat=sladice&podkat=potice&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=5,376232E-02');});</script>
            </div>
        </div>
</div>

<script>
        // Create a namespace for the ad functionality
        const bottomAD = window.bottomAD || {};

        (function(namespace) {
            function showAd() {
                const adContainer = document.getElementById('adContainer');
                if (adContainer) {
                    adContainer.style.visibility = 'visible';
                    adContainer.style.bottom = '0';
                }
            }

            function hideAd() {
                const adContainer = document.getElementById('adContainer');
                if (adContainer) {
                    adContainer.style.bottom = '-250px';
                }
            }

            function debounce(func, wait) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        clearTimeout(timeout);
                        func(...args);
                    };
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                };
            }

			function resizeAd() {
				const scaleContainer = document.getElementById('scaleContainer');
				const adContainer = document.getElementById('adContainer');
				
				if (!scaleContainer || !adContainer) {
					console.error('One or more ad elements not found');
					return;
				}

				try {
					const windowWidth = window.innerWidth;
					const maxWidth = 480;
					const originalWidth = 970;
					const originalHeight = 250;

					const scale = Math.min(maxWidth, windowWidth) / originalWidth;
					const scaledHeight = originalHeight * scale;

					scaleContainer.style.transform = `scale(${scale})`;
					scaleContainer.style.width = `${originalWidth}px`;
					scaleContainer.style.height = `${originalHeight}px`;
					adContainer.style.height = `${scaledHeight + 5}px`; // 5px for padding
				} catch (error) {
					console.error('Error resizing ad:', error);
				}
			}

            // Expose functions in the namespace
            namespace.showAd = showAd;
            namespace.hideAd = hideAd;

            // Trigger the ad after 5 seconds (as an example)
            setTimeout(namespace.showAd, 5000);

            // Add debounced event listener for resizing
            const debouncedResize = debounce(resizeAd, 250);
            window.addEventListener('resize', debouncedResize);
            resizeAd(); // Initial resize

            // Close button event listener
            const closeButton = document.getElementById('closeButton');
            if (closeButton) {
                closeButton.addEventListener('click', namespace.hideAd);
            }
        })(bottomAD);
    </script>


</div><ins class="adsbygoogle adsbygoogle-noablate" style="display: none !important;" data-adsbygoogle-status="done" data-ad-status="unfilled"><div id="aswift_0_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?client=ca-pub-3352501607232481&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;abgtt=8&amp;lmt=1743785354&amp;plat=1%3A16777216%2C2%3A16777216%2C3%3A65536%2C4%3A65536%2C9%3A134250504%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1048576%2C32%3A32%2C41%3A32%2C42%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.kulinarika.net%2Frecepti%2Fsladice%2Fpotice%2Forehova-potica-z-rozinami%2F21134%2F&amp;pra=5&amp;wgl=1&amp;aihb=0&amp;asro=0&amp;ailel=1~2~4~7~8~9~10~11~12~13~14~15~16~17~18~19~20~21~24~29~30~34&amp;aiael=1~2~3~4~7~8~9~10~11~12~13~14~15~16~17~18~19~20~21~24~29~30~34&amp;aicel=33~38&amp;aifxl=29_18~30_19&amp;aiixl=29_5~30_6&amp;itsi=-1&amp;aiapm=0.15&amp;aiapmi=0.33938&amp;aiact=0.7&amp;ailct=0.7&amp;uach=WyJtYWNPUyIsIjEzLjQuMCIsImFybSIsIiIsIjEzMy4wLjY5NDMuMTI3IixudWxsLDAsbnVsbCwiNjQiLFtbIk5vdChBOkJyYW5kIiwiOTkuMC4wLjAiXSxbIkdvb2dsZSBDaHJvbWUiLCIxMzMuMC42OTQzLjEyNyJdLFsiQ2hyb21pdW0iLCIxMzMuMC42OTQzLjEyNyJdXSwwXQ..&amp;dt=1743785354806&amp;bpp=1&amp;bdt=117&amp;idt=38&amp;shv=r20250403&amp;mjsv=m202504010101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eoidce=1&amp;nras=1&amp;correlator=1747197056559&amp;frm=20&amp;pv=2&amp;u_tz=120&amp;u_his=4&amp;u_h=956&amp;u_w=1470&amp;u_ah=850&amp;u_aw=1470&amp;u_cd=30&amp;u_sd=2&amp;dmc=8&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1179&amp;bih=763&amp;scr_x=0&amp;scr_y=0&amp;eid=95355973%2C95355975%2C95356626&amp;oid=2&amp;pvsid=1002798879007172&amp;tmod=1545610094&amp;uas=0&amp;nvt=1&amp;fsapi=1&amp;ref=https%3A%2F%2Fwww.kulinarika.net%2Frecepti%2Fseznam%2Fsladice%2F&amp;fc=1920&amp;brdim=-7%2C37%2C-7%2C37%2C1470%2C37%2C1552%2C850%2C1179%2C763&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;bz=1.32&amp;td=1&amp;tdf=2&amp;nt=1&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;dtd=42" data-google-container-id="a!1" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true"></iframe></div></ins>

<!-- InstanceBeginEditable name="dno" -->

<script>
const bannerModule = (function() {
    let lastKnownScrollPosition = 0;
    let ticking = false;
    let container, iframe, bottomBanner;
    let isParallaxVisible = true;
    let parallaxActive = window.innerWidth < 768;

    function easeInOutCubic(t) {
        return t < 0.5
            ? 4 * t * t * t
            : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }

    function resetStyles() {
        if (iframe) {
            iframe.style.transform = '';
        }
        if (bottomBanner) {
            bottomBanner.style.opacity = '';
        }
    }

    function updateParallax() {
        if (!parallaxActive) return;
        if (!isParallaxVisible) return;
        const containerRect = container.getBoundingClientRect();
        const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
        const scrollPercentage =
            (viewportHeight - containerRect.top) /
            (viewportHeight + containerRect.height);
        // Parallax effect
        if (scrollPercentage > 0 && scrollPercentage < 1) {
            const easedScrollPercentage = easeInOutCubic(scrollPercentage);
            const moveY =
                (easedScrollPercentage - 0.5) * containerRect.height * 0.5;
            iframe.style.transform = `translate(-50%, -50%) translateY(${moveY}px)`;
        }
        // Bottom banner visibility
        const buffer = 200; // Buffer for smoother transition
        let opacity = 1;
        if (containerRect.bottom > 0 && containerRect.top < viewportHeight) {
            opacity = 0;
        } else if (containerRect.bottom <= 0) {
            opacity = Math.min(1, (-containerRect.bottom) / buffer);
        } else if (containerRect.top >= viewportHeight) {
            opacity = Math.min(1, (containerRect.top - viewportHeight) / buffer);
        }
        opacity = Math.max(0, Math.min(1, opacity));
        bottomBanner.style.opacity = opacity;
        ticking = false;
    }

    function onScroll() {
        lastKnownScrollPosition = window.pageYOffset;
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateParallax();
            });
            ticking = true;
        }
    }

    function toggleParallax() {
        isParallaxVisible = !isParallaxVisible;
        container.style.display = isParallaxVisible ? 'block' : 'none';
        bottomBanner.style.display = isParallaxVisible ? 'flex' : 'none';
        if (isParallaxVisible) {
            updateParallax();
        }
    }

    function onResize() {
        let newParallaxActive = window.innerWidth < 768;
        if (newParallaxActive && !parallaxActive) {
            // Switched from desktop to mobile
            parallaxActive = true;
            init();
        } else if (!newParallaxActive && parallaxActive) {
            // Switched from mobile to desktop
            parallaxActive = false;
            // Reset styles and remove event listeners
            resetStyles();
            window.removeEventListener('scroll', onScroll);
        }
    }

    function init() {
        container = document.querySelector('#oglas-aside2');
        iframe = document.querySelector('#banner3');
        bottomBanner = document.querySelector('#adContainer');

        if (window.innerWidth >= 768) {
            // Reset styles on larger screens
            resetStyles();
            parallaxActive = false;
            return;
        }
        parallaxActive = true;
        window.addEventListener('scroll', onScroll, { passive: true });
        // Initial update
        updateParallax();
    }

    // Public methods
    return {
        init: init,
        toggleParallax: toggleParallax,
        onResize: onResize
    };
})();

// Initialize the module
document.addEventListener('DOMContentLoaded', function() {
    bannerModule.init();
    window.addEventListener('resize', bannerModule.onResize);
});
    </script>

<!-- InstanceEndEditable -->
<a href="#0" class="cd-top cd-is-visible cd-fade-out" title="na vrh">↑</a>


<div id="ad-container" class="ad-container"></div></body><!-- InstanceEnd --><iframe id="google_esf" name="google_esf" src="https://pagead2.googlesyndication.com/pagead/html/r20250403/r20190131/zrt_lookup_fy2021.html" style="display: none;"></iframe></html>

"""

html3 = """
<html lang="sl"><!-- InstanceBegin template="/Templates/ogrodje3.dwt.asp" codeOutsideHTMLIsLocked="false" --><head>
<meta charset="utf-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

/* Raleway Light */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  src: url('/fonts/Raleway-Light.woff2') format('woff2');
  font-display: swap;
}

/* Raleway Regular */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 400;
  src: url('/fonts/Raleway-Regular.woff2') format('woff2');
  font-display: swap;
}

/* Raleway Italic */
@font-face {
  font-family: 'Raleway';
  font-style: italic;
  font-weight: 400;
  src: url('/fonts/Raleway-Italic.woff2') format('woff2');
  font-display: swap;
}

/* Raleway SemiBold */
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 600;
  src: url('/fonts/Raleway-SemiBold.woff2') format('woff2');
  font-display: swap;
}

</style>

<link href="/css/normalize.css" rel="stylesheet" type="text/css">
<link href="/css/skupaj-css.css?rel=4.0502524229335" rel="stylesheet" type="text/css">
<link href="/stiliprint.css" rel="stylesheet" type="text/css" media="print">


<link rel="stylesheet" href="/css/flickity.css" media="screen">

<script type="text/javascript" async="" src="https://www.google-analytics.com/plugins/ua/linkid.js"></script><script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202504010101/show_ads_impl_with_ama_fy2021.js?client=ca-pub-3352501607232481&amp;plah=www.kulinarika.net"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script src="/js/lazysizes.min.js" async=""></script>
<link href="/css/new-responsive.css?v=1.03" rel="stylesheet" type="text/css">

<link rel="apple-touch-icon" sizes="180x180" href="/grafika6/favicons/apple-touch-icon.png">
<link rel="icon" type="image/png" href="/grafika6/favicons/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/grafika6/favicons/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="/grafika6/favicons/manifest.json">
<link rel="mask-icon" href="/grafika6/favicons/safari-pinned-tab.svg" color="#5bbad5">
<link rel="shortcut icon" href="/grafika6/favicons/favicon.ico">
<meta name="msapplication-config" content="/grafika6/favicons/browserconfig.xml">
<meta name="theme-color" content="#ffffff">

<meta property="og:locale" content="sl_SI">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kulinarika.net">
<meta property="fb:app_id" content="182018238801081">





<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "WebSite",
  "name": "Kulinarika.net",
  "url": "http://www.kulinarika.net",
  "image": "http://www.kulinarika.net/grafika6/logotipi/logo4.png",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.kulinarika.net/iskanje/?splosno_besede={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}

</script>

<link href="/css/recepti.css?v=4.0502524229335" rel="stylesheet" type="text/css">
<!-- InstanceBeginEditable name="stili" -->

<!-- InstanceEndEditable -->


<script>

	

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-15823371-4', {'storage': 'none', 'clientId': 'c9993b1a8e5f8da0d8b8de4e2140076d'});
  ga('require', 'linkid', 'linkid.js');
  ga('require', 'displayfeatures');

	
	// Creates an adblock detection plugin.
	ga('provide', 'adblockTracker', function(tracker, opts) {
	  var ad = document.createElement('ins');
	  ad.className = 'AdSense';
	  ad.style.display = 'block';
	  ad.style.position = 'absolute';
	  ad.style.top = '-1px';
	  ad.style.height = '1px';
	  document.body.appendChild(ad);
	  tracker.set('dimension' + opts.dimensionIndex, !ad.clientHeight);
	  document.body.removeChild(ad);
	});
	
	ga('require', 'adblockTracker', {dimensionIndex: 1});
    ga('send', 'pageview'), {'anonymizeIp': true};
  

</script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-3MTV8XXHPL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3MTV8XXHPL');
</script>

<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>

<script src="https://code.jquery.com/jquery-migrate-3.4.0.min.js" integrity="sha256-mBCu5+bVfYzOqpYyK4jm30ZxAZRomuErKEFJFIyrwvM=" crossorigin="anonymous"></script>

<!--    -->



<script data-ad-client="ca-pub-3352501607232481" async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" data-checked-head="true"></script>

<script>




$(function(){
	$('#menu .main-menu #menu02').addClass("selected");
	
		if (!isMobile) {
			$( "#zid-include" ).load( "/inc/ajax-funkcije.asp?akcija=zid-include&Menu=0202&sponzor=1", function() {
			console.log( "Load was performed." );
			});
		}
	
	$('.mobileslider').css('visibility', 'visible');
	
	enquire.register("screen and (max-width: 768px)", {
    match : function() {
		
		

		 
    },
	
	 unmatch : function() {

	  

 		}
	});
	
	
})

  $(window).on('load resize', function() {


	$(".spinner-container").delay(100).fadeOut(600).remove();
	
	
	
})

jQuery.uaMatch = function( ua ) {
        ua = ua.toLowerCase();

        var match = /(chrome)[ /]([w.]+)/.exec( ua ) ||
                /(webkit)[ /]([w.]+)/.exec( ua ) ||
                /(opera)(?:.*version|)[ /]([w.]+)/.exec( ua ) ||
                /(msie) ([w.]+)/.exec( ua ) ||
                ua.indexOf("compatible") < 0 && /(mozilla)(?:.*? rv:([w.]+)|)/.exec( ua ) ||
                [];

        return {
                browser: match[ 1 ] || "",
                version: match[ 2 ] || "0"
        };
};

// Don't clobber any existing jQuery.browser in case it's different
if ( !jQuery.browser ) {
        matched = jQuery.uaMatch( navigator.userAgent );
        browser = {};

        if ( matched.browser ) {
                browser[ matched.browser ] = true;
                browser.version = matched.version;
        }

        // Chrome is Webkit, but Webkit is also Safari.
        if ( browser.chrome ) {
                browser.webkit = true;
        } else if ( browser.webkit ) {
                browser.safari = true;
        }

        jQuery.browser = browser;
}




</script>

<script src="/js/funkcije-skupaj.js?v=1.043222"></script>

<script src="/js/flickity.min.js?v=1.043222"></script>

<script src="/js/new-responsive.js?v=1.043222"></script>
 <script src="/js/jquery.cookiecuttr.js"></script>
<script>
$(document).ready(function () {
	// activate cookie cutter
    $.cookieCuttr({
		cookieAnalytics:false,
		cookieCutter: true,
		
    	cookieDeclineButton: false,
		cookieOverlayEnabled:true,
		
		cookieDisable: '.piskotki',
		cookieDomain: 'kulinarika.net',
		cookieNotificationLocationBottom: false,
		cookieWhatAreTheyLink:'/zasebnost/',
		cookiePolicyLink: '/zasebnost/'
    });
}); 	
</script>

<!-- InstanceBeginEditable name="napis" -->
<!--<link href="/css/ajax-dynamic-list.css" rel="stylesheet" type="text/css" /> -->

<meta name="robots" content="index,follow">


<title>Recept: Rogljički s skuto  - Kulinarika.net</title>

<link rel="canonical" href="https://www.kulinarika.net/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/">
<meta name="Description" content="prigrizek ali sladica">
<meta name="Keywords" content="piknik,rojstni dan otroka,valentinovo,pečenje,jesen,poletje,pomlad,zima,sladice,prigrizki">


<meta property="og:title" content="Recept: Rogljički s skuto  - Kulinarika.net">
<meta property="og:description" content="prigrizek ali sladica">
<meta property="og:type" content="article">
<meta property="og:url" content="https://www.kulinarika.net/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/">
<meta property="og:image" content="https://www.kulinarika.net/slikerecepti/21526/1.webp?0.7055475"><meta property="og:image:type" content="image/webp">


<script src="/js/mnenja.js"></script><meta http-equiv="origin-trial" content="AlK2UR5SkAlj8jjdEc9p3F3xuFYlF6LYjAML3EOqw1g26eCwWPjdmecULvBH5MVPoqKYrOfPhYVL71xAXI1IBQoAAAB8eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="Amm8/NmvvQfhwCib6I7ZsmUxiSCfOxWxHayJwyU1r3gRIItzr7bNQid6O8ZYaE1GSQTa69WwhPC9flq/oYkRBwsAAACCeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiV2ViVmlld1hSZXF1ZXN0ZWRXaXRoRGVwcmVjYXRpb24iLCJleHBpcnkiOjE3NTgwNjcxOTksImlzU3ViZG9tYWluIjp0cnVlfQ=="><meta http-equiv="origin-trial" content="A9wSqI5i0iwGdf6L1CERNdmsTPgVu44ewj8QxTBYgsv1LCPUVF7YmWOvTappqB1139jAymxUW/RO8zmMqo4zlAAAAACNeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A+d7vJfYtay4OUbdtRPZA3y7bKQLsxaMEPmxgfhBGqKXNrdkCQeJlUwqa6EBbSfjwFtJWTrWIioXeMW+y8bWAgQAAACTeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiRmxlZGdlQmlkZGluZ0FuZEF1Y3Rpb25TZXJ2ZXIiLCJleHBpcnkiOjE3MzY4MTI4MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9">
<script src="/js/knjiga.js"></script>
<link href="/p7epm/epm5/p7EPM05.css" rel="stylesheet" type="text/css" media="all">
<script src="/p7epm/p7EPMscripts.js"></script>
<style type="text/css">
.p7epm_cwrapper {height:0px;overflow:hidden;}

</style>
<script>

	if (isMobile) 
	{
		var head = document.getElementsByTagName('head')[0];
		var script = document.createElement('script');
		script.type = 'text/javascript';
		script.src = '/js/nosleep.min.js';
		head.appendChild(script);
		
	}


</script>
  <link href="/css/venobox/venobox.css?v=4.0502524229335" type="text/css" rel="stylesheet">
  <script src="/js/jquery.venobox.js?v=1.043222"></script>
 <link href="/css/slider-pro.min.css?v=4.0502524229335" type="text/css" rel="stylesheet">
 <script src="/js/jquery.sliderpro.min.js?v=1.043222"></script> 
  <script type="application/ld+json">
   [{
     "@context": "http://schema.org",
     "@type": "BreadcrumbList",
     "itemListElement":
     [
      {
       "@type": "ListItem",
       "position": 1,
	   "item": 
	   {
		  "name": "portal",
		  "@id": "https://www.kulinarika.net"
		}
      },
      {
       "@type": "ListItem",
      "position": 2,
      "item": {
			"name": "recepti",
			"@id": "/recepti/"
      }
	  }
	  ,
	  {
       "@type": "ListItem",
      "position": 3,

      "item": 
	  {
		  "name": "sladice",
		  "@id": "/recepti/seznam/sladice/"
      }
	  }
	  
	  ,
	  {
       "@type": "ListItem",
      "position": 4,
      "item": 
	  {
		 "name": "pecivo",
		 "@id": "/recepti/seznam/sladice/pecivo/"
	  }
      }
	  
	  ,
	  {
       "@type": "ListItem",
      "position": 5,
      "item": 
	  {
		 "name": "Rogljički s skuto ",
		 "@id": "/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/"
	  }
      }
     ]
    }
	,
	

	{
	  "@context": "https://schema.org/",
	  "@type": "Recipe",
	  "name": "Rogljički s skuto ",
	  "description": "prigrizek ali sladica",
	  
	  "image": ["https://www.kulinarika.net/slikerecepti/21526/1-200x150.webp","https://www.kulinarika.net/slikerecepti/21526/1-400x300.webp","https://www.kulinarika.net/slikerecepti/21526/1.webp"],
	  
	  "author": {
		"@type": "Person",
		"name": "Fala Slonček"
	  },
	  
	  "aggregateRating": {"@type": "AggregateRating","ratingValue": "5","ratingCount": "2","reviewCount": "3"},
	  
	  
	  
	  "recipeCuisine": "",
	  "totalTime": "PT60M","keywords": "piknik,rojstni dan otroka,valentinovo,pečenje,jesen,poletje,pomlad,zima,sladice,prigrizki",
	  
	  "recipeCategory": "sladice: pecivo",
	  "recipeIngredient": [
		"1 kocka kvasa Fala","1,1 kg moke","2 dl mleka","2,5 dl jogurta","18 dag kisle smetane","8 dag masla","6 dag sladkorja","3 jajca","3 male žličke soli","25 dag skute","1 beljak","4 dag sladkorja"
	  ],
	  "recipeInstructions": [
		{"@type": "HowToStep","text":"1. Kvas Fala raztopimo v polovici toplega mleka. V posodo odmerimo vse ostale sestavine brez olja, dodamo raztopljeni kvas in zamesimo kvašeno testo. Na začetku mešamo počasi, nato deset minut na najvišji hitrosti. Med mešanjem postopno dodajamo zmehčano maslo. Ko je testo gladko, ga pokrijemo in pustimo vzhajati."},{"@type": "HowToStep","text":"2. Med vzhajanjem pripravimo nadev. Beljak stepemo v trd sneg ob postopnem dodajanju sladkorja. Sneg enakomerno vmešamo v skuto."},{"@type": "HowToStep","text":"3. Vzhajano testo stresemo na pult, ga pregnetemo, razdelimo na šest delov in pustimo nekaj minut počivati. Nato vsak kos testa razvaljamo na krog, tega razrežemo na osem enakih delov (trikotnikov). Na zunanjo stran vsakega trikotnika položimo žličko nadeva in zato trikotnik zvijemo v rogljiček v smeri od zunanje strani z nadevom proti notranjosti – konici trikotnika. Oblikovani zvitek dokončno oblikujemo v rogljiček in ga položimo na pekač. Nadaljujemo z zvijanjem ostalih trikotnikov v rogljičke in nato še z oblikovanjem vseh ostalih kosov testa."},{"@type": "HowToStep","text":"4. Rogljičke pustimo vzhajati na toplem. Nato jih premažemo s stepenim jajcem in prestavimo v vročo pečico. Rogljičke pečemo 20 minut na 175 stopinjah, da se lepo obarvajo."}
		
		
	  ]
	}
]

	
	
	
	
	</script>

    


<script>
//<![CDATA[
hs.preserveContent = false;

$(window).on('load resize', function(){
	
	if ($(window).width() <= 500) {
	//$('#oglasi-stranski').insertAfter($('#receptSestavine'));
  } else {
    //$('#oglasi-stranski').insertAfter($('.info-kuha'));
  }
	
})

$(document).on({
		click: function(){
			var IDMnenje = $(this).data('id');
			$(this).prev('.like-stevilo').load("/inc/ajax-funkcije.asp?akcija=like_add_delete&s=1&IDMnenje=" + IDMnenje + "&rand=" + Math.round(new Date().getTime()/1000), function() {
				//reFacebook();
				$(this).parent().children('.likes-holder').toggleClass('on');
				});
		}
	},
 	'div.likes a.likes-holder');

$(document).on({
		click: function(){
		event.preventDefault();
			$.ajax({
				type: "get",
				url: "/inc/ajax-funkcije.asp?akcija=recepti_priljubljeni",
				data: {
					id: 21526,
					rand: Math.round(new Date().getTime()/1000)
				},
				success: function(response) {
					if (response==0) {
						$('#priljubljeni-recept img').attr('src', '/grafika7/icon-heart-off.svg');
						$('#zabelezka').removeClass('show').addClass('hide');
					}
					else
					{
						$('#priljubljeni-recept img').attr('src', '/grafika7/icon-heart-on.svg');
						$('#zabelezka').removeClass('hide').addClass('show');
					}
				}
			})
		}
	},
 	'#priljubljeni-recept');



$(document).ready(function() {

	enquire.register("screen and (max-width: 768px)", { // Mobile
		match : function() {

			$('#info-praznik').insertAfter('#receptPostopek').addClass('mobile');
			//$('#oglasi-stranski').insertAfter('footer').addClass('mobile');
			$('#oglas-aside2').insertBefore('#receptPostopek').addClass('enrecept');
			$('label#zaslon').removeClass('hide_important');
			
		},
		unmatch : function() { // Desktop

			$('#info-praznik').insertBefore('.info-kuha').removeClass('mobile');
			$('#oglas-aside2').appendTo('#oglasi-stranski').removeClass('enrecept');
			$('label#zaslon').addClass('hide_important');
	
		}
	});


		
	

	/* Preoader */

	function loadingStart(dividor) {
		$("#" + dividor).show();	
	}

	function loadingStop(dividor) {
		$("#" + dividor).hide();	
	}

	if (isMobile) {
	
		var noSleep = new NoSleep();
		
		
		
		$('#zaslon .toggle-checkbox').on('click', function() {
		
			
			varState=$('.toggle-checkbox').is(':checked');
			
			// Klik se izvrši 2x (label for in input, zato preveri ravno obratno stanje, kot je :-)
			if (!varState) {
				// daj na off
				noSleep.disable();
				$('.toggle-checkbox').prop('checked', false);

				$("#sestavine p:not('.empty,.poglavje') .input-narejeno").remove();
				$("#sestavine p:not('.empty,.poglavje')").removeClass("narejeno");
				$("#sestavine span.label").removeClass("narejeno");
				$("#sestavine span.label-value").removeClass("narejeno");	

				$("#postopek").removeClass("naredi");
				$("#postopek p:not('.edini_korak_postopek') .input-narejeno").remove();
				$("#postopek p:not('.edini_korak_postopek') .data").removeClass("narejeno");
				$("#postopek p:not('.edini_korak_postopek')").removeClass("narejeno");
				
				$("ul.priljubljeni").removeClass("hide");
				$("#oglasi-stranski").removeClass("hide");
				bannerModule.toggleParallax();
			
			} else {
				noSleep.enable();
				$('.toggle-checkbox').prop('checked', true);
				$("#sestavine p:not('.empty,.poglavje') .label-value").prepend(function(index, htmlContent) {return "<span class='input-narejeno'><input type='checkbox' class='style1 semzenaredil' name='semzenaredil' id='sestavina"+ index +"' /><label for='sestavina"+ index +"'>&nbsp;</label></span>"});
				$("#sestavine span.label").addClass("narejeno");
				$("#sestavine span.label-value").addClass("narejeno");
				
				$("#postopek").addClass("naredi");
				$("#postopek p:not('.edini_korak_postopek') .data").prepend(function(index, htmlContent) {return "<span class='input-narejeno'><input type='checkbox' class='style1 semzenaredil' name='semzenaredil' id='postopek"+ index +"' /><label for='postopek"+ index +"'>&nbsp;</label></span>"});		
				$("#postopek p:not('.edini_korak_postopek') .data").addClass("narejeno");
				$("ul.priljubljeni").addClass("hide");
				$("#oglasi-stranski").addClass("hide");
				bannerModule.toggleParallax();
			};

		
		});
	
		$('#zaslon').removeClass('hide_important');
		
	};
	
	$(document).on('click', '.semzenaredil', function() {
		
		varState=$(this).is(':checked');
		
		if (varState) {
		
			$(this).parent().parent().parent().addClass('narejeno');
			
		} else {
			$(this).parent().parent().parent().removeClass('narejeno');
			$(this).blur();
		}
	})
		

	$('.venobox').venobox(); 

	$(document).on('click', 'img.figlio', function(e){
        $('.vbox-close').click();
    });
	
	$('.odpirac-dodaj-zabelezko').venobox({
		post_close_callback: function(event){
			window.location.reload()
		}
   		 });
		

	
	$('#popup-oceneseznam-holder').venobox();
	$('#popup-zanimivosti-holder').venobox();
	$('#popup-prispevaj-holder').venobox();
		
	
	
	

	$('#popup-ocene-holder').bind('click', function () {
		return hs.htmlExpand(this, { width:385, height: 173, contentId: 'popup-ocene', objectType: 'iframe', preserveContent: false} )
	})



	$('#TekneIDSubmit').bind('click', function() {
		loadingStart("loadingRecipeID");
		$('#recipename').load('/inc/ajax-checkrecipename.asp?akcija=priporocilo&IDRecept=21526&ID=' + $('#TekneID').val(), function() {
			loadingStop("loadingRecipeID");
			});
	})
	
	$('#TekneNameSubmit').bind('click', function() {
		loadingStart("loadingRecipeName");
		$('#recipename2').load('/inc/ajax-checkrecipename.asp?akcija=priporocilo&IDRecept=21526&ImeRecepta=' + encodeURI($('#TekneName').val()), function() {
			loadingStop("loadingRecipeName");	
		});
	})
	
	var optionsSubmit = {
		target:	'#telo',
		beforeSubmit:  showRequest,
		success: function(responseText, statusText, xhr, $form) {
			napisgumb = $form.find('[name=napisgumb]').val();
			if (napisgumb==1){
					$form.find('input[type=submit]').css('display', 'none')
					$form.find('[name=napisgumb]').val('2');
				}
			loadingStop('loadingOddajPriporocilo');
			}	
		
	}
	
	$(document).on("submit", ".PriporociRecept", function() {
			$(this).ajaxSubmit(optionsSubmit)
			return false;
	})
	
	var optionsSubmit2 = {
		target:	'#telo',
		beforeSubmit:  showRequest,
		success: function(responseText, statusText, xhr, $form) {
			IDPriporocilo = $form.find('[name=IDpriporocilo]').val();
			$('#submit' + IDPriporocilo).css('display', 'inline');
			$('#PriporociRecept' + IDPriporocilo).find('[name=napisgumb]').val('1');
			loadingStop('#loadingOddajPriporocilo');
			}	
		
	}
	
	$(document).on("submit", ".PriporociRecept2", function() {	
			$(this).ajaxSubmit(optionsSubmit2)
			return false;
	})
	
	


	
	function showRequest() {
		loadingStart('loadingOddajPriporocilo')
		}
		
	
	$('#posljiprijatelju').on("click", function() {
	
		$.ajax({
			url: '/inc/ajax-funkcije.asp?id=21526&akcija=posljiprijatelju',
			success: function(text)
				{

				}
		})	
	
	})
	
	$('#receptiFotkePostopki').show();
	
		$('.vinoslider').flickity({
	// options
		cellAlign: 'left',
		contain: true,
		prevNextButtons: true,
		freeScroll: true,
		setGallerySize: false
	});

		
	
})




	


	
$(document).ready(function() {

	if (navigator.share) {
		$('#webShare').css("display", "inline-block");
		$("#ingredientsShare").css("display", "inline-block");
		
		$("#webShare").on("click", function(){
				navigator.share({
					title: 'Recept: Rogljički s skuto  - Kulinarika.net',
					text: 'Našel sem tale izvrsten recept',
					url: 'https://www.kulinarika.net/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/'

				});	
		});
		
		$("#ingredientsShare").on("click", function(){
				navigator.share({
					title: 'Recept: Rogljički s skuto  - Kulinarika.net',
					text: 'Testo:\n1 kocka \n1,1 kg moke\n2 dl mleka\n2,5 dl jogurta\n18 dag kisle smetane\n8 dag masla\n6 dag sladkorja\n3 jajca\n3 male žličke soli\n\nNadev:\n25 dag skute\n1 beljak\n4 dag sladkorja\n',
					url: 'https://www.kulinarika.net/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/'

				});

				$.ajax({
					url: '/inc/ajax-funkcije.asp?id=21526&akcija=deljenjesestavin&storitev=1'
				});
				
		});		
		
	}

	
	
	$(".vinoslider").css('visibility', 'visible');


	enquire.register("screen and (max-width: 768px)", {
		match : function() {
		   
		   $('.mobileslider').flickity({
				// options
				cellAlign: 'left',
				contain: true,
				prevNextButtons: false,
				setGallerySize: false
			});
			
			$('#receptSestavine a.prazniki_teaser').insertBefore('h1');
			
		},
		
		 unmatch : function() {
 
		   
		   $('.mobileslider').flickity('destroy');
		   $('#recept-main a.prazniki_teaser').insertAfter('#sestavine');
		   
		   		 
		}
	});
		
		
		$('#telo').load("/inc/ajax-priporocamo.asp?ID=21526");
		
		


	 
});

function mycarousel_itemAddCallback(xml)
{
	
	$( '#sliderRecepti' ).sliderPro({
			width: 640,
			height: 480,
			thumbnailWidth: 140,
			thumbnailHeight: 105,
			imageScaleMode: 'cover',
			arrows: true,
			buttons: false,
			loop:false,
			fullScreen: true,
			shuffle: false,
			smallSize: 500,
			mediumSize: 1000,
			largeSize: 3000,
			thumbnailArrows: true,
			autoplay: false,
			aspectRatio: 4/3,
			allowScaleUp: false,
			reachVideoAction: 'playVideo',
				breakpoints: {
					768: {
						thumbnailWidth: 120,
						thumbnailHeight: 90
					}
				},
			init: function() {

				var slides = $(this).get(0).slides.length;
				$( '#sliderRecepti' ).append('<div class="counter"><span class="active">1</span>/' + slides + '</div>');
				
				$( '#sliderRecepti img.sp-thumbnail.sp-video' ).removeClass('sp-video').parent().addClass('sp-video');
				
				$('.slider-pro .sp-image-container').css('background', '#000');
			
			}
		});
	
   	$( '.sp-slide' ).click(function(){
		 var slider = $( this ).parents( '.slider-pro' );
		 if( ! slider.hasClass('sp-swiping') && ! $(this).find('a').hasClass('sp-video') ) {
			  slider.find( '.sp-full-screen-button' ).trigger( 'click' );
		 }
	});

	$( '#sliderRecepti' ).on( 'sliderResize', function() {

			var slider = $(this),
			scaleMode = slider.data('sliderPro').settings.imageScaleMode;
			scaleUp=slider.data('sliderPro').settings.allowScaleUp;
			
			if ( slider.hasClass( 'sp-full-screen' ) && scaleMode !== 'contain' ) {
				slider.sliderPro( 'imageScaleMode', 'contain' );
				
			} else if ( ! slider.hasClass( 'sp-full-screen' ) && scaleMode !== 'cover' ) {
				slider.sliderPro( 'imageScaleMode', 'cover' );
			}
	});
	

	
	$( '#sliderRecepti' ).on( 'gotoSlide', function(event) {
		$(this).find('.counter .active').text(event.index + 1);
		
	});
	$( '#sliderRecepti' ).on( 'videoPlay', function(event) {
		$('.sp-caption-container .video').addClass('hide');
		
	});
	$( '#sliderRecepti' ).on( 'videoEnd', function(event) {
		$('.sp-caption-container .video').removeClass('hide');
		
	});	


	

}

</script>
<!-- InstanceEndEditable -->
<!-- InstanceBeginEditable name="head" -->
<!-- <script src="/ad/intext/intext2.js"></script> -->

    <!-- Add the ad-system.js script -->
	<script src="/ad-admin/js/ad-system.js" type="text/javascript" charset="utf-8"></script>

<!-- InstanceEndEditable -->



<!-- InstanceParam name="onload" type="text" value="" -->
<style type="text/css">.highslide img {cursor: url(/images/zoomin.cur), pointer !important;}.highslide-viewport-size {position: fixed; width: 100%; height: 100%; left: 0; top: 0}</style></head>

<body onload="">
<div id="fb-root"></div>
<div id="ozadjeReklamaContainer"><div id="ozadjeReklama" class=""><iframe id="banner16" name="banner16" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="1600" height="1200" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=16&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,5051342"></iframe><script>$(document).ready(function() {$('#banner16').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=16&kanal=recepti&kat=sladice&podkat=pecivo&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,5051342');});</script></div></div><ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><div id="aswift_0_host" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://pagead2.googlesyndication.com/pagead/ads?client=ca-pub-3352501607232481&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;abgtt=8&amp;lmt=1743871153&amp;plat=1%3A16777216%2C2%3A16777216%2C3%3A16%2C4%3A16%2C9%3A134250504%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32%2C41%3A32%2C42%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.kulinarika.net%2Frecepti%2Fsladice%2Fpecivo%2Frogljicki-s-skuto-%2F21526%2F&amp;pra=5&amp;wgl=1&amp;aihb=0&amp;asro=0&amp;ailel=1~2~4~7~8~9~10~11~12~13~14~15~16~17~18~19~20~21~24~29~30~34&amp;aiael=1~2~3~4~7~8~9~10~11~12~13~14~15~16~17~18~19~20~21~24~29~30~34&amp;aicel=33~38&amp;aifxl=29_18~30_19&amp;aiixl=29_5~30_6&amp;itsi=-1&amp;aiapm=0.15&amp;aiapmi=0.33938&amp;aiact=0.7&amp;ailct=0.7&amp;uach=WyJtYWNPUyIsIjEzLjQuMCIsImFybSIsIiIsIjEzMy4wLjY5NDMuMTI3IixudWxsLDAsbnVsbCwiNjQiLFtbIk5vdChBOkJyYW5kIiwiOTkuMC4wLjAiXSxbIkdvb2dsZSBDaHJvbWUiLCIxMzMuMC42OTQzLjEyNyJdLFsiQ2hyb21pdW0iLCIxMzMuMC42OTQzLjEyNyJdXSwwXQ..&amp;dt=1743871153262&amp;bpp=25&amp;bdt=28&amp;idt=25&amp;shv=r20250403&amp;mjsv=m202504010101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;eoidce=1&amp;nras=1&amp;correlator=5457592559747&amp;frm=20&amp;pv=2&amp;u_tz=120&amp;u_his=4&amp;u_h=956&amp;u_w=1470&amp;u_ah=850&amp;u_aw=1470&amp;u_cd=30&amp;u_sd=2&amp;dmc=8&amp;adx=-12245933&amp;ady=-12245933&amp;biw=1467&amp;bih=763&amp;scr_x=0&amp;scr_y=0&amp;eid=95355973%2C95355975%2C95356626%2C31091503%2C95357455&amp;oid=2&amp;pvsid=3112694513535905&amp;tmod=144915669&amp;uas=0&amp;nvt=1&amp;fsapi=1&amp;ref=https%3A%2F%2Fwww.kulinarika.net%2Frecepti%2Fseznam%2Fsladice%2F&amp;fc=1920&amp;brdim=0%2C37%2C0%2C37%2C1470%2C37%2C1467%2C850%2C1467%2C763&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;bz=1&amp;td=1&amp;tdf=2&amp;nt=1&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;dtd=29" data-google-container-id="a!1" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true"></iframe></div></ins><div id="MegaContainer" data-sponzor="69740"><div id="Container" class="cf">




<div id="kul-glava">
    <header class="header">
        <div class="container">
            <nav class="nav-container">
                <div class="close-menu">×</div>
                <div class="nav-items">
                    <div class="dropdown-container">
                        <a class="dropbtn izbrano" href="#">Recepti</a>
                        <div class="dropdown-content" style="display: none;">
                            <div class="dropdown-content-inner">
								<div class="special-wrapper">
									<a class="special portal" href="/recepti/"><img loading="lazy" alt="vsi recepti" src="/grafika6/recepti-portal.webp"><span>Vsi recepti</span></a>
									<a class="special oddaj" href="/mojakulinarika/recepti/oddaj/"><img loading="lazy" alt="prispevaj svoj recept" src="/grafika6/recepti-poslji.webp"><span>Prispevajte svoj recept</span></a>
									<a class="special zdravo" href="/recepti/seznam/?zdravo=1"><img loading="lazy" alt="zdravi recepti" src="/grafika6/recepti-zdravo.webp"><span><span>Zdrave jedi</span></span></a>
								</div>
								<a class="menu" href="/recepti/seznam/sladice/"><img loading="lazy" alt="recepti za sladice" src="/grafika6/recepti18.webp"><span>Sladice</span></a>
								<a class="menu" href="/recepti/seznam/zelenjavne-jedi/"><img loading="lazy" alt="recepti za zelenjavne jedi" src="/grafika6/recepti21.webp"><span>Zelenjavne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/testenine/"><img loading="lazy" alt="recepti za testenine" src="/grafika6/recepti20.webp"><span>Testenine<span></span></span></a>
								<a class="menu" href="/recepti/seznam/solate/"><img loading="lazy" alt="recepti za solate" src="/grafika6/recepti19.webp"><span>Solate<span></span></span></a>
								<a class="menu" href="/recepti/seznam/juhe-in-zakuhe/"><img loading="lazy" alt="recepti za juhe in zakuhe" src="/grafika6/recepti05.webp"><span>Juhe in zakuhe<span></span></span></a>
								<a class="menu" href="/recepti/seznam/mesne-jedi/"><img loading="lazy" alt="recepti za mesne jedi" src="/grafika6/recepti07.webp"><span>Mesne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/kruh/"><img loading="lazy" alt="recepti za kruh" src="/grafika6/recepti06.webp"><span>Kruh<span></span></span></a>
								<a class="menu" href="/recepti/seznam/prikuhe/"><img loading="lazy" alt="recepti za prikuhe" src="/grafika6/recepti15.webp"><span>Prikuhe<span></span></span></a>
								<a class="menu" href="/recepti/seznam/priloge/"><img loading="lazy" alt="recepti za priloge" src="/grafika6/recepti16.webp"><span>Priloge<span></span></span></a> 
								<a class="menu" href="/recepti/seznam/jajcne-jedi/"><img loading="lazy" alt="recepti za jajčne jedi" src="/grafika6/recepti04.webp"><span>Jajčne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/eksotika/"><img loading="lazy" alt="eksotični recepti" src="/grafika6/recepti01.webp"><span>Eksotika<span></span></span></a>
								<a class="menu" href="/recepti/seznam/enloncnice/"><img loading="lazy" alt="recepti za enolončnice" src="/grafika6/recepti02.webp"><span>Enolončnice<span></span></span></a>
								<a class="menu" href="/recepti/seznam/gobje-jedi/"><img loading="lazy" alt="recepti za gobje jedi" src="/grafika6/recepti03.webp"><span>Gobje jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/morska-hrana/"><img loading="lazy" alt="recepti za morsko hrano" src="/grafika6/recepti08.webp"><span>Morska hrana<span></span></span></a>
								<a class="menu" href="/recepti/seznam/napitki/"><img loading="lazy" alt="recepti za napitke" src="/grafika6/recepti09.webp"><span>Napitki<span></span></span></a>
								<a class="menu" href="/recepti/seznam/omake/"><img loading="lazy" alt="recepti za omake" src="/grafika6/recepti10.webp"><span>Omake<span></span></span></a>
								<a class="menu" href="/recepti/seznam/otroska-hrana/"><img loading="lazy" alt="recepti za otroško hrano" src="/grafika6/recepti12.webp"><span>Otroška hrana<span></span></span></a>
								<a class="menu" href="/recepti/seznam/ozimnica/"><img loading="lazy" alt="recepti za ozimnico" src="/grafika6/recepti13.webp"><span>Ozimnica<span></span></span></a>
								<a class="menu" href="/recepti/seznam/predjedi/"><img loading="lazy" alt="recepti za predjedi" src="/grafika6/recepti14.webp"><span>Predjedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/sirove-jedi/"><img loading="lazy" alt="recepti za sirove jedi" src="/grafika6/recepti17.webp"><span>Jajčne jedi<span></span></span></a>
								<a class="menu" href="/recepti/seznam/zar/"><img loading="lazy" alt="recepti za žar" src="/grafika6/recepti04.webp"><span>Žar<span></span></span></a>
								<a class="menu" href="/recepti/seznam/ostale-jedi/"><img loading="lazy" alt="recepti za ostale jedi" src="/grafika6/recepti11.webp"><span>Ostale jedi<span></span></span></a>
								
		
                            </div>
                        </div>
                    </div>
					<a href="/vino/">Vino</a>
                        <a href="/forumi/" class="dropbtn">Forumi</a>

					
					
                    <a href="/fotoalbumi/">Albumi</a>
                    <a href="/zid/">Zid</a>
                    <a href="/blogi/">Blogi</a>
                    <a href="/zdravje/">Zdravo</a>
                    <a href="/zanimivo/">Zanimivo</a>
                    <a href="/iskanje/?datumi=tridni#novosti">Novosti</a>
				    

					
					
					
                </div>
            </nav>
            <div class="icon-line">
                <div class="hamburger">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </div>
                <div class="logo"><a href="/"><img src="https://www.kulinarika.net/grafika6/logotipi/kul.svg" alt="Kulinarika.net logo"></a></div>
				<form class="search-container" name="FormIskanje" id="FormIskanje" action="/iskanje/" method="GET" autocomplete="off">
					<input type="text" class="search-field" name="splosno_besede" placeholder="Išči recepte...">
					<button type="submit" class="search-submit">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
							<circle cx="11" cy="11" r="8"></circle>
							<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
						</svg>
						Išči
					</button>
					<div class="search-dropdown" style="display: none;">
						<a href="/recepti/seznam/?iskanje=1" class="search-link">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<circle cx="11" cy="11" r="8"></circle>
								<line x1="21" y1="21" x2="16.65" y2="16.65"></line>
							</svg>
							Napredno iskanje po receptih
						</a>
						<a href="/forumi/forum/?vec=1" class="search-link">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
								<line x1="8" y1="6" x2="21" y2="6"></line>
								<line x1="8" y1="12" x2="21" y2="12"></line>
								<line x1="8" y1="18" x2="21" y2="18"></line>
								<line x1="3" y1="6" x2="3.01" y2="6"></line>
								<line x1="3" y1="12" x2="3.01" y2="12"></line>
								<line x1="3" y1="18" x2="3.01" y2="18"></line>
							</svg>
							Iskanje po forumih
						</a>
					</div>
				</form>
                <div class="mobile-right-icons">
                    <div class="search-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </div>
				
					
				
                    <div class="user-info">
                        <div class="avatar" alt="avatar slika">
                        <span class="ime">prijava</span>
						</div>
                        <div class="user-dropdown" style="display: none;">
							<div class="close-menu">×</div>
							


							 <form action="/mojakulinarika/prijava/" method="post" name="prijava" id="form-prijava" class="form-dizajn1 cf">
							 <h3>Prijava v Kulinarika.net</h3>
								 <div id="mojakulslo-login-wrapper" class="cf">
								 <input type="hidden" name="portal" value="1">
									<label for="loginuser">Uporabnik:</label><input id="loginuser" name="uporabnik" type="text"><br>
									<label for="loginpassword">Geslo:</label><input id="loginpassword" name="geslo" type="password"><br>
								 </div>
							
							
						
					   
							 <input name="Submit" type="submit" class="submit" value="Prijava">
						
								<a href="/mojakulinarika/pozabljeno/" class="noborder">Pozabljeno geslo</a>
						  <a class="noborder" href="/mojakulinarika/vpis/">Nov uporabnik</a>
						
							 </form>

						  
				  

							
							
							
							
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

</div>




<script>
(function() {
    document.addEventListener('DOMContentLoaded', function() {
        const kulGlava = document.getElementById('kul-glava');
        const header = kulGlava.querySelector('.header');
        const navContainer = kulGlava.querySelector('.nav-container');
        const hamburger = kulGlava.querySelector('.hamburger');
        const closeMenuButtons = kulGlava.querySelectorAll('.close-menu');
        const userInfo = kulGlava.querySelector('.user-info');
        const userDropdown = kulGlava.querySelector('.user-dropdown');
        const searchIcon = kulGlava.querySelector('.search-icon');
        const searchContainer = kulGlava.querySelector('.search-container');
        const dropdowns = kulGlava.querySelectorAll('.dropdown-container');
        const searchField = kulGlava.querySelector('.search-field');
        const searchDropdown = kulGlava.querySelector('.search-dropdown');

        let scrollPosition = 0;
        const body = document.body;

        function lockScroll() {
            if (!body.classList.contains('scroll-locked')) {
                scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
                body.classList.add('scroll-locked');
                body.style.overflow = 'hidden';
                body.style.position = 'fixed';
                body.style.top = `-${scrollPosition}px`;
                body.style.width = '100%';
            }
        }

        function unlockScroll() {
            if (body.classList.contains('scroll-locked')) {
                body.classList.remove('scroll-locked');
                body.style.removeProperty('overflow');
                body.style.removeProperty('position');
                body.style.removeProperty('top');
                body.style.removeProperty('width');
                window.scrollTo(0, scrollPosition);
            }
        }

        function closeAllMenus() {
            userDropdown.classList.remove('show');
            userDropdown.style.display = 'none';

            dropdowns.forEach(dropdown => {
                const dropdownContent = dropdown.querySelector('.dropdown-content');
                const dropbtn = dropdown.querySelector('.dropbtn');
                dropdownContent.style.display = 'none';
                dropbtn.classList.remove('active');
            });

            navContainer.classList.remove('show');
            searchContainer.classList.remove('show');

            searchDropdown.classList.remove('show');
            searchDropdown.style.display = 'none';

            unlockScroll();
        }

        function openMenu(menu) {
            menu.classList.add('show');
            document.body.classList.add('menu-open');
            lockScroll();
        }

        function closeMenu(menu) {
            menu.classList.remove('show');
            document.body.classList.remove('menu-open');
            unlockScroll();
        }

        function toggleUserDropdown(e) {
            e.stopPropagation();
            if (window.innerWidth <= 768) {
                userDropdown.style.removeProperty('display');
                userDropdown.classList.toggle('show');
                if (userDropdown.classList.contains('show')) {
                    lockScroll();
                } else {
                    unlockScroll();
                }
            } else {
                userDropdown.classList.remove('show');
                userDropdown.style.display = userDropdown.style.display === 'block' ? 'none' : 'block';
            }
        }

        function handleResize() {
            if (window.innerWidth <= 768) {
                userDropdown.style.removeProperty('display');
                if (userDropdown.classList.contains('show')) {
                    userDropdown.style.display = 'flex';
                }
            } else {
                userDropdown.classList.remove('show');
                userDropdown.style.display = 'none';
                unlockScroll();
            }
        }

        function closeUserDropdown() {
            if (window.innerWidth <= 768) {
                userDropdown.classList.remove('show');
            } else {
                userDropdown.style.display = 'none';
            }
            unlockScroll();
        }

        hamburger.addEventListener('click', (e) => {
            e.stopPropagation();
            openMenu(navContainer);
        });

        userInfo.addEventListener('click', toggleUserDropdown);

        searchIcon.addEventListener('click', () => {
            searchContainer.classList.toggle('show');
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.dropdown') && !e.target.closest('.user-info') && !navContainer.contains(e.target) && !hamburger.contains(e.target)) {
                dropdowns.forEach(dropdown => {
                    dropdown.querySelector('.dropdown-content').style.display = 'none';
                    dropdown.querySelector('.dropbtn').classList.remove('active');
                });
                closeUserDropdown();
                unlockScroll();
            }
            if (!searchContainer.contains(e.target) && !searchIcon.contains(e.target)) {
                searchContainer.classList.remove('show');
            }
        });

        closeMenuButtons.forEach(button => {
            button.addEventListener('click', () => {
                closeMenu(navContainer);
                closeUserDropdown();
            });
        });

        const userDropdownCloseButton = userDropdown.querySelector('.close-menu');
        if (userDropdownCloseButton) {
            userDropdownCloseButton.addEventListener('click', (e) => {
                e.stopPropagation();
                closeUserDropdown();
            });
        }

        userDropdown.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        dropdowns.forEach(dropdown => {
            const dropbtn = dropdown.querySelector('.dropbtn');
            const dropdownContent = dropdown.querySelector('.dropdown-content');

            dropbtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();

                if (window.innerWidth <= 768) {
                    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
                    dropbtn.classList.toggle('active');
                    if (dropdownContent.style.display === 'block') {
                        lockScroll();
                    } else {
                        unlockScroll();
                    }
                } else {
                    closeUserDropdown();
                    dropdowns.forEach(otherDropdown => {
                        if (otherDropdown !== dropdown) {
                            otherDropdown.querySelector('.dropdown-content').style.display = 'none';
                            otherDropdown.querySelector('.dropbtn').classList.remove('active');
                        }
                    });
                    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
                    dropbtn.classList.toggle('active');
                }
            });

            dropdownContent.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        });

        searchField.addEventListener('focus', () => {
            searchDropdown.style.display = 'block';
            setTimeout(() => {
                searchDropdown.classList.add('show');
            }, 10);
            closeUserDropdown();
        });

        searchField.addEventListener('blur', (e) => {
            setTimeout(() => {
                if (!searchDropdown.contains(document.activeElement)) {
                    searchDropdown.classList.remove('show');
                    setTimeout(() => {
                        searchDropdown.style.display = 'none';
                    }, 300);
                }
            }, 100);
        });

        document.addEventListener('click', (e) => {
            if (!searchField.contains(e.target) && !searchDropdown.contains(e.target)) {
                searchDropdown.classList.remove('show');
                setTimeout(() => {
                    searchDropdown.style.display = 'none';
                }, 300);
            }
        });

        // New optimized scroll handling
        let lastKnownScrollPosition = 0;
        let ticking = false;
        const SCROLL_THRESHOLD = 5;

        function handleScroll(scrollPos) {
            if (Math.abs(scrollPos - lastKnownScrollPosition) > SCROLL_THRESHOLD) {
                if (scrollPos > lastKnownScrollPosition && scrollPos > 0) {
                    if (!header.classList.contains('header-hidden')) {
                        closeAllMenus();
                    }
                    header.classList.add('header-hidden');
                } else if (scrollPos < lastKnownScrollPosition) {
                    header.classList.remove('header-hidden');
                }
                lastKnownScrollPosition = scrollPos;
            }
        }

        window.addEventListener('scroll', (e) => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    handleScroll(window.scrollY);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        window.addEventListener('resize', debounce(handleResize, 150));
    });

    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            const later = () => {
                clearTimeout(timeout);
                func.apply(this, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
})();
    </script>


<div id="bodyContainer" class="cf">

    <div id="breadcrumbs">
          <div id="breadcrumbsPortal">
               
          </div>
        <!-- InstanceBeginEditable name="breadcrumbs" -->

<p class="breadcrumbs"><a href="/">domov</a> » <a href="/recepti/">recepti</a> » <a href="/recepti/seznam/sladice/">sladice</a> » <a href="/recepti/seznam/sladice/pecivo/">pecivo</a> » <span class="trenutno">Rogljički s skuto </span></p>
<!-- InstanceEndEditable -->
    
    </div>
<main id="vsebina" class="cf">
<!-- InstanceBeginEditable name="Main" -->

<section id="recepti" class="recept main-left">

<div id="recept-main">

<span style="display:none">piknik,rojstni dan otroka,valentinovo,pečenje,jesen,poletje,pomlad,zima,sladice,prigrizki</span><h1>Rogljički s skuto </h1><p class="podnaslov">prigrizek ali sladica</p><div class="podatki linki"><img class="spol" src="/grafika6/ikona-spol-brez.png" title="uporabnik"><a class="username" href="/uporabniki/seznam/ms4mp69e30x9541q/">Fala Slonček</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=Fala Slonček"><img title="Pošljite uporabniku Fala Slonček zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<span class="after1">ogledov: 47 856</span></div><span class="hide"></span> 
   






<div id="fotografije" class="cf">

	

			
			
			<div id="sliderRecepti" class="slider-pro sp-no-js no-thumbs">

				<div class="sp-slides">
					
					<a class="venobox vbox-item" href="/slikerecepti/21526/1.webp"><img title="Rogljički s skuto " alt="Rogljički s skuto " class="single rounded-all lazyautosizes ls-is-cached lazyloaded" data-sizes="auto" data-srcset="/slikerecepti/21526/1-200x150.webp 200w, /slikerecepti/21526/1-400x300.webp 400w, /slikerecepti/21526/1.webp " src="/grafika7/slika-se-nalaga.png" sizes="960px" srcset="/slikerecepti/21526/1-200x150.webp 200w, /slikerecepti/21526/1-400x300.webp 400w, /slikerecepti/21526/1.webp "></a>
				</div>
			</div> 	
				</div><ul class="servis cf linki"><span style="display:none">sladice: pecivo</span><li class="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"><img src="/grafika6/ikona-utez-prazna.png" alt="Zahtevnost" title="zahtevnost"></li><li><img class="ura" src="/grafika6/ikona-ura.png" alt="1 ura" title="1 ura">&nbsp;<span class="cas">1 ura</span><time datetime="PT60M"></time></li><li id="ocene"><a href="/inc/popup-ocene.asp?ID=21526" id="popup-oceneseznam-holder" data-type="ajax" data-width="340" data-height="500" data-fullscreen_mobile="true" title="Ocenite recept" class="vbox-item"><img src="/grafika6/ikona-ocena.png" title="2 oceni">&nbsp;<span title="povprečna ocena: 5">5</span></a></li><li class="zanimivosti"><a href="/inc/ajax-funkcije.asp?akcija=recepti-zanimivosti&amp;ID=21526" id="popup-zanimivosti-holder" data-type="ajax" data-width="300" data-height="290" data-fullscreen_mobile="true" class="vbox-item"><img title="Zanimivosti" alt="Zanimivosti" src="/grafika7/icon-info.svg" width="24" height="24"></a></li>

</ul>

<ul class="priljubljeni"><a class="neopazen vbox-item" href="/inc/popup-prispevaj.asp?id=21526" id="popup-prispevaj-holder" data-type="ajax" data-width="300" data-height="290" data-fullscreen_mobile="true" title="Prispevaj" alt="Prispevaj"><li><img title="prispevajte" src="/grafika7/icon-add-photo.svg" height="24">&nbsp;Prispevaj</li></a><a class="neopazen" href="/mojakulinarika/nisemclan/"><li><img src="/grafika7/icon-heart-off.svg" title="shranite med priljubljene" height="28">&nbsp;Shrani</li></a><a class="neopazen" href="/recepti/tiskanje/?id=21526" target="_blank"><li><img title="natisnite recept" src="/grafika7/icon-printer.svg" height="24">&nbsp;Natisni</li></a></ul>

<div id="uvod" class="linki">

	

</div>




<div id="receptSestavine"><h2>Sestavine

<span id="ingredientsShare" style="display: inline-block;">
<img title="shranite sestavine" src="/grafika7/icon-share.svg" height="36">
</span>

</h2>

      <div id="sestavine" class="articlesize linki ">
        
           <p class="cf poglavje" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>Testo:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">1 kocka </span><span class="label-value"><a href="https://www.facebook.com/fala.sloncek?fref=ts" target="_blank">kvasa Fala</a></span></p><p class="cf" itemprop="recipeIngredient"><span class="label">1,1 kg </span><span class="label-value">moke</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">2 dl </span><span class="label-value">mleka</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">2,5 dl </span><span class="label-value">jogurta</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">18 dag </span><span class="label-value">kisle smetane</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">8 dag </span><span class="label-value">masla</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">6 dag </span><span class="label-value">sladkorja</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">3 </span><span class="label-value">jajca</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">3 male žličke </span><span class="label-value">soli</span></p><p class="cf poglavje" itemprop="recipeIngredient"><span class="label"></span><span class="label-value"><b>Nadev:</b></span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">25 dag </span><span class="label-value">skute</span></p><p class="cf" itemprop="recipeIngredient"><span class="label">1 </span><span class="label-value">beljak</span></p> <p class="cf" itemprop="recipeIngredient"><span class="label">4 dag </span><span class="label-value">sladkorja</span></p>
</div>




</div>


<label class="toggle hide_important" id="zaslon">
	<input class="toggle-checkbox" type="checkbox">
	<div class="toggle-switch"></div>
	<p class="toggle-label">Način za kuhanje</p>
</label>

<div id="oglas300LuknjaRecept"></div>

  <div id="receptPostopek"><h2>Postopek</h2>

    <div id="postopek" class="articlesize linki ">

  <div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf en_korak_postopek" itemprop="text"><span class="label">1. </span><span class="data"><a href="https://www.facebook.com/fala.sloncek?fref=ts" target="_blank">Kvas Fala</a> raztopimo v polovici toplega mleka. V posodo odmerimo vse ostale sestavine brez olja, dodamo raztopljeni kvas in zamesimo kvašeno testo. Na začetku mešamo počasi, nato deset minut na najvišji hitrosti. Med mešanjem postopno dodajamo zmehčano maslo. Ko je testo gladko, ga pokrijemo in pustimo vzhajati.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf en_korak_postopek" itemprop="text"><span class="label">2. </span><span class="data">Med vzhajanjem pripravimo nadev. Beljak stepemo v trd sneg ob postopnem dodajanju sladkorja. Sneg enakomerno vmešamo v skuto.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf en_korak_postopek" itemprop="text"><span class="label">3. </span><span class="data">Vzhajano testo stresemo na pult, ga pregnetemo, razdelimo na šest delov in pustimo nekaj minut počivati. Nato vsak kos testa razvaljamo na krog, tega razrežemo na osem enakih delov (trikotnikov). Na zunanjo stran vsakega trikotnika položimo žličko nadeva in zato trikotnik zvijemo v rogljiček v smeri od zunanje strani z nadevom proti notranjosti – konici trikotnika. Oblikovani zvitek dokončno oblikujemo v rogljiček in ga položimo na pekač. Nadaljujemo z zvijanjem ostalih trikotnikov v rogljičke in nato še z oblikovanjem vseh ostalih kosov testa.</span></p></div><div itemprop="recipeInstructions" itemscope="" itemtype="http://schema.org/HowToStep"><p class="cf en_korak_postopek" itemprop="text"><span class="label">4. </span><span class="data">Rogljičke pustimo vzhajati na toplem. Nato jih premažemo s stepenim jajcem in prestavimo v vročo pečico. Rogljičke pečemo 20 minut na 175 stopinjah, da se lepo obarvajo.</span></p></div></div></div><br class="clear"><div id="videooglas" class="" style="height: 360px; display: block;"><iframe id="banner25" name="banner25" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="640" height="480" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=25&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,7423975" style="overflow: hidden; transform: scale(1); height: 360px;"></iframe><script>$(document).ready(function() {$('#banner25').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=25&kanal=recepti&kat=sladice&podkat=pecivo&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,7423975');});</script></div><div id="opombe" class="articlesize linki"><h2>Opombe</h2> <p>SPONZORIRANO SPOROČILO</p></div><section id="vino_container" class="Najnovejsi cf"><h2><a class="linki3" href="/vino/?kategorija=18&amp;kategorija1=140">Predlogi za vino</a></h2><div class="vinoslider flickity-enabled is-draggable" tabindex="0" style="visibility: visible;"><div class="flickity-viewport" style="touch-action: pan-y;"><div class="flickity-slider" style="left: 0px; transform: translateX(0%);"><article class="carousel-cell vino is-selected" style="position: absolute; left: 0px; transform: translateX(0%);"><a href="/vino/98/"><div class="flex"><img alt="fotografija vina" src="/slike/vino/kzkw9yszyal927g9_small.jpg" data-src="/slike/vino/kzkw9yszyal927g9_small.jpg" data-sizes="auto" data-srcset="/slike/vino/kzkw9yszyal927g9_small.jpg 50w, /slike/vino/kzkw9yszyal927g9.jpg" class="mala50 enovino lazyautosizes lazyloaded" sizes="50px" srcset="/slike/vino/kzkw9yszyal927g9_small.jpg 50w, /slike/vino/kzkw9yszyal927g9.jpg"><img alt="logotip vinarja" class="vinar" src="/slike/vinar/hc3a48dy.png"></div></a><p class="ime single-line textLeft"><a href="/vino/98/">Rumeni muškat – verduc Quercus</a></p></article><article class="carousel-cell vino" aria-hidden="true" style="position: absolute; left: 0px; transform: translateX(102.83%);"><a href="/vino/120/"><div class="flex"><img alt="fotografija vina" src="/slike/vino/hc1kv6peca7lqdj5_small.png" data-src="/slike/vino/hc1kv6peca7lqdj5_small.png" data-sizes="auto" data-srcset="/slike/vino/hc1kv6peca7lqdj5_small.png 50w, /slike/vino/hc1kv6peca7lqdj5.png" class="mala50 enovino lazyautosizes lazyloaded" sizes="50px" srcset="/slike/vino/hc1kv6peca7lqdj5_small.png 50w, /slike/vino/hc1kv6peca7lqdj5.png"><img alt="logotip vinarja" class="vinar" src="/slike/vinar/1zfnvf74.png"></div></a><p class="ime single-line textLeft"><a href="/vino/120/">Ventus Rumeni Muškat</a></p></article></div></div><button class="flickity-button flickity-prev-next-button previous" type="button" disabled="" aria-label="Previous"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow"></path></svg></button><button class="flickity-button flickity-prev-next-button next" type="button" aria-label="Next"><svg class="flickity-button-icon" viewBox="0 0 100 100"><path d="M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z" class="arrow" transform="translate(100, 100) rotate(180) "></path></svg></button><ol class="flickity-page-dots"><li class="dot is-selected" aria-label="Page dot 1" aria-current="step"></li><li class="dot" aria-label="Page dot 2"></li></ol></div><p class="vec"><a class="linki3" href="/vino/?kategorija=18&amp;kategorija1=140">Več predlogov </a></p></section>



</div>

<ul id="servis2" class="servis clearfix">

	<span class=""><a href="/recepti/seznam/?priloznost=4">#valentinovo</a><a href="/recepti/seznam/?priloznost=7">#piknik</a><a href="/recepti/seznam/?priloznost=8">#rojstni dan</a></span><span class=""><a href="/recepti/seznam/?letnicas=1">#pomlad</a><a href="/recepti/seznam/?letnicas=2">#poletje</a><a href="/recepti/seznam/?letnicas=3">#jesen</a><a href="/recepti/seznam/?letnicas=4">#zima</a></span><span class=""><a href="/recepti/seznam/?vrstaobroka=8">#prigrizki</a></span><span class=""><a href="/recepti/seznam/?vrstajedi=3">#sladice</a></span>



    </ul>

<ul class="servis cf linki"><li><a rel="noreferrer" href="https://www.facebook.com/sharer.php?u=https://www.kulinarika.net/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/" target="_blank"><img src="/grafika7/icon-facebook.svg" height="36" title="pošljite na Facebook"></a></li><li><a rel="noreferrer" href="https://twitter.com/intent/tweet?text=Roglji%C4%8Dki+s+skuto+%3A+&amp;url=https://www.kulinarika.net/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/" target="_blank"><img title="pošljite na Twitter" src="/grafika7/icon-twitter.svg" height="36"></a></li><li id="webShare" style="display: inline-block;"><img title="delite recept" src="/grafika7/icon-share.svg" height="36"></li><li><a class="link prijatelj" id="posljiprijatelju" href="mailto:?subject=Zanimiv%20recept%20na%20KULINARIKA%2ENET&amp;body=Pozdravljen%2Da%21%0D%0A%0D%0ANa%20strani%20KULINARIKA%2Enet%20sem%20zasledil%28a%29%20zanimiv%20recept%2C%20ki%20bi%20te%20morda%20zanimal%28a%29%3A%0D%0A%0D%0Ahttps%3A%2F%2Fwww%2Ekulinarika%2Enet/recepti/sladice/pecivo/rogljicki-s-skuto-/21526/"><img title="pošljite po emailu" alt="pošljite po emailu" src="/grafika7/icon-email.svg" height="24"></a></li></ul>

    



	<div id="malioglasi" class="cf">
    
    
    
    </div>

<div id="mnenja-container"><h2>Mnenja o receptu</h2><section id="mnenja" class="odprto">
										  <div class="telo2 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="1"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/dejangreifoner/">dejangreifoner</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=dejangreifoner"><img title="Pošljite uporabniku dejangreifoner zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 11.9.2013</p>
                                                 <p class="stevilo no-mobile">Št. objav: 3</p>
												  </div><div class="msgbody"><p>odlični</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  
										  <div class="telo1 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="2"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/u9bl59t1arx34dyp/">dy</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=dy"><img title="Pošljite uporabniku dy zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 23.1.2007</p>
                                                 <p class="stevilo no-mobile">Št. objav: 5</p>
												  </div><div class="msgbody">
                                                  <img src="/grafika/smile_rezanje.gif" alt="Zelo vesel" width="18" height="18" align="absbottom"> 
                                                   <p>Odlični rogljčki! Namesto skutinega nadeva sem jih nekaj napolnila s šunko in sirom, nekaj z nutelo, nekaj z mešanico masla, drobnjaka, česna in soli, nekaj pa sem jih namazala samo z  maslom in ravno tako pride odlično!</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  
										  <div class="telo2 cf "> 
											<div class="glava cf">
												
											
                                                  <a name="3"></a>
                                                  
                                                  
												  <a class="avtorMnenja" href="/uporabniki/seznam/milja44/">milja44</a>&nbsp;<a class="poslji-pismo" href="/mojakulinarika/sporocila/poslji/?naslovnik=milja44"><img title="Pošljite uporabniku milja44 zasebno sporočilo" class="email" alt="pošlji zasebno sporočilo" src="/grafika6/ikona-email.png"></a>&nbsp;<p class="kuha no-mobile">kuha že od: 2.1.2014</p>
                                                 <p class="stevilo no-mobile">Št. objav: 152</p>
												  </div><div class="msgbody"> <p>Jaz sem jih včeraj pripravila in sem zelo zadovoljna.Do sedaj izmed vseh, ki sem jih pripravljala, da ta recept najokusnejše testo. Polnila sem jih s skuto. Čista petica!</p><p>V kolikor bi jih pa polnila s šunko in sirom pa v osnovo ne pride sladkor!</p>

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-likes">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Seznam</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>


	<script type="text/javascript">
    			$(document).on({
				click: function(){
					return hs.htmlExpand(this, { width:200, maxHeight: 500, contentId: 'popup-likes', objectType: 'ajax', cacheAjax: false} )
				}
			},
			 	'.popup-likes-holder');
				
	
	</script>
    
    <div class="likes"><p class="like"><span class="like-stevilo"></span><span class="likes-holder"><a href="/mojakulinarika/prijava/"> uporabno</a></span></p></div><div class="ikonice cf"></div>
                                            </div>
										  </div>
										  </section><div class="preberivec linki" style="display: none;"><a href="javascript:void(null)">preberi več</a></div><p class="navigacijazg">Število mnenj: 3, prikazujem mnenja  od 1 do 3</p>

											<div id="pisite_skok"></div>
											
											<span class="pomembno">Za pošiljanje mnenj je potreben <a href="/mojakulinarika/vpis/">vpis</a> ali
											 <a href="/mojakulinarika/prijava/">prijava</a>!</span> 
											 
	
		<script>
		
			$(document).ready(function() {
	
				
				
				$(document).on("click", ".preberivec", function() {	
						$('#mnenja').addClass('odprto');
						$('.preberivec').hide();
				})


				if ($('#mnenja').height()>350 && isMobile)
					{
						$('#mnenja').removeClass('odprto');
						$('.preberivec').show();
					}
					
					else
					
					{
						$('.preberivec').hide();
					}
	
	})
		
		
		</script>
			
</div>
      
    </section>
	

<!-- InstanceEndEditable -->
<section id="servisniBlok" class="recepti">
<!-- InstanceBeginEditable name="neboticnik" -->

<div id="nadOglas">

    <div class="highslide-html-content highslide-my-standard-popup" id="popup-pravila">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Pogoji sodelovanja v nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-nagrade">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Več o nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-nagrade-old">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Več o potekli nagradni igri</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popup-sponzor">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">O pokrovitelju nagradne igre</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body en_clanek"></div>
    
    </div>

</div><aside class="velikanoc cf" id="info-praznik"><div class="container"><div class="recepti"><h2><a class="linki3" href="/recepti/seznam/?sort=popularnost&amp;nacin=desc&amp;priloznost=5">Velikonočne jedi</a></h2><a class="linki3" href="/recepti/sladice/potice/orehova-potica/1176/">Orehova potica</a><a class="linki3" href="/recepti/sladice/potice/kokosova-potica/4255/">Kokosova potica</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica-st-2/1667/">Potratna potica št. 2</a><a class="linki3" href="/recepti/sladice/potice/orehova-rulada/5737/">Orehova rulada</a><a class="linki3" href="/recepti/sladice/potice/nocna-potica/2889/">Nočna potica</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica/18232/">Potratna potica</a><a class="linki3" href="/recepti/sladice/potice/pehtranova-potica/378/">Pehtranova potica</a><a class="linki3" href="/recepti/sladice/potice/marmorni-kolac-iz-jogurta-/14691/">Marmorni kolač (iz jogurta)</a><a class="linki3" href="/recepti/sladice/potice/domaci-prijatelj-tete-dragice/12332/">Domači prijatelj tete Dragice</a><a class="linki3" href="/recepti/sladice/potice/vsestransko-testo/11944/">Vsestransko testo</a><a class="linki3" href="/recepti/sladice/potice/krhka-pita-za-vsak-okus/6439/">Krhka pita za vsak okus</a><a class="linki3" href="/recepti/sladice/potice/potratna-potica/1390/">Potratna potica</a></div></div><p class="vec"><a class="linki3" href="/recepti/seznam/?sort=popularnost&amp;nacin=desc&amp;priloznost=5">več receptov za Veliko noč</a></p></aside><div class="cf" id="oglasi-stranski"><div id="oglas-aside2" class=""><iframe id="banner3" name="banner3" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="300" height="600" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=3&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,6190867"></iframe><script>$(document).ready(function() {$('#banner3').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=3&kanal=recepti&kat=sladice&podkat=pecivo&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,6190867');});</script></div></div><aside class="ReceptiVroci cf"><h2><a href="/recepti/seznam/?avtor=Fala Slonček">Več receptov - Fala Slonček</a></h2><div class="mobileslider najboljvroci" style="visibility: visible;"><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/aromaticni-adventni-venec/22087/"><img alt="fotografija recepta" src="/slikerecepti/22087/1-200x150.webp" data-src="/slikerecepti/22087/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/22087/1-200x150.webp 200w, /slikerecepti/22087/1-400x300.webp 400w" class="lazyautosizes ls-is-cached lazyloaded" sizes="145px" srcset="/slikerecepti/22087/1-200x150.webp 200w, /slikerecepti/22087/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/aromaticni-adventni-venec/22087/">Aromatični adventni venec</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/sladice/pecivo/muskatne-rezine-s-hruskami/21133/"><img alt="fotografija recepta" src="/slikerecepti/21133/1-200x150.webp" data-src="/slikerecepti/21133/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/21133/1-200x150.webp 200w, /slikerecepti/21133/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/21133/1-200x150.webp 200w, /slikerecepti/21133/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/pecivo/muskatne-rezine-s-hruskami/21133/">Muškatne rezine s hruškami</a></div><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/ostalo/vanilijeva-pogaca-z-malinami-in-mandlji/20735/"><img alt="fotografija recepta" src="/slikerecepti/20735/1-200x150.webp" data-src="/slikerecepti/20735/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/20735/1-200x150.webp 200w, /slikerecepti/20735/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/20735/1-200x150.webp 200w, /slikerecepti/20735/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/ostalo/vanilijeva-pogaca-z-malinami-in-mandlji/20735/">Vanilijeva pogača z malinami in mandlji</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/sladice/potice/razprta-kokosova-potica-v-cokoladnem-testu/20909/"><img alt="fotografija recepta" src="/slikerecepti/20909/1-200x150.webp" data-src="/slikerecepti/20909/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/20909/1-200x150.webp 200w, /slikerecepti/20909/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/20909/1-200x150.webp 200w, /slikerecepti/20909/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/potice/razprta-kokosova-potica-v-cokoladnem-testu/20909/">Razprta kokosova potica v čokoladnem testu</a></div><div class="vroci levo"><div class="slika"><a class="image-wrap " href="/recepti/sladice/potice/mandljeva-potica-v-cokoladnem-testu/21955/"><img alt="fotografija recepta" src="/slikerecepti/21955/1-200x150.webp" data-src="/slikerecepti/21955/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/21955/1-200x150.webp 200w, /slikerecepti/21955/1-400x300.webp 400w" class="lazyautosizes ls-is-cached lazyloaded" sizes="145px" srcset="/slikerecepti/21955/1-200x150.webp 200w, /slikerecepti/21955/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/sladice/potice/mandljeva-potica-v-cokoladnem-testu/21955/">Mandljeva potica v čokoladnem testu</a></div><div class="vroci "><div class="slika"><a class="image-wrap " href="/recepti/kruh/pletenka-s-petimi-prameni-in-mandljevimi-listici/22479/"><img alt="fotografija recepta" src="/slikerecepti/22479/1-200x150.webp" data-src="/slikerecepti/22479/1-200x150.webp" data-sizes="auto" data-srcset="/slikerecepti/22479/1-200x150.webp 200w, /slikerecepti/22479/1-400x300.webp 400w" class="lazyautosizes lazyloaded" sizes="145px" srcset="/slikerecepti/22479/1-200x150.webp 200w, /slikerecepti/22479/1-400x300.webp 400w"></a></div><a class="link single-line" href="/recepti/kruh/pletenka-s-petimi-prameni-in-mandljevimi-listici/22479/">Pletenka s petimi prameni in mandljevimi lističi</a></div></div></aside><div id="zid-include"></div>

    <div class="highslide-html-content highslide-my-standard-popup" id="prijatelj">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Pošlji prijatelju</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="my-ocena">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Ocenite recept</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="ocenerecepta">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Ocene recepta</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="pomoc-priporocamo">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Zraven tekne</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="pomoc-vino">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Vinski kotiček</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body "></div>
    
    </div>



    <div class="highslide-html-content highslide-my-standard-popup" id="popupSubscribed">
        <div class="highslide-header">
        
                             <div class="FotoAlbumPremakniSliko_handle">			
                        <div class="highslide-move" onclick="return false">
                        
                         
                        <span><a href="#" onclick="return hs.close(this)">✕</a></span><div class="highslide-heading">Naročeni ste na nova mnenja</div>
                        
                        </div>
              </div>
        
        </div>
        <div class="highslide-body ">Ko bo nekdo napisal novo mnenje k temu receptu, boste o tem dobili e-mail obvestilo (le enkrat, dokler ne odprete spet tega recepta). Na naročanje se lahko odjavite na samem receptu ali pa iz beležke.</div>
    
    </div>


    <!-- InstanceEndEditable -->
</section>
</main>
</div>
<div class="push"></div>
</div>



<footer class="footer cf">

<!-- The Modal -->
	<div id="myModal" class="modal">

	  <!-- Modal content -->
	  <div class="modal-content">
	    	<div class="img_wrap"><img alt="prazno" src="/images/prazno.jpg"></div>
	    	<div class="txt_wrap">
	    		<h3>Zaznan je blokator oglasov</h3>
				<p>Vsebina Kulinarika.net je podprta z oglaševanjem. Če želite še naprej uživati v naših receptih, izklopite blokiranje oglasov.</p>
				<h4>Prosimo vas, da za našo spletno stran onemogočite blokiranje oglasov.</h4>
				<!-- <p>Onemogoči blokiranje oglasov<p> -->
				<a href="javascript:void(0);" class="close_modal">Nadaljujte z blokiranjem oglasov</a>
			</div>
	  </div>

	</div>

    <div id="footer-top">
      
    </div>
	<div class="cf" id="footer-main">
	<p>© 2025 Spletna kulinarika d.o.o.</p>
	<ul>
    
		<li><a href="/oglasevanje/">Trženje</a></li>	
		<li><a href="/pravo/">Pogoji uporabe</a></li>
		<li><a href="/zasebnost/">Zasebnost</a></li>
		
   		<li><a href="/faq/">Pomoč</a></li>
        <li><a href="/zanimivo/dogodki/">Dogodki</a></li>
        
		<li><a href="/uporabniki/seznam/">Člani</a></li>
	</ul>
</div>

  
</footer>

<script>
<!--//<![CDATA[
if (isMobile == true) {
var ox_u = 'https://oglasi2.kulinarika.net/www/delivery/al.php?zoneid=24&layerstyle=simple&align=left&valign=top&padding=0&padding=0&shifth=0&shiftv=0&closebutton=t&nobg=t&noborder=t';
if (document.context) ox_u += '&context=' + escape(document.context);
document.write("<scr"+"ipt src='" + ox_u +"'></scr"+"ipt>");
}
//]]>--></script>

<div id="bottomAdWrapper">

        <div id="adContainer" style="height: 128.711px; visibility: visible; bottom: 0px;">
            <div id="closeButton"></div>
            <div id="scaleContainer" style="transform: scale(0.494845); width: 970px; height: 250px;">
                <iframe id="banner1" name="banner1" referrerpolicy="no-referrer-when-downgrade" frameborder="0" scrolling="no" width="980" height="250" allowtransparency="true" src="https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=1&amp;kanal=recepti&amp;kat=sladice&amp;podkat=pecivo&amp;user=ms4mp69e30x9541q&amp;target=_blank&amp;refresh=240&amp;cb=0,5038661"></iframe><script>$(document).ready(function() {$('#banner1').attr('src', 'https://oglasi2.kulinarika.net/www/delivery/afr.php?zoneid=1&kanal=recepti&kat=sladice&podkat=pecivo&user=ms4mp69e30x9541q&target=_blank&refresh=240&cb=0,5038661');});</script>
            </div>
        </div>
</div>

<script>
        // Create a namespace for the ad functionality
        const bottomAD = window.bottomAD || {};

        (function(namespace) {
            function showAd() {
                const adContainer = document.getElementById('adContainer');
                if (adContainer) {
                    adContainer.style.visibility = 'visible';
                    adContainer.style.bottom = '0';
                }
            }

            function hideAd() {
                const adContainer = document.getElementById('adContainer');
                if (adContainer) {
                    adContainer.style.bottom = '-250px';
                }
            }

            function debounce(func, wait) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        clearTimeout(timeout);
                        func(...args);
                    };
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                };
            }

			function resizeAd() {
				const scaleContainer = document.getElementById('scaleContainer');
				const adContainer = document.getElementById('adContainer');
				
				if (!scaleContainer || !adContainer) {
					console.error('One or more ad elements not found');
					return;
				}

				try {
					const windowWidth = window.innerWidth;
					const maxWidth = 480;
					const originalWidth = 970;
					const originalHeight = 250;

					const scale = Math.min(maxWidth, windowWidth) / originalWidth;
					const scaledHeight = originalHeight * scale;

					scaleContainer.style.transform = `scale(${scale})`;
					scaleContainer.style.width = `${originalWidth}px`;
					scaleContainer.style.height = `${originalHeight}px`;
					adContainer.style.height = `${scaledHeight + 5}px`; // 5px for padding
				} catch (error) {
					console.error('Error resizing ad:', error);
				}
			}

            // Expose functions in the namespace
            namespace.showAd = showAd;
            namespace.hideAd = hideAd;

            // Trigger the ad after 5 seconds (as an example)
            setTimeout(namespace.showAd, 5000);

            // Add debounced event listener for resizing
            const debouncedResize = debounce(resizeAd, 250);
            window.addEventListener('resize', debouncedResize);
            resizeAd(); // Initial resize

            // Close button event listener
            const closeButton = document.getElementById('closeButton');
            if (closeButton) {
                closeButton.addEventListener('click', namespace.hideAd);
            }
        })(bottomAD);
    </script>


</div>

<!-- InstanceBeginEditable name="dno" -->

<script>
const bannerModule = (function() {
    let lastKnownScrollPosition = 0;
    let ticking = false;
    let container, iframe, bottomBanner;
    let isParallaxVisible = true;
    let parallaxActive = window.innerWidth < 768;

    function easeInOutCubic(t) {
        return t < 0.5
            ? 4 * t * t * t
            : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }

    function resetStyles() {
        if (iframe) {
            iframe.style.transform = '';
        }
        if (bottomBanner) {
            bottomBanner.style.opacity = '';
        }
    }

    function updateParallax() {
        if (!parallaxActive) return;
        if (!isParallaxVisible) return;
        const containerRect = container.getBoundingClientRect();
        const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
        const scrollPercentage =
            (viewportHeight - containerRect.top) /
            (viewportHeight + containerRect.height);
        // Parallax effect
        if (scrollPercentage > 0 && scrollPercentage < 1) {
            const easedScrollPercentage = easeInOutCubic(scrollPercentage);
            const moveY =
                (easedScrollPercentage - 0.5) * containerRect.height * 0.5;
            iframe.style.transform = `translate(-50%, -50%) translateY(${moveY}px)`;
        }
        // Bottom banner visibility
        const buffer = 200; // Buffer for smoother transition
        let opacity = 1;
        if (containerRect.bottom > 0 && containerRect.top < viewportHeight) {
            opacity = 0;
        } else if (containerRect.bottom <= 0) {
            opacity = Math.min(1, (-containerRect.bottom) / buffer);
        } else if (containerRect.top >= viewportHeight) {
            opacity = Math.min(1, (containerRect.top - viewportHeight) / buffer);
        }
        opacity = Math.max(0, Math.min(1, opacity));
        bottomBanner.style.opacity = opacity;
        ticking = false;
    }

    function onScroll() {
        lastKnownScrollPosition = window.pageYOffset;
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateParallax();
            });
            ticking = true;
        }
    }

    function toggleParallax() {
        isParallaxVisible = !isParallaxVisible;
        container.style.display = isParallaxVisible ? 'block' : 'none';
        bottomBanner.style.display = isParallaxVisible ? 'flex' : 'none';
        if (isParallaxVisible) {
            updateParallax();
        }
    }

    function onResize() {
        let newParallaxActive = window.innerWidth < 768;
        if (newParallaxActive && !parallaxActive) {
            // Switched from desktop to mobile
            parallaxActive = true;
            init();
        } else if (!newParallaxActive && parallaxActive) {
            // Switched from mobile to desktop
            parallaxActive = false;
            // Reset styles and remove event listeners
            resetStyles();
            window.removeEventListener('scroll', onScroll);
        }
    }

    function init() {
        container = document.querySelector('#oglas-aside2');
        iframe = document.querySelector('#banner3');
        bottomBanner = document.querySelector('#adContainer');

        if (window.innerWidth >= 768) {
            // Reset styles on larger screens
            resetStyles();
            parallaxActive = false;
            return;
        }
        parallaxActive = true;
        window.addEventListener('scroll', onScroll, { passive: true });
        // Initial update
        updateParallax();
    }

    // Public methods
    return {
        init: init,
        toggleParallax: toggleParallax,
        onResize: onResize
    };
})();

// Initialize the module
document.addEventListener('DOMContentLoaded', function() {
    bannerModule.init();
    window.addEventListener('resize', bannerModule.onResize);
});
    </script>

<!-- InstanceEndEditable -->
<a href="#0" class="cd-top" title="na vrh">↑</a>


<div id="ad-container" class="ad-container"></div></body><iframe id="google_esf" name="google_esf" src="https://pagead2.googlesyndication.com/pagead/html/r20250403/r20190131/zrt_lookup_fy2021.html" style="display: none;"></iframe><!-- InstanceEnd --></html>
"""

from bs4 import BeautifulSoup

def cleaned(html_content):
  """Izpiše cleaned content za posamezno stran."""
  soup = BeautifulSoup(html_content, 'html.parser')
  section = soup.find('section', id='recepti')
  return str(section)

slovar_zahtevnosti = {1: 'zelo lahek', 2: 'lahek', 3: 'srednje težek', 4: 'težek', 5: 'zelo težek'}
slovar_pretvorb = {'g': 'gramov', 'mg': 'miligramov', 'kg': 'kilogramov', 'dag': 'dekagramov', 'ml': 'mililitrov',
                                'l': 'litrov', 'dl': 'decilitrov'}

def opis(html_content):
  """Izpiše tri stavke, ki opisujejo page_segment 'OPIS'."""
  tree = html.fromstring(html_content)
  podnaslov = tree.xpath('//div[@id="recept-main"]/p/text()')[0]
  ura = re.search(r'<span class="cas">([^<]+)<\/span>', html_content).group(1)
  zahtevnost = len(tree.xpath('//li[@class="zahtevnost"]/img[@src="/grafika6/ikona-utez.png"]'))
  print(f"Opis recepta je '{podnaslov.strip()}'. Za recept porabimo {ura.strip()}. Recept je {slovar_zahtevnosti[zahtevnost]}.")

opis(cleaned(html_c))

def komentarji(html_content):
  """Izpiše stavke o komentarjih za posamezen recept."""
  #opombe = tree.xpath('//*[@id="opombe"]/p/text()')
  avtorji = re.findall(r'<a\s+class="avtorMnenja"[^>]*>(.*?)<\/a>', html_content)
  komentarji = re.findall(r'<div\s+class="msgbody"[^>]*>(?:[^<]|<(?!p\b))*<p>(.*?)<\/p>', html_content)
  izpis = ""
  for a,k in list(zip(avtorji, komentarji)):
     izpis += f"{a} je zapisal '{k}'.\n"
  print(izpis)

komentarji(cleaned(html_c))

def postopek(html_content):
  """Izpiše cel text za postopek."""
  tree = html.fromstring(html_content)
  p = tree.xpath('//div[@id="postopek"]')[0].text_content().strip()
  print(p)

postopek(cleaned(html_c))

def pretvori(niz):
    niz = niz.split()
    nov = []
    for i, n in enumerate(niz):
        if i > 0 and any(c.isdigit() for c in niz[i-1]) and n in slovar_pretvorb:
            nov.append(slovar_pretvorb[n])
        else:
            nov.append(n)
    return ' '.join(nov)
print(pretvori('250 ml mleka'))

def sestavine(html_content):
  """Izpiše cel text za sestavine."""
  tree = html.fromstring(html_content)
  izpis = ""
  sestavine_vsi_p = tree.xpath('//div[@id="sestavine"]/p[@class="cf"] | //div[@id="sestavine"]/p[@class="cf poglavje"]')
  for p in sestavine_vsi_p:
        p0 = p[0].text_content().strip()
        p1 = p[1].text_content().strip()

        p0 = p0.replace('\u200b', '').strip()
        p1 = p1.replace('\u200b', '').strip()

        if 'poglavje' in p.get('class', ''):
            izpis += f"\n{p1}\n"
        else:
            if p0 == "":
                line = f"{pretvori(p1)}"
            else:
                line = f"{pretvori(p0)} {pretvori(p1)}".replace('  ', ' ')
            izpis += f"{line}\n"

  print(izpis.strip())

sestavine(cleaned(html_c))

def tags(html_content):
  """Izpiše seznam vseh tagov # za posamezen recept."""
  tree = html.fromstring(html_content)
  vsi_tagi = tree.xpath('//section[@id="recepti"]/ul[@id="servis2"]/span/a/text()')
  print(vsi_tagi)

tags(cleaned(html_c))

  
