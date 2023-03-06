# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):
    var_greet = greeting.replace("<name>", name)
    return var_greet
    #print(var_greet)

def force(mass, body= "earth"):
    celestial_body = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }

    if body in celestial_body.keys():
       gravity = celestial_body[body]
       force_calc = mass * gravity
       return round(force_calc,2)
       #print(round(force_calc,2))

    else: print("Body not found")
    return

def pull(m1, m2, d):
    g = 6.674*(10**-11)
    f = g*((m1*m2)/(d**2))
    #print(round(f, 6))
    return f


print(greet("Sam"))
print(greet("Sam", "What's up, <name>!"))
print(force(0.1, ))
print(pull(0.1, 5972*(10**24), 6371*(10**6)))

