## Example Workshop

### Image and Volume Preparation

1. Choose the current Visual-Studio-Code Research Environment as the image for the Virtual Machine, which you will use for the creation oft the template.
2. Also add a volume to the instance. 1GB of space is sufficient, mount it to `/vol/data`.
3. Start the instance - as soon as it is available, connect to it via SSH or browser
4. Install the requirements, which are needed to perform the tasks in the workshop.
    ``` 
    pip install pandas matplotlib
    ```


5. Clone the scripts one will adjust and execute during the workshop.
    ```
    git clone git@github.com:SimpleVM/TeachV-Workshop.git
    ```

6. Download data needed for the workshop to the volume. We will later clone the volume.

    ```
    cd /vol/data
    wget https://openstack.cebitec.uni-bielefeld.de:8080/workshopteach/world_population.csv
    ```
7. Stop the virtual machine, detach the volume and create a snapshot of the virtual machine.

### Workshop Conduction

1. Start the instances for the participants
   1. Select a suitable flavor and the snapshot you have created as the image for the instance
   2. Select the volume, you have put the data on and again set `/vol/data` as the mountpath.
   3. Select the participants you want to start a machine with this parameters for
   4. Click on start


