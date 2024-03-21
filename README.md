# ENDF Analyzer

ENDF (Evaluated Nuclear Data File) analyzer made for https://wwwndc.jaea.go.jp/ENDF_Graph/.
Currently computes the y-axis average based on a range of energy values for JENDL-5.

### How to use

This assumes you have matplotlib, pandas, and numpy installed in your Python interpreter library.

1. On https://wwwndc.jaea.go.jp/ENDF_Graph/, ensure you have JENDL-5 selected for the dataset. Insert desired values into Nuclides and MT Numbers section.

2. Click "Draw Graph", then download the .plot file by clicking "Plot Data".

3. Clone the repository, then move the .plot file into the "data" folder.

4. Navigate to main.py, then modify the values outlined in the file, if necessary (most of them are default values)

5. Run the file. The graph should display in a new window and the average values should be logged in the console.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
