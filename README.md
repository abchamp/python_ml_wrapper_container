### python_ml_wrapper_container

- input tabular and image (mainly)
- base on single model
- run on docker continer
- Direct with HTTPS (FastAPI)
- can edit multiple model config (can programmable)
- PUB/SUB (rabbitMQ, kafka)
- Support queue (....think about tech) to model
- No SECURITY !! (For now)

Question:

- What is the limitation ?

<code>
uvicorn main:app --reload

</code>

### checklist

[ ] enviroment setup

### Resource

- https://www.rabbitmq.com/tutorials/tutorial-one-php.html
- https://www.fullstackpython.com/task-queues.html
- https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
- https://cloud.google.com/ai-platform/prediction/docs/exporting-for-prediction

### note package

- django-celery-beat => periodic task schedule in the database
