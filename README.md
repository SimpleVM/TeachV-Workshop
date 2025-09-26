
# Teach V - SimpleVM Demonstration

## Example Workshop: Setting Up Reproducible Environments for Data Science Training

This example outlines the preparation and execution of a hands-on data science workshop using cloud-based virtual machines (VMs) to provide a consistent, ready-to-use computing environment for all participants. The focus is on reproducibility, convenience, and minimizing setup time for workshop attendees. The steps below use the Visual Studio Code’s Research Environment in SimpleVM as a base image and demonstrate how to pre-install required software and stage workshop data.

## Workshop Preparation

### Background

When organizing practical workshops, especially in computational fields, ensuring that all participants have access to the required tools and data can be a major challenge. Local environment discrepancies, missing software, and compatibility issues often lead to time-consuming troubleshooting. By preparing cloud-based VM templates in advance—with all software, scripts, and datasets pre-installed—organizers can provide each participant with an isolated, identical development environment launched with a single click.

While this repository describes all necessary steps for the conduction of the example use-case given, one can get more detailed instructions and technical informations in the [SimpleVM Wiki](https://simplevm.denbi.de/wiki)

### Step-by-Step Instruction

#### 1. Base Image Selection

Begin by selecting an appropriate base image for the workshop’s virtual machines.

- **Recommendation:** Use the `Visual Studio Code` Research Environment image, which comes with a pre-configured coding environment ideal for Python and data science tasks.
- **Purpose:** This choice ensures all participants have an integrated development environment (IDE) suitable for code editing, debugging, and visualization.

#### 2. Volume Attachment

Provision a persistent storage volume to the template VM.

- **Mount Point:** Attach the volume to the VM and mount it at `/vol/data`.
- **Purpose:** Using a separate volume allows easy sharing and cloning of workshop data for all participants.

#### 3. VM Startup and Access

Launch the virtual machine with the selected image and attached volume.

- **Access Methods:** Connect to the instance via SSH or use a browser-based session of the research environment. 
- **Purpose:** This initial session is for provisioning; workshop participants will receive cloned or templated environments later.

#### 4. Software Environment Setup

Install all software dependencies required for the workshop exercises. For example:

```bash
pip install pandas matplotlib
```

- **Explanation:** `pandas` is a library for data manipulation, and `matplotlib` is used for data visualization—both common in Python-based data analysis.
- **Tip:** Consider creating a `requirements.txt` file if multiple packages are needed, to allow batch installation.

#### 5. Workshop Script Preparation

Retrieve the scripts that will be used or modified during the workshop:

```bash
git clone https://github.com/SimpleVM/TeachV-Workshop.git
```


#### 6. Data Preparation

Download all required datasets into the attached data volume and adjust ownership with `chown` beforehand:

```bash
cd /vol/data
sudo chown -R ubuntu:ubuntu .
wget https://openstack.cebitec.uni-bielefeld.de:8080/workshopteach/world_population.csv
```

- **Purpose:** Placing the data on the mounted volume allows to create a clone of the data - a corresponding volume providing the data of the mounted volume can be attached to each participants machine. 

#### 7. Image and Volume Finalization

Once the setup is complete:

- **Shut down** the virtual machine.
- **Detach the volume** that stores the workshop data.
- **Create a snapshot** of the prepared VM. This snapshot captures the exact software state and tools required for the workshop.

### Running the Workshop

With the environment prepared and captured, proceed to define participant instances:

#### 1. Instance Launch for Participants

- **Create instances** for each workshop participant using the workshop instance creation interface.

- **Choose an appropriate flavor** (CPU/RAM configuration) to match the workshop’s workload.
- **Select the VM snapshot** created earlier to ensure each participant’s machine is identical to the template.

- **Attach the prepared data volume** in the volume selection, again using `/vol/data` as the mount path.

#### 2. User Assignment

- Select the participants who require access and assign them to the corresponding instances.

## Workshop Instructions

### Running and Using `graphs.py` to create Bar Charts of Population Changes

1. **Navigate to the Workshop Folder**

   Change into the cloned workshop repository:

   ```bash
   cd TeachV-Workshop
   ```

2. **Adjust the CSV Path**

   Open `graphs.py` in your preferred text editor and modify the line:

   ```python
   CSV_PATH = "ADJUST_PATH"
   ```

   so that it points to the location of the data file:

   ```python
   CSV_PATH = "/vol/data/world_population.csv"
   ```

3. **Run the Script**

   Execute the script using Python 3:

   ```bash
   python3 graphs.py
   ```

   This will read the population data, process it, and generate two bar plots:

   - `population_growth.png`: Top 5 countries by relative population growth (2020–2022)
   - `population_decline.png`: Top 5 countries by relative population decline (2020–2022)

4. **View the Results**

   After successful execution, you will find the two PNG images in your current directory. These visualizations display population changes and annotate each bar with population numbers for 2020 and 2022.

