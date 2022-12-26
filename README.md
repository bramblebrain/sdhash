# sdhash
![image](https://user-images.githubusercontent.com/121334679/209499154-650fc833-d6ac-4806-803b-6627982b493d.png)

Based off of Ehplodor's hash calcuation, sdhash allows you to quickly get a list of model hashes and then saves it to hashes.txt file. Duplicate hashes will have their own column. Also works with Embeds and Hypernetworks by hashing the entire file.

![image](https://user-images.githubusercontent.com/121334679/209499736-1688f8f7-93b0-4eee-af21-34ff49a51053.png)

You can either pass the model names as arguments or drag and drop the models on to the .bat (Windows). You can also create a button if your file manager supports it.

Duplicate hashes will be in a new row after the original with a **+** after the hash indicating that it's the duplicate row


## Changelog
#### v1.02
  - Now uses the entire file for hypernetworks and embeds in order to get a unique hash.
#### v1.01 
  - Fixed batch allowing for the model to be in a different directory when drag and dropping.
#### v1.00 
  - Initial release
