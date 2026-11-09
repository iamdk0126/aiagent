from typing import List, Dict, Optional

class WorkflowRuntime:
    """
    WorkflowRuntime: 管理工作流任务的类
    """

    def __init__(self):
        """
        初始化 WorkflowRuntime 类
        """
        self.tasks = {}

    def register_task(self, task_id: str, task_function):
        """
        注册任务

        :param task_id: 任务ID
        :param task_function: 任务函数
        """
        self.tasks[task_id] = task_function

    def execute_task(self, task_id: str, *args, **kwargs):
        """
        执行任务

        :param task_id: 任务ID
        :param args: 任务参数
        :param kwargs: 任务关键字参数
        :return: 任务执行结果
        """
        if task_id in self.tasks:
            return self.tasks[task_id](*args, **kwargs)
        else:
            raise ValueError(f"Task {task_id} not found")

    def get_task_status(self, task_id: str) -> Optional[str]:
        """
        查询任务状态

        :param task_id: 任务ID
        :return: 任务状态
        """
        if task_id in self.tasks:
            return "Running"
        else:
            return None
