# TS 4G Server™
TS 4G documentation

## Client Commands

Every client command will be sent as a json in a dict:
`{"request_type": command, "argument1": argument1, "argument2": argument2, etc...}`
1. [Host](#host)
2. [Target](#target)
3. [Miscellaneous](#miscellaneous)
-  ### Host

&emsp;&emsp; • <u id="block_input_command">**[block_input](#block_input_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦ Blocks a targets keyboard and mouse.

&emsp;&emsp;&emsp;&emsp;◦ **Errors**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ user_already_affected: You are trying to block a targets input when it's already blocked.

&emsp;&emsp;&emsp;&emsp;◦ **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;◦ **Callback**: blocked_input.

<br/>

&emsp;&emsp; • <u id="unblock_input_command">**[unblock_input](#unblock_input_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦  Unblock a targets keyboard and mouse.

&emsp;&emsp;&emsp;&emsp;◦  **Errors**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ user_not_affected: You are trying to unblock a targets input when it's not blocked.

&emsp;&emsp;&emsp;&emsp;◦  **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;◦  **Callback**: unblocked_input.

<br/>

&emsp;&emsp; • <u id="block_screen_command">**[block_screen](#block_screen_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦  Block a targets screen. This will also block their mouse and keyboard.

&emsp;&emsp;&emsp;&emsp;◦  **Errors**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ user_already_affected: You are trying to block a targets screen when it's already blocked.

&emsp;&emsp;&emsp;&emsp;◦  **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;◦  **Callback**: blocked_screen.

<br/>

&emsp;&emsp; • <u id="unblock_screen_command">**[unblock_screen](#unblock_screen_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦   Unblock a targets screen.

&emsp;&emsp;&emsp;&emsp;◦  **Errors**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ user_not_affected: You are trying to unblock a targets screen when it's not blocked.

&emsp;&emsp;&emsp;&emsp;◦  **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;◦  **Callback**: unblocked_screen.

<br/>

&emsp;&emsp; • <u id="block_url_command">**[block_url](#block_url_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦  Block a website for a target. 

&emsp;&emsp;&emsp;&emsp;◦  **Errors**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ user_already_affected: You are trying to block a website that is already blocked.

&emsp;&emsp;&emsp;&emsp;◦  **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ url - str: the url of the website you are want to block.

&emsp;&emsp;&emsp;&emsp;◦  **Callback**: blocked_url.

<br/>

&emsp;&emsp; • <u id="unblock_url_command">**[unblock_url](#unblock_url_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦  Unblock a website for a target.

&emsp;&emsp;&emsp;&emsp;◦  **Errors**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ user_not_affected: You are trying to unblock a website that is not blocked.

&emsp;&emsp;&emsp;&emsp;◦  **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ url - str: the url of the website you want to unblock.

&emsp;&emsp;&emsp;&emsp;◦  **Callback**: unblocked_url.

<br/>

&emsp;&emsp; • <u id="start_screenshare_command">**[start_screenshare](#start_screenshare_action)**</u>

&emsp;&emsp;&emsp;&emsp;◦  Start a screenshare. To use this command, open a new connection to the server and login with the [screenshare role](#roles).

&emsp;&emsp;&emsp;&emsp;◦  **Arguments**:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;▫ [target_id](#target_id) - int: the ID of the target.

&emsp;&emsp;&emsp;&emsp;◦  **Callback**: awaiting_screenshare_client.

- ### Target

	-  <u id="init_target_screenshare_command">**init_target_screenshare**</u>
		- Init a screenshare after the client received the start_screenshare client. To use this command, open a new connection to the server.
		- **Arguments**:
			- target_id - int: the target ID received from the start_screenshare action.
			- screenshare_id - int: the screenshare ID received from the start_screenshare action.
		- **Callback** screenshare_started.

- ### Miscellaneous

	-  <u>**login**</u>
		- Log in to a role
		- **Errors**:
			- invalid_role: the role you are trying to log into doesn't exist.
			- invalid_password: the password doesn't match the role password.
		- **Arguments**:
			- [role](#roles) - int: the id of the role.
			- pc_name - str: the name of your computer.
			- password - str, not required: the password of the role, if applicable.
		- **Callback**: logged_in.  Will also send the user_logged_in callback with the user information to everyone.

## Server Actions

Every server will be sent  as a json in a dict:
`{"request_type": "action", "type": action type, "argument1": argument1, "argument2": argument2, etc...}`
These actions will be send to the target when a command is executed

- <u id="block_input_action">**[block_input](#block_input_command)**</u>
- <u id="unblock_input_action">**[unblock_input](#unblock_input_command)**</u>

<br/>

- <u id="block_screen_action">**[block_screen](#block_screen_command)**</u>
- <u id="unblock_screen_action">**[unblock_screen](#unblock_screen_command)**</u>

<br/>

- <u id="block_url_action">**[block_url](#block_url_command)**</u>
- <u id="block_url_action">**[unblock_url](#unblock_url_command)**</u>
<br/>

- <u id="start_screenshare_action">**[start_screenshare](#start_screenshare_command)**</u>
	- **Arguments**:
		-  target_id - int: the ID of the target that the host wants to screenshare
		- screenshare_id: the ID of the screenshare.

## Screenshare
When you want to start a screenshare, you start a new connection, login as a screenshare and send the [start_screenshare](#start_screenshare_command) command. This command will send the target the [start_screenshare](#start_screenshare_action) action.

When the target receives this action, they will start a new connection and send the [init_target_screenshare](#init_target_screenshare_command) command, and start sending image data to the server, which will forward it to the host screenshare connection.

The image data is a pickled CV2 image. The first 8 bits of the data is the length of the image data.
## Roles
**0** - target

**1** - host, password is required

**2** - screenshare, password is required