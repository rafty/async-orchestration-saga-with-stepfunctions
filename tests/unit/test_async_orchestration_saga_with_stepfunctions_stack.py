import aws_cdk as core
import aws_cdk.assertions as assertions

from async_orchestration_saga_with_stepfunctions.async_orchestration_saga_with_stepfunctions_stack import AsyncOrchestrationSagaWithStepfunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in async_orchestration_saga_with_stepfunctions/async_orchestration_saga_with_stepfunctions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AsyncOrchestrationSagaWithStepfunctionsStack(app, "async-orchestration-saga-with-stepfunctions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
