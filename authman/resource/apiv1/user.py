from flask_restfulimport Resource

class UserResource(Resource):
	def get(self, user_id=None):
		if user_id is None:
			return { "user":"singleton"}
		return {"users":"collection"}
