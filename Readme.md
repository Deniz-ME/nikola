# Report for Assignment 1

## Project chosen

Name: Nikola

URL: https://github.com/Deniz-ME/nikola

Number of lines of code and the tool used to count it: 106 KLOC using Lizard

Programming language: Python

## Coverage measurement

### Existing tool

To measure the coverage, we made use of pytest and pytest-cov and other libraries for dependencies such as coverage and better visualization such as pytest-html.
To execute, we do pytest -s. We use -s to show the print statements as well.





### Your own coverage tool

Group member: Aziz
Function name: wrap_in_color(self, record: logging.LogRecord) -> str found in
the class ColorfulFormatter(logging.Formatter) in nikola\log.py
Commit link can be found here 

I added a dictionary that has all the branches found in the method. When a branch is reached, the dictionary updates the specific branch. You can call a print coverage to see whether these branches are hit (covered).




Function name: _execute(self, options={}, args=None) found in the class CommandVersion(Command) in nikola\plugins\command\version.py
Commit link can be found here

The same method of instrumentation used in function 1 is applied here. This method required injecting a new branch to overwrite a specific value in the method, this is required to reach the branch of an outdated version. This branch is only reached by the test’s unique flag, this means that the functionality is left unaffected.




<Group member name>
Darian Samsoedien

<Function 1 name>
human_time(self, dt) in the CommandStatus class

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/getnikola/nikola/commit/b16a7a8dcbdf59978db7d1f6a4fa6c4c490485c5

<Provide a screenshot of the coverage results output by the instrumentation>
Before I added a test there was no test for this function. As can be seen when running this line (this is when I run all the tests without the test I added) :

	We see in this screenshot that lines 170 to 183 were missed

We can see in this screenshot that these are all the lines of the human_time function 	so we can conclude that this function isn’t being tested yet

To still show the instrumentation with our report_coverage function we just need to call the function manually ourselves and it should show that no branch is being hit as of right now (because it didn’t get tested).
doing this we get this as expected: 



none of the branches have been covered yet.

<Function 2 name>
configure_logging(logging_mode: LoggingMode = LoggingMode.NORMAL) -> None 
in the log.py file

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/Deniz-ME/nikola/commit/5643b3b52568dd57d126e30572c9ebd0bde12227
<Provide a screenshot of the coverage results output by the instrumentation>

When we check the function without our newly made test function we see this: 
we see this: 
We also notice a total file coverage of 78 %

When we check this with the lines in the function we see that branch1, branch 3, and branch 4 are not being covered 
 
When we check  this with our function we see that this is true and only branch 2 gets hit before our tests this equals a branch coverage of 25%






Group member name: Deniz Erdoğan

Function 1 name: Gen_tasks(self), The path to the file where the function is -> “nikola.plugins.task.sources”. In the Sources class.

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements : https://github.com/getnikola/nikola/commit/92d2980b8a555220a787ea1a4e0c241a89f7ad1a

