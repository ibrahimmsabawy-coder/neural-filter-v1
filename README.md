#Neural filter

##this is a neural filter project that simulates the behavior of the brain 's neural signals to process and filter information with the various limbs of the body. The project aims to create a system that can analyze and interpret sensory data,allowing for more accurate and efficient responses when using prosthetic limbs or other assistive devices. By leveraging digital signal processing (DSP), this project seeks to enhance the functionality and usability of these devices, ultimately improving the quality of life for individuals who rely on them.
## How It Works
*   **Step 1 The Clean Signal (`clean_signal`):** The first and foremost step in the coding was to make a `clean_signal`. This array is essentially the intent of the user to move the limb in a certain direction. It is a clean sine wave made by the `np.sin` function, representing the raw neural signal before it encounters biological noise and electrical interference in real life.
*   **Step 2 The Noise (`gaussian_noise`):** The next step is to add noise to the clean signal. This is done by generating Gaussian noise using the `np.random.normal` function. The noise is then added to the clean signal to simulate real-world conditions where neural signals are often contaminated by various sources of noise and artifacts. The resulting signal is saved as `messy_signal`, representing the chaotic raw data a prosthetic electrode would actually read, which will be used for further processing.
*   **Step 3 Filtering (`filtered_signal`):** The final step is to filter the `messy_signal` using digital signal processing. Specifically, the `for` loop in the code acts as a **moving average filter**. The goal of this step is to remove unwanted noise and artifacts from the signal, allowing for a cleaner representation of the user's intent to move the limb. The `filtered_signal` can then be used to control prosthetic limbs or other assistive devices more accurately and efficiently.


### The Math

The math behind this filter is actually pretty straightforward. To make the filter work, we use a `window_size` of 5. This is done to create a "window" of data points around every single point $i$ in our signal, looking 5 points backward and 5 points forward. 

Because the loop can run into errors at the very beginning or the very end of our data, we use the `max` and `min` functions. This is essentially done to keep the window boundaries safe so the code doesn't try to read data that doesn't exist.

Mathematically, we are calculating the average ($y[i]$) of all the points currently inside this sliding window:

$$y[i] = \frac{1}{N} \sum_{j = \text{start\_index}}^{\text{end\_index} - 1} x[j]$$

We do this using the `np.mean` function. This is the key to cleaning the signal: because Gaussian noise is completely random, it constantly fluctuates both above (positive) and below (negative) our true signal. When we take the average of these points, the random positive and negative spikes cancel each other out (averaging out to zero), leaving behind only the smooth, low-frequency movement of the user's actual intent.
