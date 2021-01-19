
class ConditionFailedException(BaseException):
    def __init__(self, message):
        super(ConditionFailedException, self).__init__()
        self.message = message

    def __str__(self):
        return self.message


# def rollback_transaction(self):
#     self.cursor.execute('ROLLBACK')


def type_checker(self, target, expected_type, error_to_raise=TypeError, belong=True, message=''):
    if message == '':
        message = 'expected to have type %s, but found %s' % (expected_type, type(target))
    if belong:
        if target is not None and not isinstance(target, expected_type):
            raise error_to_raise(message)
    if not belong:
        if target is not None and isinstance(target, expected_type):
            raise error_to_raise(message)
        return
    return True


def condition_checker_v1(self, condition, expected=True):
    if expected:
        if condition:
            return True
    if not expected:
        if not condition:
            return True
    raise ConditionFailedException('the condition has not been satisfied')


def condition_checker(self, condition, expected=True, message='the condition has not been satisfied'):
    if condition is expected:
        return True
    raise ConditionFailedException(message)