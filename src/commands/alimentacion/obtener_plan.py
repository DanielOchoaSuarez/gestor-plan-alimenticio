import logging

from src.commands.base_command import BaseCommand
from src.errors.errors import BadRequest
from src.models.plan_alimenticio import PlanAlimenticio, PlanAlimenticioSchema
from src.utils.str_utils import str_none_or_empty


logger = logging.getLogger(__name__)


class ObtenerPlan(BaseCommand):
    def __init__(self, **info):
        logger.info(
            'Validando informacion para obtener plan de alimentacion')

        if str_none_or_empty(info.get('id_plan')):
            logger.error("ID Plan Obligatorio")
            raise BadRequest

        self.id_plan = info.get('id_plan')

    def execute(self):
        logger.info("Buscando plan de alimentacion" + self.id_plan)
        plan_alimenticio = PlanAlimenticio.query.filter_by(
            id_plan=self.id_plan).all()

        if plan_alimenticio is None or len(plan_alimenticio) == 0:
            logger.error("Plan de alimentacion no encontrado")
            return []
        else:
            logger.info("Plan alimentacion encontrado")
            schema = PlanAlimenticioSchema(many=True)
            return schema.dump(plan_alimenticio)
