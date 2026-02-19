import os
import sys
import time
from dotenv import load_dotenv

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

# Orchestration
from orchestration.supervisor import Supervisor
from orchestration.scheduler import Scheduler

# Agents ✅ FIXED
from agents.monitor_agent.monitor import MonitorAgent
from agents.predictor_agent.predictor import PredictorAgent
from agents.planner_agent.planner import PlannerAgent
from agents.executor_agent.executor import ExecutorAgent
from agents.learning_agent.learning import LearningAgent
from agents.cost_agent.cost import CostAgent

# Shared
from shared.logger import get_logger

logger = get_logger("finops-main")


def create_agents():
    """
    Initialize all FinOps agents
    """

    logger.info("Initializing FinOps agents...")

    monitor = MonitorAgent()

    predictor = PredictorAgent()

    planner = PlannerAgent()

    executor = ExecutorAgent()

    learner = LearningAgent()

    cost = CostAgent()

    return {
        "monitor": monitor,
        "predictor": predictor,
        "planner": planner,
        "executor": executor,
        "learner": learner,
        "cost": cost
    }


def main():

    logger.info("Starting Autonomous FinOps Agent")

    # Create all agents
    agents = create_agents()

    # Create supervisor
    supervisor = Supervisor(
        monitor=agents["monitor"],
        predictor=agents["predictor"],
        planner=agents["planner"],
        executor=agents["executor"],
        learner=agents["learner"],
        cost=agents["cost"]
    )

    # Create scheduler
    scheduler = Scheduler(supervisor)

    # Start autonomous loop
    logger.info("Starting scheduler loop...")
    scheduler.start()

    # Keep process alive
    while True:
        time.sleep(60)


if __name__ == "__main__":
    main()