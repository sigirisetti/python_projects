from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333))

stack = gateway.entry_point.getStack()
print(stack)

stack.push("First %s" % ('item'))
stack.push("Second item")
print(stack.pop())
print(stack.pop())
#print(stack.pop())


stack.push('First item')
internal_list = stack.getInternalList()
print(len(internal_list))

print(internal_list[0])

internal_list.append('Second item')
print(stack.getInternalList())
