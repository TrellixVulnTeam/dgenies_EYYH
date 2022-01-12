# Changelog

## 1.2.1 (2022-01-??)

### Major changes

- Backup archive is now a `tar.gz` file. Old `tar` backup archive are still supported
- Speedup compressed file operations by using [`xopen` library](https://github.com/pycompression/xopen)
- Upgrade embedded minimap2 to the latest available version (2.23)

### Other changes

- Fix upload form. Form is now correctly reset when a field is missing or erroneous.
- Fix filename collision. Uploading a query file and a target file with the same filename now works correctly
- Correct default `slurm` parameters to match last version of [slurm-drmaa](https://github.com/natefoo/slurm-drmaa) (1.1.3)
- Update documentation:
  - Explain how similarity/identity measure is computed
  - Describe what is expected in backup archive
  - Update deployment instruction for webserver and cluster mode
  - Additional information for developers

## 1.2.0.2 (2021-11-15) - pypi release only

### Bugfixes

- Update python requirements

## 1.2.0.1 (2018-09-25) - pypi release only

Bugfix release

## 1.2.0 (2018-07-17)

### Major changes

- Dot plot have now a mouse cursor centered zoom
- Now includes [mashmap](https://github.com/marbl/MashMap) (v2.0), a faster aligner for high identity genomes, as an alternative to minimap2 (Linux only)
- Download a HTML page which permit to show an interactive dot plot offline (with the summary)
- Display match coordinates by moving the mouse cursor over the match line

### Other changes

- Upgrade embedded minimap2 to the latest available version (2.11)
- Add help messages on the interface
- Add the ability to add a message to the run form through command line (designed for maintenance for example)
- Several bug fixes


## 1.1.1 (2018-06-20)

### Bugfixes

- Fix bug with parse of MAF files
- Fix incompatibility with pip >= 10.0


## 1.1.0 (2018-04-17)

### Major changes

- Improve run form: add support for uploading an alignment file (PAF or MAF by default) instead of fasta files, if alignment file is already available
- Add export of a job into a backup, which can be re-uploaded with the run form
- Ease the integration of new tools or new file formats
- Allow to install as simple user on Unix systems

### Other changes

- Export of the dot plot is now done including the zoom factor
- Add new color palettes for dot plot
- Add analytics logs (anonymous) which permits to know which size of genomes are ploted (can be disabled)
- Improve documentation
- Minor bug fixes


## 1.0.1 (2018-02-23)

Bug fix release.

### Changes

- Fix bugs
- Disable export of fasta files for gallery items


## 1.0.0 (2018-02-21)

First stable release