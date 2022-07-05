import check_limits
assert(check_limits.battery_is_ok("Temperature", 25, 0, 45) is True)
assert(check_limits.battery_is_ok("Temperature", 85, 0, 45) is False)
assert(check_limits.battery_is_ok("State of Charge", 70, 20, 80) is True)
assert(check_limits.battery_is_ok("State of Charge", 10, 20, 80) is False)
assert(check_limits.battery_is_ok("Charge Rate", 0.7, 0.8, 1) is False)
assert(check_limits.battery_is_ok("Charge Rate", 0.9, 0.8, 1) is True)
