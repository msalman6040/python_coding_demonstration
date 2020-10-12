train_mass = 22680
train_acceleration = 10
train_distance = 100

device_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp -32)*5/9

def c_to_f(c_temp):
  f_temp = c_temp *(9/5) + 32

f100_in_celcius = f_to_c(100)

c0_in_farenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3*10**8):
  return mass*(c**2)

device_energy = get_energy(device_mass)

print("A 1kg bomb supplies " + str(device_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force*distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
