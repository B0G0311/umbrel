#!/usr/bin/env python3
import sys
import subprocess

#umbrel
def install_umbrel():
    subprocess.run(["./install"])

def configure_umbrel():
    subprocess.run(["./configure"])

def start_umbrel():
    subprocess.run(["./start"])

def stop_umbrel():
    subprocess.run(["./stop"])

def debug_umbrel():
    subprocess.run(["../debug"])

def backup_umbrel():
    subprocess.run(["./backup/backup"])

def app_command(action, app_name):
    subprocess.run(["./app", action, app_name])

def repo_command(action, repo):
    subprocess.run(["./repo", action, repo])

#umbrel-os
def change_password():
    subprocess.run("./umbrel-os/change-password")

def umbrel_details():
    subprocess.run("./umbrel-os/umbrel-details")

#print cli command options
def show_usage():
    print('''
        CLI (v${VERSION}) for managing Umbrel

        Usage: app <command> <app> [<arguments>]

        Commands:
          install               Installs Umbrel
          configure             Updates the Umbrel configuration
          start                 Starts your Umbrel
          stop                  Stops your Umbrel
          debug                 Creates debug output for Umbrel
          backup                Creates baackup for Lighting wallet
          app                   Manage Umbrel apps
          repo                  Manage Umbrel repos

        Umbrel-OS compatible:
          change-password       Change Umbrel password
          details               Prints the details of your Umbrel
    ''')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == "install":
        install_umbrel()
    elif command == "configure":
        configure_umbrel()
    elif command == "start":
        start_umbrel()
    elif command == "stop":
        stop_umbrel()
    elif command == "debug":
        debug_umbrel()
    elif command == "backup":
        backup_umbrel()
    elif command == "app" and len(sys.argv) == 4:
        app_action = sys.argv[2]
        app_name = sys.argv[3]
        app_command(app_action, app_name)
    elif command == "repo" and len(sys.argv) == 4:
        repo_action = sys.argv[2]
        repo_name = sys.argv[3]
        repo_command(repo_action, repo_name)
    elif command == "change-password":
        change_password()
    elif command == "details":
        umbrel_details()
    else:
        show_usage()
        sys.exit(1)

    sys.exit(0)
