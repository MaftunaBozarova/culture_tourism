/**
 * Created by Umar on 02.11.2016.
 */
$(document).ready(function() {

var minFontSize = 15;
var maxFontSize = 25;


$('#random').find('a').each(function(e) {
$(this).css("fontSize", randomNumberGenerator(minFontSize, maxFontSize));
});

function randomNumberGenerator(min,max)
{return Math.floor(Math.random()*(max-min+1)+min);}
});