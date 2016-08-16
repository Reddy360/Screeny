# Screeny
A ShareX commandline uploader

# Command line arguments
screeny.py [-h] [--config CONFIG] [-clipboard] [-browser] file
* h (optional) - DIsplays the help screen ^ that thing up there
* config (optional) - Specify location of ShareX config, defaults to ~/.screeny.json
* clipboard (optional) - Copy the URL to your clipboard after upload
* browser (optional) - Open the URL in your default browsers after upload
* file (required) positional argument with a path to the file to upload

# Config support
* RequestURL
* FileFormName
* Arguments
* RegexList (ish)
* URL

# Config tests
* shite.xyz (private, no regex just key) - PASS
* animegirlsare.sexy (public, http://shite.xyz/bOpOR9.json) - PASS
* jii.moe (public (found on Twitter), https://jii.moe/EyT9W9c_.json) - FAIL (Implementation issue)
* hnng.moe (public, http://www.hnng.moe/api) - FAIL (Implementation issue)

# Implement in your own project
Alongside Screeny being a commandline tool it can also be imported as a module
```python
import Screeny from screeny

configLocation = "test.json"
screeny = Screeny(configLocation)

# String upload
returnedData = screeny.uploadString("foo")
print(screeny.handleRegex(returnedData)) # URL to resource

# File upload
returnedData = screeny.uploadFile("bar.png")
print(screeny.handleRegex(returnedData)) # URL to resource
```
