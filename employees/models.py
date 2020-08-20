# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    manager_id = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    du_head_id = models.CharField(max_length=200)
    du_head_name = models.CharField(max_length=200)
    date_of_joining = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    service_status = models.CharField(max_length=200)
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=200)
    project_start_date = models.CharField(max_length=200)
    project_end_date = models.CharField(max_length=200)
    coe_id = models.CharField(max_length=200)
    coe = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'employee'

class Quarterly(models.Model):
    id = models.IntegerField(primary_key=True)
    quarter = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quarterly'

class QuarterlyReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    qms_id = models.CharField(max_length=200, blank=True, null=True)
    employee_id = models.CharField(max_length=200)
    manager_id = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    du_head_id = models.CharField(max_length=200, blank=True, null=True)
    du_head_name = models.CharField(max_length=200, blank=True, null=True)
    coe_head_id = models.CharField(max_length=200, blank=True, null=True)
    coe_head_name = models.CharField(max_length=200, blank=True, null=True)
    employee_service_status = models.CharField(max_length=200, blank=True, null=True)
    manager_hard_skills_comments = models.CharField(max_length=200, blank=True, null=True)
    manager_soft_skills_comments = models.CharField(max_length=200, blank=True, null=True)
    manager_value_addition_comments = models.CharField(max_length=200, blank=True, null=True)
    manager_up_learning_comments = models.CharField(max_length=200, blank=True, null=True)
    manager_hard_skills_ratings = models.CharField(max_length=200, blank=True, null=True)
    manager_soft_skills_ratings = models.CharField(max_length=200, blank=True, null=True)
    manager_value_addition_ratings = models.CharField(max_length=200, blank=True, null=True)
    manager_up_learning_ratings = models.CharField(max_length=200, blank=True, null=True)
    goal = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    hr_form_submit_date = models.DateTimeField(blank=True, null=True)
    review_complete_date = models.DateTimeField(blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    quarterly_rating = models.FloatField(blank=True, null=True)
    manager_form_submit_date = models.DateTimeField(blank=True, null=True)
    workflow_status = models.CharField(max_length=200, blank=True, null=True)
    last_modified_by = models.CharField(max_length=200, blank=True, null=True)
    du_head_complete_date = models.DateTimeField(blank=True, null=True)
    du_hard_skills_ratings = models.FloatField(blank=True, null=True)
    du_soft_skills_ratings = models.FloatField(blank=True, null=True)
    du_value_addition_ratings = models.FloatField(blank=True, null=True)
    du_up_learning_ratings = models.FloatField(blank=True, null=True)
    du_hard_skills_comments = models.CharField(max_length=200, blank=True, null=True)
    du_soft_skills_comments = models.CharField(max_length=200, blank=True, null=True)
    du_value_addition_comments = models.CharField(max_length=200, blank=True, null=True)
    du_up_learning_comments = models.CharField(max_length=200, blank=True, null=True)
    save_for_later = models.BooleanField(blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    manager_email = models.CharField(max_length=200, blank=True, null=True)
    du_head_email = models.CharField(max_length=200, blank=True, null=True)
    employee_email = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quarterly_review'


class SkillsWeightage(models.Model):
    id = models.IntegerField(primary_key=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    weightage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills_weightage'


class WorkflowStatus(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflow_status'


class Year(models.Model):
    year = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'year'


class YearlyReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    yms_id = models.CharField(max_length=200, blank=True, null=True)
    employee_id = models.CharField(max_length=200)
    coe_head_id = models.CharField(max_length=200, blank=True, null=True)
    coe_head_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    employee_email = models.CharField(max_length=200, blank=True, null=True)
    du_head_id = models.CharField(max_length=200, blank=True, null=True)
    du_head_name = models.CharField(max_length=200, blank=True, null=True)
    du_head_email = models.CharField(max_length=200, blank=True, null=True)
    du_head_complete_date = models.DateTimeField(blank=True, null=True)
    manager_id = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    manager_email = models.CharField(max_length=200, blank=True, null=True)
    manager_form_submit_date = models.DateTimeField(blank=True, null=True)
    employee_service_status = models.CharField(max_length=200, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    hr_form_submit_date = models.DateTimeField(blank=True, null=True)
    review_complete_date = models.DateTimeField(blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    workflow_status = models.CharField(max_length=200, blank=True, null=True)
    last_modified_by = models.CharField(max_length=200, blank=True, null=True)
    save_for_later = models.BooleanField(blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    final_rating = models.FloatField(blank=True, null=True)
    employee_self_comments = models.CharField(max_length=200, blank=True, null=True)
    manager_final_comments = models.CharField(max_length=200, blank=True, null=True)
    du_head_final_comments = models.CharField(max_length=200, blank=True, null=True)
    employee_form_submit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yearly_review'
