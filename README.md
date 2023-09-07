**This tool can automatically add a breakpoint to the code where an error occur.** I have been using it for many years and find it very useful for code debug.

To use the tool, just import it at the begining of your code:
```python
import auto_breakpoint
```
Basically, I hook the default python excepthook to set up a `pdb` interactive environment when the code has an error. Then the code would pause at that error. For example, try the following code:
```python
import auto_breakpoint
a = 1
arr = []
arr[0] += 1
```
It will pause at the last line, then you can print any variables of interest that might lead to the error to debug like the following, instead of explicitly adding debug codes like `print(a)` and then re-run the code

![image](https://github.com/changmenseng/auto_breakpoint/assets/60961806/84ee54fa-27e9-4257-933e-dc0f385dbf35)

I recommend to copy this code to the path of a python interpreter, e.g., the `site-packages` directory. Then, you can use it in every path.
