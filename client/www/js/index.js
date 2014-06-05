/**
 * 
 */

PREFIX_URL = "http://localhost:8888"

function getArgument() {
	return JSON.parse(localStorage.argument);
}

function setArgument(argument) {
	localStorage.argument = JSON.stringify(argument);
}

$(document).on("pageinit", "#schoolinfos", function() {
	
	$(document).on("tap", ".schoolinfos-schoolitem", function() {
		setArgument({"schoolID":$(this).find("input").val()});
	});
	
	$(document).on("pagebeforeshow", "#schoolinfos", function() {
		loadSchoolInfos();
	});
	
	function loadSchoolInfos() {
		$.ajax({
			url:PREFIX_URL+"/schoolinfos",
			dataType:"json",
			success:function(data) {
				var list = new Array();
				for (var i = 0; i < data.result.length; i++) {
					var school_info = {};
					school_info.id = data.result[i].id;
					school_info.name = data.result[i].name;
					school_info.sat = data.result[i].sat;
					school_info.toefl = data.result[i].toefl;
					school_info.englishName = data.result[i].englishName;
					list[i] = school_info;
				}
				var result = {"list":list};
				$("#schoolinfos-content").html(Handlebars.compile($("#schoolinfos-content-template").html())(result));
				$("#schoolinfos-content").listview("refresh");
			}
		});
	}
});

$(document).on("pageinit", "#schoolinfo", function() {
	
	$(document).on("pagebeforeshow", "#schoolinfo", function() {
		var schoolID = getArgument().schoolID;
		loadSchoolInfo(schoolID);
	});
	
	function loadSchoolInfo(schoolID) {
		$.ajax({
			url:PREFIX_URL+"/schoolinfo/"+schoolID,
			dataType:"json",
			success:function(data) {
				result = {};
				$("#schoolinfo-schoolname").text(data.result.schoolName);
				$("#schoolinfo-schoolprofile").text(data.result.schoolProfile);
				$("#schoolinfo-admissionstatus").text(data.result.admissionStatus);
			}
		});
	}
});

$(document).on("pageinit", "#candidatesrecommendation", function() {
	
	$(document).on("pagebeforeshow", "#candidatesrecommendation", function() {
		var sat = getArgument().sat;
		var toefl = getArgument().toefl;
		var discipline = getArgument().discipline;
		loadCandidatesRecommendation(sat, toefl, discipline);
	});

	
	$(document).on("tap", ".candidatesrecommendation-schoolitem", function() {
		setArgument({"schoolID":$(this).find("input").val()});
	});
	
	function loadCandidatesRecommendation(sat, toefl, discipline) {
		$.ajax({
			url:PREFIX_URL+"/candidatesrecommendation",
			dataType:"json",
			type:"POST",
			data:{"sat":sat, "toefl":toefl, "discipline":discipline},
			success:function(data) {
				list = new Array();
				for (var i = 0; i < data.result.length; i++) {
					school_info = {};
					school_info.id = data.result[i].id;
					school_info.name = data.result[i].name;
					school_info.rate = data.result[i].rate;
					list[i] = school_info;
				}
				var result = {"list":list};
				$("#candidatesrecommendation-content").html(Handlebars.compile($("#candidatesrecommendation-content-template").html())(result));
				$("#candidatesrecommendation-content").listview("refresh");
			}
		});
	}
});

$(document).on("pageinit", "#candidatestools", function() {
	
	$(document).on("tap", "#candidatestools－calculate", function() {
		var sat = $("#candidatestools－sat").val();
		var toefl = $("#candidatestools－toefl").val();
		var discipline = $("#candidatestools－discipline").val();
		setArgument({
			"sat":sat,
			"toefl":toefl,
			"discipline":discipline,
		});
	});
});
