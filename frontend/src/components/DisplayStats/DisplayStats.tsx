import React from 'react'
import Stats from "../../interfaces/Stats";

export default function DisplayStats(props: Stats) {
    return (
        <div>
            Max: {props.max} Min: {props.min} Prom: {props.avg}
        </div>
    )
}
