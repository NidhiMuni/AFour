from rest_framework import serializers
from .models import Employee, Quarterly, QuarterlyReview

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'manager_id', 'manager_name', 'du_head_id', 'du_head_name', 'date_of_joining', 'email', 'designation', 'service_status', 'project_id', 'project_name', 'project_start_date', 'project_end_date', 'coe_id', 'coe')

class QuarterlyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyReview
        fields = (
            'id',
            'qms_id', 
            'employee_id', 
            'manager_id', 
            'manager_name', 
            'du_head_id', 
            'du_head_name',
            'coe_head_id',
            'coe_head_name',
            'employee_service_status',
            'manager_hard_skills_comments',
            'manager_soft_skills_comments',
            'manager_value_addition_comments',
            'manager_up_learning_comments',
            'manager_hard_skills_ratings',
            'manager_soft_skills_ratings',
            'manager_value_addition_ratings',
            'manager_up_learning_ratings',
            'goal',
            'create_date',
            'hr_form_submit_date',
            'review_complete_date',
            'last_modified_date',
            'quarterly_rating',
            'manager_form_submit_date', 
            'workflow_status', 
            'last_modified_by', 
            'du_head_complete_date', 
            'du_hard_skills_ratings', 
            'du_soft_skills_ratings', 
            'du_value_addition_ratings', 
            'du_up_learning_ratings', 
            'du_hard_skills_comments', 
            'du_soft_skills_comments', 
            'du_value_addition_comments', 
            'du_up_learning_comments', 
            'save_for_later', 
            'first_name', 
            'last_name', 
            'manager_email', 
            'du_head_email', 
            'employee_email', 
            'designation'
            )