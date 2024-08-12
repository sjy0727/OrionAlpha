'''
使用三个单引号创建多行注释，如下所示。
这主要用于在所有脚本的开头放置我们的许可证。
下面是脚本顶部多行注释中始终放置的内容。
'''

'''
此文件是OrionAlpha的一部分，这是一个MapleStory模拟器项目。
版权所有 (C) 2018 Eric Smith <notericsoft@gmail.com>

本程序是自由软件：您可以根据GNU通用公共许可证的条款重新分发和/或修改
由自由软件基金会发布的许可证的第三版或（由您选择的）任何更高版本。

本程序的发布是希望它能有用，
但没有任何担保；甚至没有适销性或特定用途适用性的隐含担保。
有关详细信息，请参阅GNU通用公共许可证。

您应该已经收到一份随本程序一起分发的GNU通用公共许可证的副本。如果没有，请参阅 <http://www.gnu.org/licenses/>。
'''

'要创建单行注释，请使用单引号。'
'这是我们通常用于编写NPC和脚本描述的注释。'
'您还可以使用反斜杠在多行中使用单行注释。'

'NPC: 普通出租车'
'脚本: 在维多利亚岛的城镇之间传送用户。'

'''
以下是从JS转到Python需要了解的一些重要事项。

1) 请记住，Python将在全局范围内执行我们的所有脚本。
这意味着我们从未像在Odin的start()、action()等中调用函数。
相反，我们只是直接在脚本中逐行执行我们的代码。

2) Python声明变量的方式与JS不同。
这意味着我们从不声明未初始化的变量，使用var/let等，也不使用类型定义。
此外，您不能像在JS中那样从全局范围修改值。
如果您希望修改在全局范围内声明的变量，必须使用global关键字：

val = "a"

def foo():
    global val
    val = "b"

print(val)

上面的代码将把'val'从'a'修改为'b'。如果不使用global val，则不会对全局范围进行任何修改。

3) 在许多方面，Python中的操作符与JS有很大不同：
- 我们从不在语句末尾加上分号（;）像在JS中那样。
- 在条件中实际上不需要使用括号。
- 要定义代码块，我们不使用大括号（{），而是使用冒号（:）。
- 所有包含在块中的代码都缩进 - 如果缩进返回，则意味着块结束。格式化在Python中非常重要，必须始终正确缩进（或使用Python编辑器为您完成此操作）！
- 在处理条件语句时，没有'else if'，只有'if'，'elif'和'else'。请记住，每当使用条件语句时，必须始终将其定义为块（例如'else:'）
- 在Python中，布尔值有点不同。它们不是'true'/'false'，而是'True'/'False'。此外，没有像JS中的!操作符，因此只需执行val == False。
- 如果条件检查值是否>= x && <= y，可以使用'in'关键字。（例如'if val in (1, 5):'）
- For循环的声明方式与JS不同。如果您从i = 0，i < x循环，请使用'for i in range(0, x):'
- 要声明函数，我们不使用关键字'function'，而是用'def'定义。（例如'def foo():'）

4) 在字符串中添加对象的方式与JS不同。（例如"you have " + mesos + " mesos"）。
在Python中，必须通过执行'str(mesos)'将对象基本上'转换为字符串'。（例如"you have " + str(mesos) + " mesos"）
'''

'如您所见，我们仍然像在JS中那样声明和处理数组。'
towns = [["Lith Harbor", 104000000, 120], ["Henesys", 100000000, 100], ["Ellinia", 101000000, 100], ["Kerning City", 103000000, 80]]

'这是一个如何定义和使用带参数的函数的示例。'
'注意：必须始终首先声明函数。也就是说，在上面定义函数，然后在下面调用它。'
def goTown(mapName, mapNum, fee):
    '我们的脚本是无状态的 - 它们等待用户的异步响应后继续执行。'
    '在这种情况下，我们要求用户选择是或否，并将该响应分配给ret。'
    ret = self.askYesNo("你在这里没有其他事情要做了吗？你真的想去#b" + mapName + "#k吗？这将花费你#b" + str(fee) + " 金币#k。")
    '如果ret为1（是），则继续将用户传送到选定的城镇。'
    if ret == 1:
        if (self.userIncMoney(-fee, True)):
            self.registerTransferField(mapNum, "")
        else:
            self.say("恐怕你没有足够的钱，你得走路。")
    else:
        self.say("这个镇上有很多值得看的东西。当你想去其他地方时再回来。")

'这继续全局范围，并且是NPC开始执行的地方。'
self.sayNext("嗨，我是普通出租车。如果你想快速安全地去另一个城镇，你来对地方了。您的满意是有保证的。")
menu = "选择你的目的地，费用因地点而异。\r\n#b"
'我们从i=0到i=towns.length进行循环。在每个循环中，我们将城镇选择附加到菜单中。'
for i in range(0, len(towns)):
    menu += "#L" + str(i) + "#" + towns[i][0] + " (" + str(towns[i][2]) + " 金币)#l\r\n"
'就像我们在goTown中所做的一样，我们将菜单选择的响应分配给sel。'
sel = self.askMenu(menu)
'现在我们确保选择的响应有效，然后调用goTown移动用户。'
if sel in (0, len(towns)):
    '再次，访问数组参数与在JS中一样。'
    goTown(towns[sel][0], towns[sel][1], towns[sel][2])

'''
另一个显示在Odin中常见的区别的示例是，您不能同时发送多个"sendOk"（或任何sendXXX）。
如果这样做，会一次发送所有这些，并且会崩溃您的客户端。

在OrionAlpha中不是这样！由于它是逐行异步脚本执行，我们可以执行以下操作：

self.sayNext("嗨！")
self.sayNext("欢迎来到OrionAlpha！")
ret = self.askYesNo("你准备好开始你的旅程了吗？")
if ret == 1:
    self.registerTransferField(map, "")

每次调用都会等待响应。当用户点击'下一步'时，npc将执行第二个sayNext调用。当他们再次点击下一步时，npc将执行askYesNo调用。
最后，如果askYesNo调用的响应为'是'，则它将传送用户。就是这样！
'''

'最后但并非最不重要的是，我们的脚本从不需要调用dispose()。 :)'
