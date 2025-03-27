# ElliShape

[![PyPI version](https://badge.fury.io/py/ElliShape.svg)](https://badge.fury.io/py/ElliShape)

A graphical user interface tool for shape analysis using Elliptic Fourier Descriptors (EFD).

## Description
A user-friendly software designed to offer improved contour extraction, efficient EFDs calculation, and complete EFD normalization across all basic contour transformations.

## Installation

#### Preparation Steps:
Option 1. Install Conda (if not already installed):
    - Download Anaconda from the official website:
      https://www.anaconda.com/
    - Follow the installation instructions for your operating system

Option 2. Install Python (if not using Conda):
    - Download Python 3.8 or later from the official website: https://www.python.org/downloads/ 
    - Follow the installation instructions and ensure you select the option to add Python to your system PATH

#### Installation and Usage with Conda:
1. Open the Anaconda Prompt 
2. Create a Conda environment with Python 3.8:
    ```Anaconda Prompt
    conda create -n ElliShape python=3.8
    ```
3. Activate the environment:
    ```Anaconda Prompt
    conda activate ElliShape
    ```
4. Install the ElliShape package:
    ```Anaconda Prompt
    pip install  ElliShape
    ```
4. Download the required model weight files:
    ```Anaconda Prompt
    python path/to/download_pth.py
    ```
5. Run ElliShape:
    ```Anaconda Prompt
    ElliShape
    ```

#### Direct Installation with Python :
1. Open the Command Prompt
2. Install the ElliShape package:
    ```cmd
    pip install  ElliShape
    ```
3. Download the required model weight files:
    ```cmd
    python path/to/download_pth.py
    ```
4. Run ElliShape:
    ```cmd
    ElliShape
    ```

#### Notes:
- Ensure your environment meets the Python version requirements.
- The model weight files are essential for running ElliShape. Make sure to download them before using the software.
- For detailed documentation and troubleshooting, refer to the official website or contact support.

## Functions

The software comprises two components: contour extraction and elliptic
Fourier analysis.

Contour extraction involves four steps: manual target selection,
automatic segmentation, manual correction of automatic contour
outlining, and automatic chain code generation. Various functions
address challenges of contour extraction during specimen preservation
and digitization, such as incomplete edges due to white strips, low
image contrast, and noises from fragile, overlapping, and damaged
organs.

**Step 1: Image loading**

Click the \'Folders\' button and choose the folder containing your image
files. All file names with extensions \'.jpg\', \'.png\', \'.tif\', and
\'.bmp\' will be listed. Choose the desired image file to load it into
the program (Fig. 2). Use the \'Next\' and \'Previous\' buttons to
navigate through the loaded images.

The test images can be found in the \'ElliShape\' folder you downloaded.

![](media/image4.png){width="5.768055555555556in"
height="3.170138888888889in"}

Figure . Image loading.

**Step 2.1: Object selection**

Users can zoom in and out using the mouse scroll wheel and navigate left
and right by dragging the slider to quickly locate the object (Fig. 3).
Object selection is facilitated through two methods: automated
segmentation and manual polygon selection.

![](media/image8.png){width="5.768055555555556in"
height="3.1791666666666667in"}

Figure 3. Object selection.

**Method 1: Object selection via "automated segmentation"**

After drawing a rectangular box around the object in the left window,
click the \'automated segmentation\' button. The segmented object will
appear in the lower middle and right windows as a binary image (Fig.4),
enabling direct chain code generation.

![](media/image9.png){width="2.774021216097988in"
height="1.5304483814523184in"}
![](media/image10.png){width="2.785386045494313in"
height="1.5338735783027122in"}

Figure 4. Object selection via "automated segmentation".

**Method 2: Object selection via "Polygon Tool"**

To select a region of interest (ROI), use the \'Polygon Tool\' button.
Left-click to create a polygon around the leaf, connecting points.
Right-clicking to close the polygon and display the selected object in
the upper middle picture window (Fig. 5). To begin a new selection,
right-clicking to end the current one.

![](media/image13.png){width="5.768055555555556in"
height="3.1777777777777776in"}

Figure 5. Object selection via "Polygon Tool".

**Step 2.2: Color inverting**

If the foreground objects exhibit high grayscale values and distinct
contrast with the background, the \'Inverted Colors\' function is
necessary. However, if they do not, it should be utilized.

An illustration of an image featuring a black background is shown in
Fig. 6.

![](media/image14.png){width="2.796467629046369in"
height="1.5359361329833772in"}
![](media/image15.png){width="2.8103969816272967in"
height="1.5490004374453192in"}

Figure 6. Color inverting.

**Step 2.2: Image enhancement and grayscale conversion**

If the foreground objects lack noticeable contrast with the background,
use this step, as shown in Fig. 7.

Note: Clicking the \'Image Enhancement\' button multiple times will
superimpose the enhanced effect. To revert to the original grayscale
image, click the \'Grayscale Conversion\' button.

![](media/image17.png){width="2.8453674540682417in"
height="1.5675907699037621in"}
![](media/image19.png){width="2.7822298775153107in"
height="1.5321347331583552in"}

\(2\) the image after using function

\(1\) the original image

Figure 7. Image enhancement.

**Step 3: Chain code generation**

Two methods are available for obtaining the object contour: \'Image
Binarization\' or \'Edge Detection\', selectable via radio buttons (Fig.
8). \'Image Binarization\' is the default method for contour extraction.

![](media/image19.png){width="5.768055555555556in"
height="3.176388888888889in"}

Figure 8. Two methods for obtaining the object contour.

**Method 1: Contour extraction via "Image binarization"**

Click the \'Binarization\' button to convert the processed grayscale
image into a binary image. The result will be displayed in the window
below the middle section and in the enlarged view window on the right
(Fig. 9).

To reduce noise in images with short chain code lengths (e.g. "the
length is 2") , click the \' Erosion \' button (Fig. 10). Adjust the
value in the box next to this button to control the size of the
corrosion operation for desired results.

If the prompt indicates \'chain code is not close\' and there are small
gaps or holes in the target region hindering closed curve formation,
click the \'Dilation\' button to close the boundary (Fig. 11).

If the prompt indicates \'chain code is not close\' and the editing
window shows that a single pixel point causing interruption in the
connecting line at the edge top, clicking the \'Corrosion\' button or
\'Dilation\' button will close the boundary (Fig. 12). If your target
object is broken, use the \'Editing\' function in the right window. Zoom
in using the mouse scroll wheel and pan the image, and draw white line
to connect the broken parts by long-pressing the left mouse and dragging
(Fig. 13). You can also use the left mouse button to draw a black line
to break the connection, where the color of the line is the opposite of
the background value. Right-click to pop up the \"Reset\" button to
reset and undo all edits.

Notes:

\(1\) The more dilations performed, the greater the distortion of the
object, so use an appropriate number.

\(2\) Zoom in until one pixel is clearly visible before editing the
image to avoid positional deviations (Fig. 13).

\(3\) Decide whether to use corrosion, dilation, and editing functions
based on the specific circumstances.

![](media/image22.png){width="5.768055555555556in"
height="3.1743055555555557in"}

Figure 9. Binarization results.

![](media/image24.png){width="2.9691797900262467in"
height="1.634012467191601in"}
![](media/image26.png){width="3.0050240594925635in"
height="1.653740157480315in"}

Figure 10 Erosion operation. When the prompt words indicate the short
length of chain code (e.g. "the length is 2"), click the \' Erosion \'
button and obtain the corrected boundary.

![](media/image29.png){width="2.897668416447944in"
height="1.5946587926509186in"}
![](media/image31.png){width="2.950521653543307in"
height="1.6237456255468066in"}

Figure 11. Dilation operation. When the prompt indicates \'chain code is
not close\' and there are small gaps or holes in the target region
hindering closed curve formation, click the \'Dilation\' button to close
the boundary.

![](media/image33.png){width="2.9377055993000876in"
height="1.6135094050743657in"}
![](media/image35.png){width="2.925518372703412in"
height="1.60998687664042in"}

Figure 12. Dilation operation. When prompted that the \'chain code is
not closed\' and the editing window shows a single pixel point
interrupting the connecting line at the top edge, clicking \'Dilation\'
button will close the gap in the boundary.
![](media/image37.png){width="5.768055555555556in"
height="3.1791666666666667in"}

Figure 13. Editing operation. When target object is broken, draw white
line to connect the broken parts by long-pressing the left mouse and
dragging.

Click the \'Chain Code\' button to initiate chain code extraction, with
a message box confirming its success (Fig. 14). The correctness and
closure of the chain code are determined by its length and the presence
of a red line in the middle right window. If the chain code is not
closed, the break location is enlarged in the editing window for user
edits, followed by clicking the \'Chain Code\' button again until the
result is correct.

![](media/image39.png){width="5.768055555555556in"
height="3.1791666666666667in"}

Figure 14. Successful chain code extraction.

**Method 2: Contour extraction via "Edge detection"**

Various edge detection methods, including Canny, Sobel, Prewitt, and
Roberts operators, as well as the log and zero-cross detectors, are
available in the popup menu (Fig. 15). Select the desired method adjust
the threshold using the slider. A lower threshold reveals more details,
while a higher threshold detects fewer details. Optimal thresholding is
achieved when clear edge contours are visible (Fig. 16).

In the editing window, users can connect disjointed contours and correct
any contour errors (Fig. 17). Click the \'Chain Code\' button to obtain
the correct edge contour (green line) and chain code (red line) as shown
in Fig. 18.

![](media/image41.png){width="5.768055555555556in"
height="3.297222222222222in"}

Figure 15. Edge detection method selection.

![](media/image43.png){width="5.768055555555556in"
height="3.176388888888889in"}

Figure 16. Threshold adjustment.

![](media/image45.png){width="5.768055555555556in"
height="3.1791666666666667in"}

Figure 17. Contour connection.

![](media/image47.png){width="5.768055555555556in"
height="3.1777777777777776in"}

Figure 18. Successful chain code extraction.

**Step** **4: Size calculation and saving**

If a ruler is present, zoom in on the image in the left window to the
ruler's location. Click the 'Click Two Points' button and select a
starting point and an endpoint by left-clicking. The coordinates of the
two points will be get. Enter the actual distance between the points in
the right text box, for example, input '10' (Fig. 19). Choose the
measurement units as 'mm' or 'inch'. If a ruler is absent, click the
'Skip' button. Provide a label for the object, then click the 'Save
(Chain code, Labeled images, and size)' button to save the outputs with
names appended with the user-defined tag. The files will be saved in the
'results' and 'label' directory located within the current program\'s
runtime path. These outputs include:

Boundary coordinates: input file name_user-defined tag_b.txt

Chain code: input file name_user-defined tag_c.txt

Size: input file name_user-defined tag_info.xlsx, Sheet 1

Labeled images: input file name_user-defined tag.png

![](media/image49.png){width="5.768055555555556in"
height="3.176388888888889in"}

Figure 19. Size calculation.

**Step 5:** **Ellipse Fourier Analysis page**

Click the \'Elliptic Fourier Analysis\' button to access a new page for
obtaining normalized EFD data and visualizing reconstructed shapes (Fig.
20).

Use the \'Calculate and Save\' button to save the EFD data. Users can
input any integer as the number of harmonic coefficients, with the
default value set at 35 (Fig.21).

Adjust the visualization number of the EFD, ensuring it is less than or
equal to the maximum, by clicking the \'Plot Curve\' button. The result
is displayed in Fig. 22. Click the \'Save Curve\' button to choose the
path for saving the curve (Fig. 23).

<figure>
<img src="media/image50.png" style="width:5.76806in;height:2.93194in" />
<figcaption><p>Figure 20. EFA interface.</p></figcaption>
</figure>

<figure>
<img src="media/image51.png" style="width:5.76806in;height:2.93194in" />
<figcaption><p>Figure 21. EFD calculation.</p></figcaption>
</figure>

<figure>
<img src="media/image52.png" style="width:5.76806in;height:2.93194in" />
<figcaption><p>Figure 22. Curve reconstruction.</p></figcaption>
</figure>

<figure>
<img src="media/image53.png" style="width:5.76806in;height:3.15833in" />
<figcaption><p>Figure 23. Curve saving.</p></figcaption>
</figure>

**Reference:**

Kuhl, F. P. , & Giardina, C. R. . (1982). Elliptic fourier features of a
closed contour. Computer Graphics & Image Processing, 18(3):236-258.
https://doi.org/10.1016/0146-664X(82)90034-X.

Haines, A. J., & Crampton, J. S. (2000). Improvements to the method of
Fourier shape analysis as applied in morphometric studies.
Palaeontology, 43(4):765-783. <https://doi.org/10.1111/1475-4983.00148>.

Bonhomme, V., Picq, S., Gaucherel, C. and Claude, J. (2014). Momocs:
Outline Analysis Using R. Journal of Statistical Software, 56(13):1--24.
https://doi.org/10.18637/jss.v056.i13.

Wishkerman, A., & Hamilton, P. B. (2018). Shape outline extraction
software (DiaOutline) for elliptic Fourier analysis application in
morphometric studies. Applications in Plant Sciences, 6(12): e01204.
https:// doi.org/10.1002/aps3.1204

Wu, H.,  Yang, J. J.,  Li, C. Q.,  Ran, J. H.,  Peng, R. H., &
Wang, X. Q. (2024). Reliable and superior elliptic fourier descriptor
normalization and its application software ellishape with efficient 
image processing.







