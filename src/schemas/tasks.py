from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    title: str
    author_id: int
    assignee_id: int

    class Config:
        from_attributes = True


class TaskSchemasAction(BaseModel):
    title: str
    author_id: int
    assignee_id: int



