CONTRIBUTING GUIDELINE
========================

# Commits
Run at least the unit tests under before committing
* test/0_mocked_tests
* test/1_objects_tests
* test/2_file_system_based_tests

## Unit Tests
- Create as much UT as possible :)
- When a bug is found, cover it with a UT
- Add the UT is the appropriate test category
  * _**test/0_mocked_tests**_: UT that would isolate the behavior with mocks/stubs
  * _**test/1_objects_tests**_: UT that would rely on objects in memory (no persistent data)
  * _**test/2_file_system_based_tests**_: UT that would rely on data stored on the file system
  * _**test/3_online_tests**_: UT that would rely on online servers (eg. google.com, ultimate-guitar.com)

## Code Quality
Comply at much as possible with PEP8
IDE such as Pycharm provide a code inspection to perform a [5S](https://www.agilitest.com/cards/5s-on-code)

# Todos
The code embeds "_todo_" tags to improve features.
Tickets in Github are also an option - this is still in building mode

You are encouraged to contribute...

# Building a package
    
    python.exe setup.py bdist_wheel
