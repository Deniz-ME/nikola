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
Commit link can be found [here ](https://github.com/Deniz-ME/nikola/pull/2/commits/fe7127e1fa04377f9d699d8288f0ab29e0a62fd1)

I added a dictionary that has all the branches found in the method. When a branch is reached, the dictionary updates the specific branch. You can call a print coverage to see whether these branches are hit (covered).
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed.png)
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed2.png)


Function name: _execute(self, options={}, args=None) found in the class CommandVersion(Command) in nikola\plugins\command\version.py
Commit link can be found [here](https://github.com/Deniz-ME/nikola/pull/2/commits/dd3b3e69e499bd81a0898f6737f145134508e1cc)

The same method of instrumentation used in function 1 is applied here. This method required injecting a new branch to overwrite a specific value in the method, this is required to reach the branch of an outdated version. This branch is only reached by the test’s unique flag, this means that the functionality is left unaffected.

![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed3.png)
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed4.png)


<Group member name>
Darian Samsoedien

<Function 1 name>
human_time(self, dt) in the CommandStatus class

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/getnikola/nikola/commit/b16a7a8dcbdf59978db7d1f6a4fa6c4c490485c5

<Provide a screenshot of the coverage results output by the instrumentation>
Before I added a test there was no test for this function. As can be seen when running this line (this is when I run all the tests without the test I added) :
(for some the image via markdown doesn't work and the link has to be clicked for example this one:)
![image](https://github.com/Deniz-ME/nikola/assets/122440225/8247db58-fae6-4313-9f04-f5a7b0db9ad1)

	We see in this screenshot that lines 170 to 183 were missed
![image](https://github.com/Deniz-ME/nikola/assets/122440225/0b2d42a6-0dba-4a50-8db4-afb09805b2c7)
We can see in this screenshot that these are all the lines of the human_time function 	so we can conclude that this function isn’t being tested yet
![image](https://github.com/Deniz-ME/nikola/assets/122440225/b2d094db-21a3-406a-b37a-45f6a87f6e4e)
To still show the instrumentation with our report_coverage function we just need to call the function manually ourselves and it should show that no branch is being hit as of right now (because it didn’t get tested).
doing this we get this as expected: 
![image](https://github.com/Deniz-ME/nikola/assets/122440225/c03f3993-1f0f-4b69-a52e-b44fa2fd2771)


none of the branches have been covered yet.

<Function 2 name>
configure_logging(logging_mode: LoggingMode = LoggingMode.NORMAL) -> None 
in the log.py file

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>
https://github.com/Deniz-ME/nikola/commit/5643b3b52568dd57d126e30572c9ebd0bde12227
<Provide a screenshot of the coverage results output by the instrumentation>
![image](https://github.com/Deniz-ME/nikola/blob/Derra_Branch/logo/ass1_pic_1.png)
When we check the function without our newly made test function we see this: 
we see this: 
![image](https://github.com/Deniz-ME/nikola/assets/122440225/ba7792e8-0be8-4995-a5a8-a4df723e446a)

We also notice a total file coverage of 78 %
![image](https://github.com/Deniz-ME/nikola/assets/122440225/b70e656b-e9cc-44ed-a9fc-bcdf820699c7)

When we check this with the lines in the function we see that branch1, branch 3, and branch 4 are not being covered 
![image](https://github.com/Deniz-ME/nikola/assets/122440225/cdac9c6a-eee7-4f46-aba2-ffa5eb89cae5)

When we check  this with our function we see that this is true and only branch 2 gets hit before our tests this equals a branch coverage of 25%






Group member name: Deniz Erdoğan

Function 1 name: Gen_tasks(self), The path to the file where the function is -> “nikola.plugins.task.sources”. In the Sources class.

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements : https://github.com/getnikola/nikola/commit/92d2980b8a555220a787ea1a4e0c241a89f7ad1a

(Github only shows the changes of the last commit(unfortunately), you can see the whole code if you click the expand up button or expand down you are able to see the whole code)

Provide a screenshot of the coverage results output by the instrumentation
![image](https://github.com/Deniz-ME/nikola/assets/122368681/4ee5f69f-93f3-4df8-89e2-11d2cf40248e)


As you can see, branches 1,4,5 are hit without any test code written by me. 5 is hit multiple times because this one is in a for loop. Command that is used to get this is pytest -s
 
Function 2 name: Gen_tasks(self). The path to the file where the function is -> “nikola.plugins.task.pages”. In the RenderPages class.

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>       
https://github.com/getnikola/nikola/commit/31542c31f410f4e5ca74f88314b31670a17c7885

(Github only shows the changes of the last commit(unfortunately), you can see the whole code if you click the expand up button or expand down you are able to see the whole code)

Provide a screenshot of the coverage results output by the instrumentation: ![image](https://github.com/Deniz-ME/nikola/assets/122368681/0686104c-0ebb-4220-9259-bcd1425a826a)


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

![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed5.png)
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed6.png)

New coverage results:

![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed7.png)
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed8.png)


In the old coverage, only the first branch is hit during runtime, the other branches are not reached. The coverage of the file log.py is around 71%. 
After updating the tests, the branches are reached by getting calls with different parameters. The test prints out statements to see whether the visual functionality of the method work properly. You can also see that all branches of the method are now covered. This is further confirmed by the coverage report showing an increase of coverage in the file log.py reaching 84% cover.

Test: test_plugins.py

Link to commit

Old coverage results:

![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed9.png)
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed10.png)

New coverage results:

![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed11.png)
![image](https://github.com/Deniz-ME/nikola/blob/AzizBranch/logo/unnamed12.png)


In the old coverage, none of the branches are reached in the original test, this makes sense as the current tests do not use the flag ‘check’ for version number. This can also be seen before the branch printing, where Nikola v8.3.1 is printed but not checked for new versions. 
We added a new test which does so and also passes the new flag ‘old’ to force reach the branch for outdated versions. 
After updating the tests, we have fully covered the file version.py (thus the method too). The print statements before the branch coverage prints further confirm that the branches are hit.

<Darian Samsoedien>

<test_human.py>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/Deniz-ME/nikola/commit/73318f4da289602722b5a2f30f45aee8e53c42cc
	The test can be found in the test_human.py file
<Provide a screenshot of the old coverage results (the same as you already showed above)>
![image](https://github.com/Deniz-ME/nikola/assets/122440225/55e6c63c-c933-4ca3-b022-6e27882228ae)
![image](https://github.com/Deniz-ME/nikola/assets/122440225/67e7e8be-c328-4142-9ab1-44f4d3355dbf)


(for an explanation read the text above)

<Provide a screenshot of the new coverage results>
(for some the image via markdown doesn't work and the link has to be clicked for example this one:)
![image](https://github.com/Deniz-ME/nikola/assets/122440225/de8ee700-c638-4ddc-a41d-a8028378b03d)



we see that now all the branches are covered and with the print statements that all the results are true and the function does what it is supposed to (when you enter in 0 seconds the function should return False)


<State the coverage improvement with a number and elaborate on why the coverage is improved>
we went from a branch coverage of 0 % to a branch coverage of 100% as now all the branches have been covered
(for some the image via markdown doesn't work and the link has to be clicked for example this one:)
![image](https://github.com/Deniz-ME/nikola/assets/122440225/d19de05a-be21-4492-b3e0-039b618a1bbb)

We also see now that the total coverage of the file is 41% (which first was 20%) so there has been a total 21% increase in the total file coverage.

<Test 2>
<test_configure_logs.py>
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/Deniz-ME/nikola/commit/9a58ee2fc61f17f48e8706e67f905aa59e2ca2f3
The test can be found in the test_configure_logs.py file
<Provide a screenshot of the old coverage results (the same as you already showed above)>
![image](https://github.com/Deniz-ME/nikola/assets/122440225/4186ec80-b92b-4e3a-9cee-b8b21e16b661)
![image](https://github.com/Deniz-ME/nikola/assets/122440225/2ada5424-24b9-45f4-bf0a-5e9550af6833)

(For an explanation read the text for function 2)





	<Provide a screenshot of the new coverage results>
when we run the function with our function we see that all the branches get hit
![image](https://github.com/Deniz-ME/nikola/assets/122440225/7f36e9ec-4eb5-4b1d-bec6-339e96a85b4a)
![image](https://github.com/Deniz-ME/nikola/assets/122440225/de436fd6-af27-4b05-a7a5-903a468637b9)

	



<State the coverage improvement with a number and elaborate on why the coverage is improved>
The branch coverage went from 25 % to 100 % as all the branches are now hit.
We also see that the total coverage file went from 78% to 82% so that got improved because more lines are covered now.




<Group member name:> Deniz Erdoğan

<Test 1:> test_sources.py
    
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/getnikola/nikola/commit/985a833c0093bd0a299459ff446e842718e35383 

(Github only shows the changes of the last commit(unfortunately), you can see the whole code if you click the expand up button or expand down you are able to see the whole code)

<Provide a screenshot of the old coverage results (the same as you already showed above)>
![image](https://github.com/Deniz-ME/nikola/assets/122368681/4ee5f69f-93f3-4df8-89e2-11d2cf40248e)

Provide a screenshot of the new coverage results
![image](https://github.com/Deniz-ME/nikola/assets/122368681/0c551157-2fea-4fad-83ef-35ba0851e1a5)


I have now run the test file I have made, it covers branch 1, 2 and 3. This means that the not covered 2 and 3 from before are covered too!

![image](https://github.com/Deniz-ME/nikola/assets/122368681/a99a19b7-005b-4e1d-9b1e-6a312ddf5314)

This(^) is without the new test file which covers branch 2 and 3. Branch 2 and 3 are 66-68 and 70-72.(The other lines are functions for coverage check)
If you look at the improved coverage:
![image](https://github.com/Deniz-ME/nikola/assets/122368681/d5736aa2-8690-422f-848a-87688f7ecff9)

It says 100%, all the branches are covered.


<State the coverage improvement with a number and elaborate on why the coverage is improved

The coverage improvement went up by 40%, so it is now 100%. Every branch is covered in the function. I have made a mock post so that it imitates being a post with certain aspects which then will satisfy the if branches which needed to be covered.


<Function 2 name>
<test_pages.py>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>
https://github.com/getnikola/nikola/commit/7a0da9628a16637d9e30233b6b3443ac0d9c571d 

(Github only shows the changes of the last commit(unfortunately), you can see the whole code if you click the expand up button or expand down you are able to see the whole code)

<Provide a screenshot of the old coverage results (the same as you already showed above)>
![image](https://github.com/Deniz-ME/nikola/assets/122368681/a1f6b429-16f2-4227-bbbb-021156242564)


<Provide a screenshot of the new coverage results
![image](https://github.com/Deniz-ME/nikola/assets/122368681/8ded10e8-9c25-429a-8ca5-2947f67cfa0a)


I have now run the test file I have made, it covers branch 1, 2 and 3. This means that the not covered 2 is covered too now!

![image](https://github.com/Deniz-ME/nikola/assets/122368681/93db1131-af34-45ac-a12a-7eb79544b484)

This(^) is without the new test file which covers branch 2. Branch 2 is 72-73.(The other lines are functions for coverage check)

If you look at the improved coverage:

![image](https://github.com/Deniz-ME/nikola/assets/122368681/02cdf715-1ad3-4d91-9935-efc7e3552d0f)

It says 95%,it covers almost all the branches except one.

<State the coverage improvement with a number and elaborate on why the coverage is improved

The coverage improvement went up by 20%, so it is now 80%. Every branch except the last is covered in the function. I have made a mock post so that it imitates being a post with certain aspects which then will satisfy the if branch which I was able to cover.





ILyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas








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


