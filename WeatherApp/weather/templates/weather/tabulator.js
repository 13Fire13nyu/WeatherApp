$(document).ready(function() {
    var url = 'https://cp.simpple.ru/api/v1/widgets/ratings/753bf174295992b3ca2d0bd4a78d6598/popular&limit=8';
    $.get(url, function(response) {
        var table = new Tabulator('#paged', {
			data: JSON.parse(response),
			layout: 'fitColumns',
			columns: [
				{ title: 'Дата', field: 'date' },
				{ title: 'Время (московское)', field: 'time'},
				{ title: 'T', field: 't' },
				{ title: 'Отн. влажность воздуха, %', field: 'ran' },
				{ title: 'Td', field: 'td'},
				{ title: 'Атм. давление, мм рт. ст.', field: 'atm_pres' },
				{ title: 'Направление ветра', field: 'wind_dir' },
				{ title: 'Скорость ветра, м/с', field: 'wind_speed'},
				{ title: 'Облачность, %', field: 'cloudiness' },
				{ title: 'h', field: 'h' },
				{ title: 'VV', field: 'vv'},
				{ title: 'Погодные явления', field: 'wconditions' },
			]
		});
    });
});