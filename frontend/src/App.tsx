import React, { useEffect, useState } from 'react';
import './App.css';
import 'react-dates/initialize';
import { DateRangePicker } from 'react-dates';
import 'react-dates/lib/css/_datepicker.css';
import moment from "moment";
import axios from "axios"
import AreaChart from "./components/AreaChart/AreaChart";
import Stats from "./interfaces/Stats";
import Dates from "./interfaces/Dates";
import DisplayStats from "./components/DisplayStats/DisplayStats";


function formatDate(date:any) {
  let month = (date.month() + 1 < 10) ? `0${date.month() + 1}` : date.month() + 1
  let day = (date.date() < 10) ? `0${date.date()}` : date.date()
  let newFormat = `${date.year()}-${month}-${day}`
  return newFormat
}

function transformIntoTimeValueList(list:any) {
  list = list.map((item: any) => {
    let date = Date.parse(item.date);
    let value = item.value
    return [date, value]
  })
  return list
}

function App() {
  const [startDate, setStartDate] = useState(moment);
  const [endDate, setEndDate] = useState(moment);
  const [focusedInput, setFocusedInput] = useState(null);
  const [dollarData, setDollarData] = useState([])
  const [UDISData, setUDISData] = useState([])
  const [dollarStats, setDollarStats] = useState({max: 0, min: 0, avg: 0})
  const [UDISStats, setUDISStats] = useState({max: 0, min: 0, avg: 0})

  useEffect(() => {
    if (startDate && endDate) {

      let startRange = formatDate(startDate);
      let endRange = formatDate(endDate);
      
      
      axios.get(`http://localhost:5000/dollars?start_date=${startRange}&end_date=${endRange}`, {headers: { 'Content-Type': 'application/json'}})
        .then((response) => {
          const data = transformIntoTimeValueList(response.data.data)
          const { max, min, avg }: Stats = {...response.data}
          setDollarStats({ max, min, avg })
          setDollarData(data)
        })
        .catch((error) => {
            console.log(error);
        });
      
      axios.get(`http://localhost:5000/UDIS?start_date=${startRange}&end_date=${endRange}`, {headers: { 'Content-Type': 'application/json'}})
        .then((response) => {
          const data = transformIntoTimeValueList(response.data.data)
          const { max, min, avg }: Stats = { ...response.data }
  
          setUDISStats({ max, min, avg })
          setUDISData(data)
        })
        .catch((error) => {
            console.log(error);
        });
      
    }
  }, [startDate, endDate]);
  return (
    <div className="App">
      <DateRangePicker
        startDate={startDate} // momentPropTypes.momentObj or null,
        startDateId="start_date" // PropTypes.string.isRequired,
        endDate={endDate} // momentPropTypes.momentObj or null,
        endDateId="end_date" // PropTypes.string.isRequired,
        onDatesChange={({ startDate, endDate }: Dates) => { setStartDate(startDate); setEndDate(endDate); }} // PropTypes.func.isRequired,
        focusedInput={focusedInput} // PropTypes.oneOf([START_DATE, END_DATE]) or null,
        onFocusChange={(focusedInput: any) => setFocusedInput(focusedInput)} // PropTypes.func.isRequired,
        isOutsideRange={() => false}
      />
      <DisplayStats { ...UDISStats }/>
      <AreaChart title={"UDIS"} data={UDISData} />
      <DisplayStats { ...dollarStats }/>
      <AreaChart title={"Dolar"} data={dollarData} />
    </div>
  );
}

export default App;
