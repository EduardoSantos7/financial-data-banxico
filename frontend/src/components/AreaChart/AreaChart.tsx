import React from 'react'
import ReactApexChart from 'react-apexcharts';

interface AreaChartProps {
    title: string
    data: any
}

export default function AreaChart(props: AreaChartProps) {
    let series = [
				{
					name: props.title,
					data: props.data
				}
			]
    let options = {
        chart: {
            type: 'area',
            zoom: {
                enabled: true
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'straight'
        },

        title: {
            text: props.title,
            align: 'left'
        },
        subtitle: {
            text: 'Precio por día',
            align: 'left'
        },
        xaxis: {
            type: 'datetime'
        },
        yaxis: {
            opposite: true
        },
        legend: {
            horizontalAlign: 'left'
        }
    }
    return (
        <div id="chart">
            <ReactApexChart options={options} series={series} type="area" height={350} />
        </div>
    )
}