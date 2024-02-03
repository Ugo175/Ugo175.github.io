
class Solution:
    def reorderLogFiles(self, logs):
        is_letter_log = lambda log: log[log.find(' ') + 1].isalpha()
        get_content = lambda log: log[log.find(' ') + 1: ]
        get_identifier = lambda log: log[:log.find(' ')]
        letter_logs = []
        digit_logs = []
        for log in logs:
            letter_logs.append(log) if is_letter_log(log) else digit_logs.append(log)
        letter_logs.sort(key=get_content)
        for i in range(1, len(letter_logs)):
            for j in range(i - 1, -1, -1):
                if get_content(letter_logs[i]) == get_content(letter_logs[j]):
                    if get_identifier(letter_logs[i]) < get_identifier(letter_logs[j]):
                        letter_logs.insert(j, letter_logs.pop(i))
                    else:
                        break
        return letter_logs + digit_logs

