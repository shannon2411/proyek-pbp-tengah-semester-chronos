const endpoint1 = $("#linechart").attr("data-url");
const endpoint2 = $("#searchform").attr("data-url");

// Ajax Variant 1 for Chart
$.ajax({
    method: "GET",
    url: endpoint1,
}).done((data) => {
    const ctx = document.getElementById('linechart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Kasus Positif',
                data: data.dataPositif,
                backgroundColor: 'rgba(255, 205, 86, 0.2)',
                borderColor: 'rgb(255, 205, 86)',
                borderWidth: 1
            },
            {
                label: 'Kasus Meninggal',
                data: data.dataMeninggal,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 1
            },
            {
                label: 'Kasus Sembuh',
                data: data.dataRecovery,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            interaction: {
                mode: 'point',
            },

            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Tanggal'
                    }
                },
                y: {
                    display: true,
                    beginAtZero: false,
                    title: {
                        display: true,
                        text: 'Jumlah Kasus'
                    }
                }
            }
        }
    })
});

// Ajax Variant 2 for Query Provinsi
$(document).ready(function(){
    $("#submit").on('click',function(){
        // Run Ajax
        $.ajax({
            type:'GET',
            url:endpoint2,
            data:{
                'query': $("#queryInput").val(),
            },
            success: function(res){
                $(".wrap").html(res['html_from_view']);
            }
        });
    });
});