Provide a screenshot of the coverage results output by the instrumentation
![image](https://github.com/Deniz-ME/nikola/assets/122368681/4ee5f69f-93f3-4df8-89e2-11d2cf40248e)

As you can see, branches 1,4,5 are hit without any test code written by me. 5 is hit multiple times because this one is in a for loop. Command that is used to get this is pytest -s
 
Function 2 name: Gen_tasks(self). The path to the file where the function is -> “nikola.plugins.task.pages”. In the RenderPages class.

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>       
https://github.com/getnikola/nikola/commit/31542c31f410f4e5ca74f88314b31670a17c7885

Provide a screenshot of the coverage results output by the instrumentation: [SEP2.png](https://github.com/Deniz-ME/nikola/blob/DenizBranch/SEP2.png?raw=true) 

As you can see, branches 1,3, 4 are hit without any test code written by me. Command that is used to get this is pytest -s





Group member name: Ilyaas Wardere

Function 1 name: get_lang(self)

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements: https://github.com/Deniz-ME/nikola/commit/e5537fd73bfb17c3a914b7d633fe628f58834548

Provide a screenshot of the coverage results output by the instrumentation

	
<Function 2 name>
	filter_exif(self, exif, whitelist)
<Provide the same kind of information provided for Function 1>

https://github.com/Deniz-ME/nikola/commit/e1321a03fbce2444770d65cc31b3d0f09a9db4d9

.

## Coverage improvement

### Individual tests

Group member: Aziz

Test: test_custom.py

Link to commit

Old coverage results:



New coverage results:



In the old coverage, only the first branch is hit during runtime, the other branches are not reached. The coverage of the file log.py is around 71%. 
After updating the tests, the branches are reached by getting calls with different parameters. The test prints out statements to see whether the visual functionality of the method work properly. You can also see that all branches of the method are now covered. This is further confirmed by the coverage report showing an increase of coverage in the file log.py reaching 84% cover.

Test: test_plugins.py

Link to commit

Old coverage results:



New coverage results:



In the old coverage, none of the branches are reached in the original test, this makes sense as the current tests do not use the flag ‘check’ for version number. This can also be seen before the branch printing, where Nikola v8.3.1 is printed but not checked for new versions. 
We added a new test which does so and also passes the new flag ‘old’ to force reach the branch for outdated versions. 
After updating the tests, we have fully covered the file version.py (thus the method too). The print statements before the branch coverage prints further confirm that the branches are hit.

<Darian Samsoedien>

<test_human.py>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/Deniz-ME/nikola/commit/73318f4da289602722b5a2f30f45aee8e53c42cc
	The test can be found in the test_human.py file
<Provide a screenshot of the old coverage results (the same as you already showed above)>


(for an explanation read the text above)

<Provide a screenshot of the new coverage results>

we see that now all the branches are covered and with the print statements that all the results are true and the function does what it is supposed to (when you enter in 0 seconds the function should return False)


<State the coverage improvement with a number and elaborate on why the coverage is improved>
we went from a branch coverage of 0 % to a branch coverage of 100% as now all the branches have been covered

We also see now that the total coverage of the file is 41% (which first was 20%) so there has been a total 21% increase in the total file coverage.

<Test 2>
<test_configure_logs.py>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/Deniz-ME/nikola/commit/9a58ee2fc61f17f48e8706e67f905aa59e2ca2f3
The test can be found in the test_configure_logs.py file
<Provide a screenshot of the old coverage results (the same as you already showed above)>
(For an explanation read the text for function 2)





	<Provide a screenshot of the new coverage results>
when we run the function with our function we see that all the branches get hit
	



<State the coverage improvement with a number and elaborate on why the coverage is improved>
The branch coverage went from 25 % to 100 % as all the branches are now hit.
We also see that the total coverage file went from 78% to 82% so that got improved because more lines are covered now.

<Group member name>
Deniz Erdogan
<Test 1>
<test_sources.py>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/getnikola/nikola/commit/985a833c0093bd0a299459ff446e842718e35383 

<Provide a screenshot of the old coverage results (the same as you already showed above)>


<Provide a screenshot of the new coverage results>

-        I have now run the test file I have made, it covers branch 1, 2 and 3. This means that the not covered 2 and 3 from before are covered too!

This is without the new test file which covers branch 2 and 3. Branch 2 and 3 are 66-68 and 70-72.(The other lines are functions for coverage check)
If you look at the improved coverage:

It says 100%, all the branches are covered.
<State the coverage improvement with a number and elaborate on why the coverage is improved>
The coverage improvement went up by 40%, so it is now 100%. Every branch is covered in the function. I have made a mock post so that it imitates being a post with certain aspects which then will satisfy the if branches which needed to be covered.
<Function 2 name>
<test_pages.py>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/getnikola/nikola/commit/7a0da9628a16637d9e30233b6b3443ac0d9c571d 
<Provide a screenshot of the old coverage results (the same as you already showed above)>
 
<Provide a screenshot of the new coverage results>

-         I have now run the test file I have made, it covers branch 1, 2 and 3. This means that the not covered 2  is covered too!


This is without the new test file which covers branch 2. Branch 2 is 72-73.(The other lines are functions for coverage check)
If you look at the improved coverage:

It says 95%,it covers almost all the branches except one.
 <State the coverage improvement with a number and elaborate on why the coverage is improved> 
The coverage improvement went up by 20%, so it is now 80%. Every branch except the last is covered in the function. I have made a mock post so that it imitates being a post with certain aspects which then will satisfy the if branch which I was able to cover.

<Test 1>
test_utils.py:
test_not_self_translated()
test_get_lang_locale_borg()
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
	https://github.com/Deniz-ME/nikola/commit/6bc2853b91c2e1c705a6f3e075dbaffe2dcf3579

<Provide a screenshot of the old coverage results (the same as you already showed above)>


<Provide a screenshot of the new coverage results>



<State the coverage improvement with a number and elaborate on why the coverage is improved>
Since only one of the 5 branches was hit originally, the coverage was at 20%. After the changes we cover 4 of the 5 branches which makes the coverage 80%. The coverage was improved by adding 2 new test functions that enter the branches that weren’t hit. The first function enters the eilf branch by setting self.lang to false and make sure to not add a translation. This should return the default language which is english and we assert that. The second function enters the else branch and the try branch. We make sure the first two branches aren’t hit by setting our own language. The language is set to french and we ensure this happens correctly by checking if the language is indeed french.
<Test 2>
	test_archive_per_day.py:
	test_star_whitelist()
	test_no_dict_value()
	test_not_in_whitelist()
	test_in_whitelist()
	test_last_if()
<Provide the same kind of information provided for Test 1>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/Deniz-ME/nikola/commit/49872c74c88aa455d825bba39a9988ff2233aba4

https://github.com/Deniz-ME/nikola/commit/701c4c09f1aca62dbf6fbfa35a193203728e9033
(small name change)
<Provide a screenshot of the old coverage results (the same as you already showed above)>




<Provide a screenshot of the new coverage results>


<State the coverage improvement with a number and elaborate on why the coverage is improved>
Originally only one of the seven branches were hit. This makes the original coverage around 14%. After adding the new test functions, the branch coverage was increased to 100% since all branches get hit now. The new functions each handle different cases of the filter_exif function which is why the coverage was able to be improved. For example, the first new function sets {'*': '*'} as the whitelist's key and value. This makes the first branch get hit. Through similar means do we make sure all the other branches get hit as well. 

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>


<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

We got an improvement of 1% over the whole project

## Statement of individual contributions

<Write what each group member did>

We have chosen the project as a group effort with everybody contributing to finding the project, using the tools to measure the coverage and lines, and ensuring the project's requirements are met.
Then we divided the functions and each chose 2 functions to measure the coverage of,and improve the coverage via tests. The tests per person are mentioned above.


