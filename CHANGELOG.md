# Change Log

## [1.0.0] - 06-10-2020

- Initial release

## [1.1.0] - 06-10-2020

### Added

 - Added ability to pause and resume the timer, by hitting Ctrl+C and resuming
   with enter.

## [1.2.0] - 07-10-2020

### Changed

 - Reworked to wait using select(), which allows us to read stdin for different
   keypresses. See README.md for the usage.
