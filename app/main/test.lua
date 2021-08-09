local last_x, last_y, last_z, last_update = 0, need_update = false

function onScriptUpdate()
	local now_x, now_y, now_z = getPosition()
	if now_x ~= last_x or now_y ~= last_y or now_z ~= last_z then
		last_x = now_x
		last_y = now_y
		last_z = now_z
		last_update = os.time()
		need_update = true
	end
	if need_update and last_update + 300 <= os.time() then
		need_update = false
		-- любое действие которое тебе надо
		
	end
end