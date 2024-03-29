from typing import Dict, List

from app.pipelines import Pipeline


class TextToTextPipeline(Pipeline):
    def __init__(self, model_id: str):
        # IMPLEMENT_THIS
        # Preload all the elements you are going to need at inference.
        # For instance your model, processors, tokenizer that might be needed.
        # This function is only called once, so do all the heavy processing I/O here
        raise NotImplementedError(
            "Please implement TextToTextPipeline __init__ function"
        )

    def __call__(self, inputs: str) -> List[Dict[str, str]]:
        """
        Args:
            inputs (:obj:`str`):
                The input text
        Return:
            A :obj:`list`:. The list contains a single item that is a dict {"text": the model output}
        """
        # IMPLEMENT_THIS
        raise NotImplementedError(
            "Please implement TextToTextPipeline __call__ function"
        )
