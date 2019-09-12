#你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表


from operator import itemgetter     #支持原生比较的字典
from operator import attrgetter    #不支持原生比较操作的类

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


# 在上面例子中， rows 被传递给接受一个关键字参数的 sorted() 内置函数。 这个参数是 callable 类型，
# 并且从 rows 中接受一个单一元素，然后返回被用来排序的值。
# itemgetter() 函数就是负责创建这个 callable 对象的。
rows.sort(key=itemgetter('fname'))
print(rows)
rows_by_fname = sorted(rows,key=itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_uid)
rows_by_fname_lname = sorted(rows,key=itemgetter('lname','fname'))
print(rows_by_fname_lname)

rows_by_fname_key = sorted(rows,key=lambda r:r['fname'])
print(rows_by_fname_key)

# 不要忘了这节中展示的技术也同样适用于 min() 和 max() 等函数
min_rows_in_uid = min(rows,key=itemgetter('uid'))
print(min_rows_in_uid)


#######不支持原生比较的类
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(12),User(124),User(42)]
    print(users)
    # users.sort(key=lambda u: u.user_id)
    # print(users)    #使用sort直接改变user序列
    print(sorted(users,key=lambda u:u.user_id))    #效果和attrgeter一致
    print(users)     #sorted不会改变原有序列
    print(sorted(users,key=attrgetter('user_id')))    #效果比lambda好
    print(max(users,key=attrgetter('user_id')))

sort_notcompare()