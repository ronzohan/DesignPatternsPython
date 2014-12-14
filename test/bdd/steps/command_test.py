from lettuce import step, world
from Command.receiver import LsReceiver, RmReceiver, TouchReceiver
from Command.command import LsCommand, RmCommand, TouchCommand
from Command.invoker import Invoker
from contextlib import contextmanager
from StringIO import StringIO
import sys
from nose.tools import assert_equal


@contextmanager
def captured_output():
    """
    Used for capturing print outputs
    """
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


@step(u'Given I have ls command and reciever')
def given_i_have_ls_command_and_reciever(step):
    world.ls_receiver = LsReceiver()
    world.ls_command = LsCommand(world.ls_receiver)


@step(u'And I have reciever and command for rm and touch with name "([^"]*)"')
def and_i_have_reciever_and_command_for_rm_and_touch_with_name_group1(step,
                                                                      name):
    world.rm_receiver = RmReceiver(name)
    world.rm_command = RmCommand(world.rm_receiver)
    world.touch_receiver = TouchReceiver(name)
    world.touch_command = TouchCommand(world.touch_receiver)


@step(u'When I have create and delete file commands')
def when_i_have_create_and_delete_file_commands(step):

    world.create_file_commands = [world.ls_command, world.touch_command,
                                  world.ls_command]

    world.delete_file_commands = [world.ls_command, world.rm_command,
                                  world.ls_command]


@step(u'Then I will call invoker class and call create_file')
def then_i_will_call_invoker_class_and_call_create_file(step):
    world.invoker = Invoker(world.create_file_commands,
                            world.delete_file_commands)
    # Capture all print outputs from the function call
    with captured_output() as (out, err):  # @UnusedVariable
        world.invoker.create_file()

    output = out.getvalue().strip() + '\n'
    message = ''
    for row in step.hashes:
        message += str(row['message']) + '\n'

    assert_equal(output, message)


@step(u'And then call delete_file from invoker class')
def and_then_call_delete_file_from_invoker_class(step):
    with captured_output() as (out, err):  # @UnusedVariable
        world.invoker.delete_file()

    output = out.getvalue().strip() + '\n'
    message = ''
    for row in step.hashes:
        message += str(row['message']) + '\n'

    assert_equal(output, message)


@step(u'And then call undo_all from invoker class')
def and_then_call_undo_all_from_invoker_class(step):
    with captured_output() as (out, err):  # @UnusedVariable
        world.invoker.undo_all()

    output = out.getvalue().strip() + '\n'
    message = ''
    for row in step.hashes:
        message += str(row['message']) + '\n'

    assert_equal(output, message)
