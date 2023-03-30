//CODE AND DESIGN - CHARLIE GIANNIS
//declaration of independance
var iconsDarkSky = ["clear-day", "clear-night", "rain", "snow", "sleet", "wind", "fog", "cloudy", "partly-cloudy-day", "partly-cloudy-night"];
var iconsLocal = ["FAIR", "FAIR", "RAIN", "SNOW", "RAIN", "WIND", "HAZE", "CLOUD", "SUNCLOUD", "SUNCLOUD"];
var monthsList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"];
var cohortWeeks = [["a", "b", "a", "b", "a"], ["c", "d", "c", "d", "c"], ["a", "b", "a", "b", "b"], ["c", "d", "c", "d", "d"]];
//broken
var cohortSundays = ["10-11,11-8,12-13,1-24,2-7,3-7,4-4,4-11,4-25,5-23,6-20", "10-18,11-22,1-3,1-31,2-14,3-14,4-18,5-2,5-30", "9-27,10-25,11-29,1-10,2-21,3-14,3-28,5-9,6-6", "10-4,11-1,12-6,1-17,2-28,4-4,5-16,6-13"];

//UPDATE TIME WIDGET - every second
setInterval(changeTime, 1000);
function changeTime() {
  var time = new Date();
  document.getElementById("time").innerHTML = (((time.getHours() + 11) % 12) + 1) + ":" + (time.getMinutes() < 10 ? ("0" + time.getMinutes()) : time.getMinutes());
  document.getElementById("amorfm").innerHTML = time.getHours() > 11 ? "PM" : "AM";
}

//UPDATE WEATHER - every 20 minutes
getWeather();
setInterval(getWeather, 1200000);
function getWeather() {
  //Making JQuery request to darksky
  $.ajax({
    url: "https://api.darksky.net/forecast/d712ece6761d6d8f669039ea673ab789/43.5951,-79.5165",
    dataType: 'jsonp',
    success: function(data, status) {
      //updating weather icon and temperature
      document.getElementById("weatherInfo").style.backgroundImage = "url(\"weatherIcons/" + (iconsLocal[iconsDarkSky.indexOf(data.currently.icon)]) + ".png\")";
      document.getElementById("temp").innerHTML = Math.round((data.currently.temperature - 32) * (5 / 9)) + "\u00B0";
    }
  });
  //running the schedule and date update function in this weather loop
  updateSchedule();
}

//UPDATE SCHEDULE FUNCTION - with getWeather
updateSchedule();
function updateSchedule() {
  //update month and day number
  var time = new Date();
  document.getElementById("month").innerHTML = monthsList[time.getMonth()];
  document.getElementById("dayNum").innerHTML = time.getDate();
  //clearing old weekday glows
  for (var wd = 1; wd < 6; wd++) {
      document.getElementById("day" + wd).style = "border-radius: 15px;background: #FFFFFF00;";
  }
  //update weekday glow
  if (time.getDay() > 0 && time.getDay() < 6) {
    document.getElementById("day" + time.getDay()).style = "border-radius: 15px;background: #FFFFFF66;";
  }
  //get last sunday, compare it to cohortSundays to get this weeks cohort (0 - 3)
  var d = new Date();
  d.setDate(d.getDate() - time.getDay());
  var currentWeek = 0;
  var lastSunday = ((d.getMonth() + 1) + "-" + d.getDate());
  for (var weeks = 0; weeks < 4; weeks++) {
    if (cohortSundays[weeks].indexOf(lastSunday) != -1) {
      currentWeek = weeks;
    }
  }
  
  //update cohort week schedule
  document.getElementById("coh0").src = "cohortIcons/" + (cohortWeeks[currentWeek][0]) + "white.png";
  document.getElementById("coh1").src = "cohortIcons/" + (cohortWeeks[currentWeek][1]) + "white.png";
  document.getElementById("coh2").src = "cohortIcons/" + (cohortWeeks[currentWeek][2]) + "white.png";
  document.getElementById("coh3").src = "cohortIcons/" + (cohortWeeks[currentWeek][3]) + "white.png";
  document.getElementById("coh4").src = "cohortIcons/" + (cohortWeeks[currentWeek][4]) + "white.png";
}
