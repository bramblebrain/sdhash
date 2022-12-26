# sdhash
![image](https://user-images.githubusercontent.com/121334679/209446169-9382c9c9-f2d8-4d86-8ac6-c07e63b13f0f.png)

Based off of Ehplodor's hash calcuation, sdhash allows you to quickly get a list of model hashes and then saves it to hashes.txt file. Duplicate hashes will have their own column. This does not work for Hypernetwork or Embeds as the part that gets hashed appears to be the same.

You can either pass the model names as arguments or drag and drop the models on to the .bat (Windows). 

Duplicate hashes will be in a new row after the original with a **+** after the hash indicating that it's the duplicate row


## Changelog
v1.02
- Now uses the entire file for hypernetworks and embeds in order to get a unique hash.
v1.01 
- Fixed batch allowing for the model to be in a different directory when drag and dropping.
v1.00 
- Initial release