if __name__ == '__main__':
    import re


    # 定义一个函数来分析日志文件
    def analyze_log(log_contents):
        # 定义错误模式
        error_pattern = re.compile(r"ERROR|Exception|Traceback|failure|error")

        # 初始化状态
        status = "SUCCESS"  # 假设训练成功完成

        # 搜索日志内容中的错误信息
        if error_pattern.search(log_contents):
            status = "FAILURE"  # 发现错误模式，设置状态为失败

        return status


    # 假设您已经有了日志内容，这里是一个例子
    log_contents = """
    [2024-03-12 14:41:30,298] torch.distributed.elastic.multiprocessing.api: [ERROR] failed (exitcode: 1) local_rank: 0 (pid: 494) of binary: /usr/bin/python
    torch.distributed.DistBackendError: NCCL error in: /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp
    """

    # 分析日志
    training_status = analyze_log(log_contents)

    # 打印状态或进行相应的操作
    print(f"Training status: {training_status}")
