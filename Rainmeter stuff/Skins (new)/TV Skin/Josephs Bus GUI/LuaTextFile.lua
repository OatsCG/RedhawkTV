function Initialize()

	sFileToRead = SELF:GetOption('FileToRead')
	
end

function Update()

	hReadingFile = io.open(sFileToRead)
	if not hReadingFile then
		print('LuaTextFile: unable to open file at ' .. sFileToRead)
		return
	end
	
	sAllText = hReadingFile:read("*all")
	if sAllText ~= "" then
		new_word = ''
		sAllText = string.gsub(sAllText, "\t", "     ")
		for word in sAllText:gmatch("'(.-)'")do
			if word == "Not Scheduled" then
				new_word = word
			elseif word ~= "" then
				new_word = new_word .. word
			else
			end
			
		end
	old_word = new_word
	return tostring(old_word)
	
	else
	end
	old_word = new_word
	io.close(hReadingFile)
	return tostring(old_word)
	
	
end
