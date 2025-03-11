# ALX System Engineering & DevOps - Processes and Signals

This repository contains solutions to tasks related to processes and signals in
Bash scripting. Below is a summary of the completed tasks:

## Tasks

### 0. What is my PID

**Script:** `0-what-is-my-pid`
**Description:** Displays the PID of the current Bash script.
**Example Output:**
```bash
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
```
**Script:** `2-show_your_bash_pid`
**Description:**  Displays lines containing the word bash, allowing you to
easily get the PID of your Bash process.
**Example output**
```
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00 \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00 \_ bash./2-sho.
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00  \_ grep bash
```