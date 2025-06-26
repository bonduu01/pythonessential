"""The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter
 version information."""

from platform import platform, machine, processor, system, version

print(platform())
print(platform(False, False))


# Print Machine Name
print("Machine:", machine())

# Print Processor
print("Processor:", processor())

# Print System
print("System:", system())

# Print Version
print("Version:", version())
