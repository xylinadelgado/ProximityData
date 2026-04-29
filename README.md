# Proximity Data Analyzer

## Overview

This project is a simple Python program that simulates and analyzes proximity sensor data. It processes distance values and categorizes them into safety levels such as **SAFE**, **WARNING**, and **TOO CLOSE**.

The goal of this project was to practice Python fundamentals and explore how sensor data can be interpreted programmatically.

---

## Features

* Classifies distance readings into safety categories
* Calculates summary statistics (average, minimum, maximum)
* Displays results in a clear, readable format

---

## Technologies Used

* Python 3

---

## How It Works

The program takes a list of distance values (in centimeters) and:

1. Iterates through each value
2. Determines its safety level based on thresholds
3. Outputs the classification
4. Calculates overall statistics

---

## Example Output

35 cm -> SAFE
22 cm -> WARNING
9 cm -> TOO CLOSE

Summary:
Average Distance: 23.29 cm
Closest Object: 9 cm
Farthest Object: 40 cm

---

## How to Run

1. Make sure Python 3 is installed
2. Navigate to the project folder
3. Run the following command:

```
python3 main.py
```

---

## Future Improvements

* Accept real-time data from an Arduino sensor
* Save results to a CSV file
* Add data visualization (graphs)

---

## Author

Xylina D

---

## Notes

This project was created as a refresher on Python and to explore how software can be used to analyze sensor data.
