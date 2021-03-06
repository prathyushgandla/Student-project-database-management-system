# Generated by Django 3.2 on 2022-01-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeproject', '0005_alter_project_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='academic',
            new_name='Academic',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='file',
            new_name='File',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='group_size',
            new_name='GroupSize',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='guide',
            new_name='GuideName',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_type',
            new_name='ProjectType',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='research',
            new_name='Research',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='software',
            new_name='Software',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_name1',
            new_name='StudentName1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_name2',
            new_name='StudentName2',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_name3',
            new_name='StudentName3',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_name4',
            new_name='StudentName4',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_name5',
            new_name='StudentName5',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_rollno1',
            new_name='StudentRollno1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_rollno2',
            new_name='StudentRollno2',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_rollno3',
            new_name='StudentRollno3',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_rollno4',
            new_name='StudentRollno4',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='stu_rollno5',
            new_name='StudentRollno5',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='Title',
        ),
        migrations.AddField(
            model_name='project',
            name='GuideEmail',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='GuideNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentEmail1',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentEmail2',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentEmail3',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentEmail4',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentEmail5',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentMobileNumber1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentMobileNumber2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentMobileNumber3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentMobileNumber4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='StudentMobileNumber5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
