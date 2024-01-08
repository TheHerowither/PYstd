################################################################################
# Python Standard library
#   A basic set of functions, i use a lot of times
#   This includes logging functionalities, and ansi colors
#
# MIT License
# 
# Copyright (c) 2024 TheHerowither
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

# non-constants
__stdout__ = __import__("sys").stdout
__stderr__ = __import__("sys").stderr

log_output = __stdout__
log_errout = __stderr__

exit_on_error = True

# SGR color constants
# rene-d 2018
class Color:
    """ ANSI color codes """
    BLACK        = "\033[0;30m"
    RED          = "\033[0;31m"
    GREEN        = "\033[0;32m"
    BROWN        = "\033[0;33m"
    BLUE         = "\033[0;34m"
    PURPLE       = "\033[0;35m"
    CYAN         = "\033[0;36m"
    LIGHT_GRAY   = "\033[0;37m"
    DARK_GRAY    = "\033[1;30m"
    LIGHT_RED    = "\033[1;31m"
    LIGHT_GREEN  = "\033[1;32m"
    YELLOW       = "\033[1;33m"
    LIGHT_BLUE   = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN   = "\033[1;36m"
    LIGHT_WHITE  = "\033[1;37m"
    BOLD         = "\033[1m"
    FAINT        = "\033[2m"
    ITALIC       = "\033[3m"
    UNDERLINE    = "\033[4m"
    BLINK        = "\033[5m"
    NEGATIVE     = "\033[7m"
    CROSSED      = "\033[9m"
    RESET        = "\033[0m"
    # cancel SGR codes if we don't write to a terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""

class CommandOutput:
    output = ""
    error = ""
    code = 0
    def __str__(self) -> str:
        return f"{self.__class__}\n\tReturn code -> {self.code}\n\tError output -> {repr(self.error)}\n\tOutput -> {repr(self.output)}"

# Utility functions
def exit(code : int):
    __import__("sys").exit(code)

# Logging functions
def trace(*msg : str):
    log_output.write(Color.LIGHT_GRAY+"[TRACE]:"+Color.RESET+" "+" ".join(msg)+"\n")
    log_output.flush()
def info(*msg : str):
    log_output.write(Color.GREEN+"[INFO]:"+Color.RESET+" "+" ".join(msg)+"\n")
    log_output.flush()
def warn(*msg : str):
    log_output.write(Color.YELLOW+"[WARN]:"+Color.RESET+" "+" ".join(msg)+"\n")
    log_output.flush()
def error(*msg : str, code : int = 1):
    global exit_on_error
    log_errout.write(Color.RED+"[ERROR]:"+Color.RESET+" "+" ".join(msg)+"\n")
    log_errout.flush()
    if exit_on_error: exit(code)

def yes_no_request(*msg: str) -> int:
    answer = input(f"[REQUEST]: {' '.join(msg)} (y/n) ")
    if answer.strip() == "y": return 1
    return 0

def command(cmd : str) -> CommandOutput:
    log_output.write("[CMD]: "+cmd+"\n")
    log_output.flush()
    out = CommandOutput()
    command = __import__("subprocess").run(cmd, shell = True, capture_output = True)
    out.code   = command.returncode
    out.error  = command.stderr.decode()
    out.output = command.stdout.decode()
    return out

# Testing
if __name__ == "__main__":
    if yes_no_request("Hi, are you yes?"):
        print(command("echo Hello World!"))
    else:
        print(command("echo You are no"))

    trace("Trace")
    info("Info")
    warn("Warning")
    error("Error")
