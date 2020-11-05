from flask_restful import Resource, reqparse
from com_sba_api.cop.cpp.model.cabbage_service import CabbageService
from com_sba_api.cop.cpp.model.cabbage_dto import CabbageVo
parser = reqparse.RequestParser()

class CabbagePricePrediction(Resource):
        
    @staticmethod
    def post():
        parser.add_argument('avg_temp', type=str, required=True,
                                        help='This field should be a userId')
        parser.add_argument('min_temp', type=str, required=True,
                                                help='This field should be a password')
        parser.add_argument('max_temp', type=str, required=True,
                                                help='This field should be a password')                                        
        parser.add_argument('rain_fall', type=str, required=True,
                                                help='This field should be a password')
        service = CabbageService()
        args = parser.parse_args()
        cabbage = CabbageVo()
        cabbage.avg_temp = args.avg_temp
        cabbage.max_temp = args.max_temp
        cabbage.min_temp = args.min_temp
        cabbage.rain_fall = args.rain_fall
        service.assign(cabbage)
        price = service.predict()
        print(f'Predicted Cabbage Price is {price} won')
        return {'price': str(price)}, 200 