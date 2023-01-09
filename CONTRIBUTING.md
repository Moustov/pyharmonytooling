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
  * _**test/4_load_tests**_: UT that would require a *long time* to have some feedback on load/robustness/...

How to launch unit tests

     .\venv39\Scripts\python.exe -m pytest test


> NOTE:
>
> Ensure the assert is done this way:
>
>      self.ut_report.assertTrue(res == expected)
> and the test class initializes `self.ut_report``:
> 
>      ut_report = UnitTestReport()
This will include the *assert* in the [test report](unit_test_report.md) with a link to the failing assert in the code

To prevent UT exits from exception, you must frame your test code with try/exception:

        try:
            res = GuitarTab.digest_tab_simplest_splitted_chords_in_a_bar(tab)
            self.ut_report.assertTrue(len(res.keys()) == len(expected.keys()))
            self.ut_report.assertTrue(CofChord.are_chord_equals(res["2"],  expected["2"]))
        except:
            self.ut_report.assertTrue(False)


## Code Quality
Comply at much as possible with PEP8
IDE such as Pycharm provide a code inspection to perform a [5S](https://www.agilitest.com/cards/5s-on-code)

# Todos
The code embeds "_todo_" tags to improve features.
Tickets in Github are also an option - this is still in building mode

You are encouraged to contribute...

# Building a package
    
    .\venv\Scripts\python.exe setup.py bdist_wheel

Then apply https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/

To deploy the package on Pypi.org

    .\venv\Scripts\python.exe -m twine upload .\dist\pyHarmonyTooling<version>.whl