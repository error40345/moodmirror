import os
from typing import Optional
from roma_dspy.core.engine.solve import RecursiveSolver
from roma_dspy.config.schemas.root import ROMAConfig
from roma_dspy.config.schemas.agents import AgentsConfig, AgentConfig
from roma_dspy.config.schemas.base import LLMConfig, RuntimeConfig
from roma_dspy.config.schemas.resilience import ResilienceConfig


class RomaExecutor:
    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment")
        
        import dspy
        
        lm = dspy.LM(
            model="openrouter/anthropic/claude-3.5-sonnet",
            api_key=api_key,
            api_base="https://openrouter.ai/api/v1",
            temperature=0.7,
            max_tokens=2000
        )
        
        dspy.configure(lm=lm)
        
        llm_dict = {
            "model": "openrouter/anthropic/claude-3.5-sonnet",
            "temperature": 0.7,
            "max_tokens": 2000,
            "api_key": api_key,
            "base_url": "https://openrouter.ai/api/v1"
        }
        
        config_dict = {
            "agents": {
                "atomizer": {"llm": llm_dict},
                "planner": {"llm": llm_dict},
                "executor": {"llm": llm_dict},
                "aggregator": {"llm": llm_dict}
            },
            "runtime": {"max_depth": 3}
        }
        
        config = ROMAConfig(**config_dict)
        
        self.solver = RecursiveSolver(config=config, enable_logging=False, enable_checkpoints=False)
        print("✓ ROMA Framework initialized from https://github.com/sentient-agi/ROMA")
    
    def is_complex_task(self, text: str) -> bool:
        complex_indicators = [
            "plan", "strategy", "step by step", "analyze", 
            "compare", "research", "calculate", "solve",
            "break down", "detailed", "comprehensive", "multi-step"
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in complex_indicators)
    
    def execute(self, task: str, mood: Optional[str] = None) -> str:
        try:
            context = f"User emotional state: {mood}\n" if mood else ""
            context += f"Task: {task}\n\n"
            context += "Provide a thoughtful, empathetic response that addresses the task while being emotionally supportive."
            
            result_node = self.solver.solve(context)
            
            return result_node.result if result_node and result_node.result else str(result_node)
            
        except Exception as e:
            error_msg = f"ROMA execution error: {str(e)}"
            print(error_msg)
            raise


def create_roma_executor() -> Optional[RomaExecutor]:
    try:
        return RomaExecutor()
    except ValueError as e:
        print(f"OpenRouter API key not found - ROMA features disabled: {e}")
        return None
    except Exception as e:
        print(f"Failed to initialize ROMA: {e}")
        return None
