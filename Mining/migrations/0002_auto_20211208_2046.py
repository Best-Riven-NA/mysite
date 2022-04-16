# Generated by Django 3.2.9 on 2021-12-08 20:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Mining', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_id', models.IntegerField(default=0, verbose_name='申请编号')),
                ('apply_person', models.CharField(max_length=24, verbose_name='申请人')),
                ('pai_num', models.IntegerField(default=0, verbose_name='钻孔排号')),
                ('kong_num', models.CharField(max_length=24, verbose_name='孔号')),
                ('pian_angle', models.FloatField(default=0.0, verbose_name='偏角')),
                ('yang_angle', models.FloatField(default=0.0, verbose_name='仰角')),
                ('kong_length', models.FloatField(default=0.0, verbose_name='孔深')),
                ('yan_kong_length', models.FloatField(default=0.0, verbose_name='岩孔长度')),
                ('mei_duan_length', models.FloatField(default=0.0, verbose_name='煤段长度')),
                ('flush_mei_count', models.FloatField(default=0.0, verbose_name='冲煤量')),
                ('apply_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='申请时间')),
                ('apply_inform', models.CharField(max_length=1024, verbose_name='申请信息')),
                ('apply_status', models.CharField(max_length=16, verbose_name='申请状态')),
                ('reback_msg', models.CharField(max_length=64, verbose_name='反馈信息')),
            ],
            options={
                'verbose_name': '申请记录表',
                'verbose_name_plural': '申请记录表',
                'db_table': 'apply_record',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '公司管理', 'verbose_name_plural': '公司管理'},
        ),
        migrations.AlterModelOptions(
            name='di_ban_hang_xiuzheng_ding_ban',
            options={'verbose_name': '底板巷道顶板坐标表', 'verbose_name_plural': '底板巷道顶板坐标表'},
        ),
        migrations.AlterModelOptions(
            name='di_ban_tunnel_tun_kuo',
            options={'verbose_name': '底板巷轮廓坐标表', 'verbose_name_plural': '底板巷轮廓坐标表'},
        ),
        migrations.AlterModelOptions(
            name='mine',
            options={'verbose_name': '煤矿管理', 'verbose_name_plural': '煤矿管理'},
        ),
        migrations.AlterModelOptions(
            name='ping_mian_zuo_biao_kong_zhi',
            options={'verbose_name': '处理后的坐标轴(上部分)', 'verbose_name_plural': '处理后的坐标轴(上部分)'},
        ),
        migrations.AlterModelOptions(
            name='ping_mian_zuo_biao_kong_zhi_xia',
            options={'verbose_name': '处理后的坐标轴(下部分)', 'verbose_name_plural': '处理后的坐标轴(下部分)'},
        ),
        migrations.AlterModelOptions(
            name='ping_zhe',
            options={'verbose_name': '平面图控制范围折线段坐标表', 'verbose_name_plural': '平面图控制范围折线段坐标表'},
        ),
        migrations.AlterModelOptions(
            name='pou_zhe_xian',
            options={'verbose_name': '剖面图煤巷折线段坐标', 'verbose_name_plural': '剖面图煤巷折线段坐标'},
        ),
        migrations.AlterModelOptions(
            name='rock_pillar_thickness',
            options={'verbose_name': '岩柱厚度表', 'verbose_name_plural': '岩柱厚度表'},
        ),
        migrations.AlterModelOptions(
            name='row',
            options={'verbose_name': '排管理', 'verbose_name_plural': '排管理'},
        ),
        migrations.AlterModelOptions(
            name='tunnel',
            options={'verbose_name': '巷道管理', 'verbose_name_plural': '巷道管理'},
        ),
        migrations.AlterModelOptions(
            name='tunnel_coal_dip_angle',
            options={'verbose_name': '巷道煤层倾角表', 'verbose_name_plural': '巷道煤层倾角表'},
        ),
        migrations.AlterModelOptions(
            name='user_group',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
        migrations.AlterModelOptions(
            name='work_face',
            options={'verbose_name': '工作面管理', 'verbose_name_plural': '工作面管理'},
        ),
        migrations.AlterModelOptions(
            name='xie_ya_fan_wei',
            options={'verbose_name': '泄压范围坐标', 'verbose_name_plural': '泄压范围坐标'},
        ),
        migrations.AlterModelOptions(
            name='xiu_zheng_hou_meiceng_di_ban',
            options={'verbose_name': '修正后煤层底板坐标表', 'verbose_name_plural': '修正后煤层底板坐标表'},
        ),
        migrations.AlterModelOptions(
            name='xiu_zheng_mei_ceng_ding_ban',
            options={'verbose_name': '修正后煤层顶板坐标表', 'verbose_name_plural': '修正后煤层顶板坐标表'},
        ),
        migrations.AlterField(
            model_name='company',
            name='c_name',
            field=models.CharField(max_length=30, verbose_name='公司名称'),
        ),
        migrations.AlterField(
            model_name='di_ban_hang_xiuzheng_ding_ban',
            name='di_I_x',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='底板巷道顶板坐标X'),
        ),
        migrations.AlterField(
            model_name='di_ban_hang_xiuzheng_ding_ban',
            name='di_J_Z',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='底板巷道顶板坐标Y'),
        ),
        migrations.AlterField(
            model_name='di_ban_hang_xiuzheng_ding_ban',
            name='di_ban_hang_tunnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.tunnel', verbose_name='巷道号'),
        ),
        migrations.AlterField(
            model_name='hole_design',
            name='design_hole_height',
            field=models.FloatField(blank=True, default=1.2, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mine',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.company', verbose_name='所属公司'),
        ),
        migrations.AlterField(
            model_name='mine',
            name='m_name',
            field=models.CharField(max_length=30, verbose_name='煤矿名称'),
        ),
        migrations.AlterField(
            model_name='ping_mian_zuo_biao_kong_zhi',
            name='Chu_li_shang_X',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='X坐标'),
        ),
        migrations.AlterField(
            model_name='ping_mian_zuo_biao_kong_zhi',
            name='Chu_li_shang_Y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='Y坐标'),
        ),
        migrations.AlterField(
            model_name='ping_mian_zuo_biao_kong_zhi_xia',
            name='Chu_li_xia_X',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='X坐标'),
        ),
        migrations.AlterField(
            model_name='ping_mian_zuo_biao_kong_zhi_xia',
            name='Chu_li_xia_Y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='Y坐标'),
        ),
        migrations.AlterField(
            model_name='ping_zhe',
            name='biao_ji',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='标记'),
        ),
        migrations.AlterField(
            model_name='ping_zhe',
            name='zhe_hole_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='孔号'),
        ),
        migrations.AlterField(
            model_name='ping_zhe',
            name='zhe_row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.row', verbose_name='排号'),
        ),
        migrations.AlterField(
            model_name='ping_zhe',
            name='zhe_x',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='平面图控制范围折线段坐标x'),
        ),
        migrations.AlterField(
            model_name='ping_zhe',
            name='zhe_y',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='平面图控制范围折线段坐标y'),
        ),
        migrations.AlterField(
            model_name='ping_zhe',
            name='zhe_z',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='平面图控制范围折线段坐标z'),
        ),
        migrations.AlterField(
            model_name='pou_zhe_xian',
            name='pou_zhe_hole_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='孔号'),
        ),
        migrations.AlterField(
            model_name='pou_zhe_xian',
            name='pou_zhe_row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.row', verbose_name='排'),
        ),
        migrations.AlterField(
            model_name='pou_zhe_xian',
            name='pou_zhe_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='剖面图煤巷折线段X坐标'),
        ),
        migrations.AlterField(
            model_name='pou_zhe_xian',
            name='pou_zhe_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='剖面图煤巷折线段Y坐标'),
        ),
        migrations.AlterField(
            model_name='pou_zhe_xian',
            name='pou_zhe_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='剖面图煤巷折线段Z坐标'),
        ),
        migrations.AlterField(
            model_name='rock_pillar_thickness',
            name='thickness',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='岩柱厚度'),
        ),
        migrations.AlterField(
            model_name='rock_pillar_thickness',
            name='thickness_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='岩柱厚度所对应的x坐标点'),
        ),
        migrations.AlterField(
            model_name='rock_pillar_thickness',
            name='tunnel_rock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.tunnel', verbose_name='巷道号'),
        ),
        migrations.AlterField(
            model_name='row',
            name='coal_seam_thickness',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤层厚度'),
        ),
        migrations.AlterField(
            model_name='row',
            name='current_tunnel_depth',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='当前排的巷道深度'),
        ),
        migrations.AlterField(
            model_name='row',
            name='left_number',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='左侧最新孔号'),
        ),
        migrations.AlterField(
            model_name='row',
            name='mei_qing_jiao',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='单排煤层倾角'),
        ),
        migrations.AlterField(
            model_name='row',
            name='pillar_thickness',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='岩柱厚度'),
        ),
        migrations.AlterField(
            model_name='row',
            name='right_number',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='右侧最新孔号'),
        ),
        migrations.AlterField(
            model_name='row',
            name='row_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='排号'),
        ),
        migrations.AlterField(
            model_name='row',
            name='row_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='排x坐标'),
        ),
        migrations.AlterField(
            model_name='row',
            name='row_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='排y坐标'),
        ),
        migrations.AlterField(
            model_name='row',
            name='row_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='排z坐标'),
        ),
        migrations.AlterField(
            model_name='row',
            name='tunnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.tunnel', verbose_name='所属巷道'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='arch_radius',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='拱形半径'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_hang',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷宽度'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_hang_hight',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷高度'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_midline_mine_ceil_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷中心线煤层顶板起止及折线点坐标x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_midline_mine_ceil_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷中心线煤层顶板起止及折线点坐标y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_midline_mine_ceil_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷中心线煤层顶板起止及折线点坐标z'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_midline_mine_floor_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷中心线煤层底板起止及折线点坐标x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_midline_mine_floor_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷中心线煤层底板起止及折线点坐标y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_midline_mine_floor_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷中心线煤层底板起止及折线点坐标z'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_qi_dian_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷底板中心线起点坐标x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_qi_dian_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷底板中心线起坐标y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_qi_dian_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷底板中心线起点坐标z设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_zhong_dian_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷底板中心线终点坐标x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_zhong_dian_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷底板中心线终点坐标y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='di_ban_tunnel_zhong_dian_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='底板巷底板中心线终点坐标z  设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='down_control_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='下部控制范围x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='down_control_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='下部控制范围y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='down_control_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='下部控制范围Z设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='hole_height',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='开孔高度'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='is_mine_ceil_tunnel_midline_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='被掩护煤巷顶板中心线起止及折线点坐标x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='is_mine_ceil_tunnel_midline_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='被掩护煤巷顶板中心线起止及折线点坐标y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='is_mine_ceil_tunnel_midline_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='被掩护煤巷顶板中心线起止及折线点坐标z'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='left_control_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='左侧控制范围x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='left_control_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='左侧控制范围y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='left_control_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='左侧控制范围z设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='mei_ceng_qing_jiao',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤层倾角'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='mine_hight',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤巷高度'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='mine_width',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤巷宽度'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='release_press_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='泄压范围坐标x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='release_press_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='泄压范围坐标y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='release_press_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='泄压范围坐标z设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='right_control_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='右侧控制范围x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='right_control_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='右侧控制范围y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='right_control_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='右侧控制范围z设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='tunnel_actual_row_gap',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='巷道实际排间距'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='tunnel_first_hole_number',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='首个钻孔号'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='tunnel_length',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='巷道长'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='tunnel_name',
            field=models.CharField(max_length=30, verbose_name='巷道名'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='tunnel_row_dig_hole_id',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='巷道排钻孔编号'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='tunnel_row_numebers',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='巷道总排数'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='up_control_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='上部控制范围x'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='up_control_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='上部控制范围y'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='up_control_z',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='上部控制范围z，设置为空'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='work_face',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.work_face', verbose_name='所属工作面'),
        ),
        migrations.AlterField(
            model_name='tunnel',
            name='zuan_kong_chui_ju',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='钻孔垂距'),
        ),
        migrations.AlterField(
            model_name='user_group',
            name='username',
            field=models.CharField(max_length=12, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user_group',
            name='userpwd',
            field=models.CharField(max_length=20, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='user_group',
            name='usertype',
            field=models.CharField(choices=[('0', 'worker'), ('1', 'operator'), ('2', 'superadmin')], default='0', max_length=20, verbose_name='用户身份类别'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='borehole_segmentation_standard1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='煤孔分割标准1'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='borehole_segmentation_standard2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='煤孔分割标准2'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='change_of_coal_rock',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='煤岩变化'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='chong_mei_standard',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='冲煤标准'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='chuan_ding_length',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='穿顶长度'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='coal_ultra_thick_divided',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤厚超大划分'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='control_range_of_final_hole_to_meet',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='终孔见煤控制范围'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='distance_of_coal_rock_tunnel',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤岩巷间距'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='down_tunnel_tunnel',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='下部底板巷与下巷内错距离'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='drainage_radius',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='抽采半径'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='drivage_distance',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='设计掘进间距'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='mine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.mine', verbose_name='所属煤矿'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='odd_even_column_distance',
            field=models.FloatField(blank=True, default=3, max_length=10, null=True, verbose_name='设计奇偶列间距'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='over_flush_coefficient',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='超冲系数'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='qie_yan_qie',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='切眼底板巷与切眼巷道内错距离'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='recovery_distance',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='设计回采间距'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='thickness_of_pinch_coal',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='尖灭煤厚'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='up_tunnel_up',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='上部底板巷上巷内错距离'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='volume_weight_of_coal',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤体容量'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='w_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='工作面的名字'),
        ),
        migrations.AlterField(
            model_name='work_face',
            name='with_of_coal_roadway',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='煤巷宽度'),
        ),
        migrations.AlterField(
            model_name='xie_ya_fan_wei',
            name='Xie_ya_x',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='X坐标'),
        ),
        migrations.AlterField(
            model_name='xie_ya_fan_wei',
            name='Xie_ya_y',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='Y坐标'),
        ),
        migrations.AlterField(
            model_name='xiu_zheng_hou_meiceng_di_ban',
            name='xiu_zheng_hou_tunnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.tunnel', verbose_name='巷道号'),
        ),
        migrations.AlterField(
            model_name='xiu_zheng_hou_meiceng_di_ban',
            name='xiu_zheng_x',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='修正后煤层底板坐标X'),
        ),
        migrations.AlterField(
            model_name='xiu_zheng_hou_meiceng_di_ban',
            name='xiu_zheng_z',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='修正后煤层底板坐标Z'),
        ),
        migrations.AlterField(
            model_name='xiu_zheng_mei_ceng_ding_ban',
            name='Xiu_x',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='修正X坐标'),
        ),
        migrations.AlterField(
            model_name='xiu_zheng_mei_ceng_ding_ban',
            name='xiu_tunnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mining.tunnel', verbose_name='巷道号'),
        ),
        migrations.AlterField(
            model_name='xiu_zheng_mei_ceng_ding_ban',
            name='xiu_z',
            field=models.FloatField(blank=True, max_length=30, null=True, verbose_name='修正Y坐标'),
        ),
    ]