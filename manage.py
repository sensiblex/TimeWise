class ManageActivity:

    @staticmethod
    def rename(activity, new_name):
        activity.name = new_name

    @staticmethod
    def change_type(activity, new_type):
        activity.type_of_activity = new_type