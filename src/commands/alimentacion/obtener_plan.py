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

        logger.info("Plan alimentacion encontrado")
        resp = []

        pa: PlanAlimenticio
        for pa in plan_alimenticio:
            tmp = {
                'tipo_plan_alimenticio_id': pa.tipo_plan_alimenticio.id,
                'tipo_plan_alimenticio_nombre': pa.tipo_plan_alimenticio.nombre,
                'menu_id': pa.menu.id,
                'menu_nombre': pa.menu.nombre,
                'menu_descripcion': pa.menu.descripcion,
                'menu_calorias': pa.menu.calorias,
                'menu_porcion': pa.menu.porcion,
                'menu_medida': pa.menu.medida,
            }
            resp.append(tmp)

        return resp
