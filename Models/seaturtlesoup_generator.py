from typing import Literal

from pydantic import BaseModel, Field

class InputModel(BaseModel):
    word: str = Field(
        alias='word',
        description='바다거북스프를 생성합니다. 원하는 주제어를 입력해주세요.',
        default='사자',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='바다거북스프 결과물',
    )
