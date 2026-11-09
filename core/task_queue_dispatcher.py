from typing import List, Dict, Optional, Any

class TaskStatus:
    """
    TaskStatus: 任务状态枚举
    """
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Task:
    """
    Task: 任务类
    """
    def __init__(self, task_id: str, task_function, *args, **kwargs):
        """
        初始化 Task 类

        :param task_id: 任务ID
        :param task_function: 任务函数
        :param args: 任务参数
        :param kwargs: 任务关键字参数
        """
        self.task_id = task_id
        self.task_function = task_function
        self.args = args
        self.kwargs = kwargs
        self.status = TaskStatus.PENDING

    def execute(self):
        """
        执行任务
        """
        try:
            self.task_function(*self.args, **self.kwargs)
            self.status = TaskStatus.COMPLETED
        except Exception as e:
            self.status = TaskStatus.FAILED

class TaskQueue:
    """
    TaskQueue: 任务队列类
    """
    def __init__(self):
        """
        初始化 TaskQueue 类
        """
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        添加任务

        :param task: 任务对象
        """
        self.tasks.append(task)

    def remove_task(self, task_id: str):
        """
        移除任务

        :param task_id: 任务ID
        """
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def process_tasks(self):
        """
        处理任务
        """
        for task in self.tasks:
            if task.status == TaskStatus.PENDING:
                task.execute()
                if task.status == TaskStatus.COMPLETED:
                    self.remove_task(task.task_id)

# 示例用法
def example_task():
    print("任务执行中...")

task_queue = TaskQueue()
task = Task("task1", example_task)
task_queue.add_task(task)
task_queue.process_tasks()
