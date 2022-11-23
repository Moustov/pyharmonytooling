
# Commits
Run at least the unit tests under before committing
* test/0_mocked_tests
* test/1_objects_tests
* test/2_file_system_based_tests

Comply at much as possible with PEP8

# Unit Tests
- Create as much UT as possible :)
- When a bug is found, cover it with a UT
- Add the UT is the appropriate test category
  * _**test/0_mocked_tests**_: UT that would isolate the behavior with mocks/stubs
  * _**test/1_objects_tests**_: UT that would rely on objects in memory (no persistent data)
  * _**test/2_file_system_based_tests**_: UT that would rely on data stored on the file system
  * _**test/3_online_tests**_: UT that would rely on online servers (eg. google.com, ultimate-guitar.com)
