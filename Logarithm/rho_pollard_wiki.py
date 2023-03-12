from base.find_cycle_floyd import floyd

def find_u_next(u_previous, z_previous, module):
	if 0 < z_previous < module / 3:
		return (u_previous + 1) % (module - 1)
	elif module / 3 < z_previous < 2 * module / 3:
		return 2 * u_previous % (module - 1)
	elif 2 * module / 3 < z_previous <  module:
		return u_previous % (module - 1)

def find_v_next(v_previous, z_previous, module):
	if 0 < z_previous < module / 3:
		return v_previous % (module - 1)
	elif module / 3 < z_previous < 2 * module / 3:
		return 2 * v_previous % (module - 1)
	elif 2 * module / 3 < z_previous < module:
		return (v_previous + 1) % (module - 1)

def find_z_next_slow(a, b, v_previous, u_previous, module):
	return ((b ** u_previous) * (a ** v_previous)) % module

def find_z_next(a, b, module, z_previous):
	if 0 < z_previous < module / 3:
		return (b * z_previous) % module
	elif module / 3 < z_previous < 2 * module / 3:
		return (z_previous ** 2) % module
	elif 2 * module / 3 < z_previous < module:
		return (a * z_previous) % module
# a^x = b mod p, find x
def ind_rho_pollard(a, b, p):
	u0 = v0 = 0
	z0 = 1
	print(floyd(find_z_next, z0))

ind_rho_pollard()