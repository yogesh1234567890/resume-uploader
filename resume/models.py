from django.db import models

class Resume(models.Model):
    class Meta:
        db_table="tbl_resume"
        verbose_name_plural="Resume"
    resume=models.FileField(upload_to="files",null=True)
