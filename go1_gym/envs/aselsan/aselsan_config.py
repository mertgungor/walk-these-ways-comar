from typing import Union

from params_proto import Meta

from go1_gym.envs.base.legged_robot_config import Cfg


def config_go1(Cnfg: Union[Cfg, Meta]):
    _ = Cnfg.init_state

    _.pos = [0.0, 0.0, 0.34]  # x,y,z [m]
    _.default_joint_angles = {  # = target angles [rad] when action = 0.0
        "comar/abad_1_joint" :  0.1,  # [rad] FL hip
        "comar/abad_2_joint" : -0.1,  # [rad] FR hip
        "comar/abad_3_joint" :  0.1,  # [rad] RL hip
        "comar/abad_4_joint" : -0.1,  # [rad] RR hip

        "comar/hip_1_joint"  :  0.8,  # [rad] FL thigh
        "comar/hip_2_joint"  :  0.8,  # [rad] FR thigh
        "comar/hip_3_joint"  :  1.,   # [rad] RL thigh
        "comar/hip_4_joint"  :  1.,   # [rad] RR thigh

        "comar/knee_1_joint" : -1.5,  # [rad] FL calf
        "comar/knee_2_joint" : -1.5,  # [rad] FR calf
        "comar/knee_3_joint" : -1.5,  # [rad] RL calf
        "comar/knee_4_joint" : -1.5,  # [rad] RR calf   
 
    }

    _ = Cnfg.control
    _.control_type = 'P'
    _.stiffness = {'joint': 20.}  # [N*m/rad]
    _.damping = {'joint': 0.5}  # [N*m*s/rad]
    # action scale: target angle = actionScale * action + defaultAngle
    _.action_scale = 0.25
    _.hip_scale_reduction = 0.5
    # decimation: Number of control action updates @ sim DT per policy DT
    _.decimation = 4

    _ = Cnfg.asset
    _.file = '{MINI_GYM_ROOT_DIR}/resources/robots/aselsan/urdf/comar_a1.urdf'
    _.foot_name = "foot"
    _.penalize_contacts_on = ["hip", "calf"]
    _.terminate_after_contacts_on = ["base"]
    _.self_collisions = 0  # 1 to disable, 0 to enable...bitwise filter
    _.flip_visual_attachments = False
    _.fix_base_link = False

    _ = Cnfg.rewards
    _.soft_dof_pos_limit = 0.9
    _.base_height_target = 0.4

    _ = Cnfg.reward_scales
    _.torques = -0.0001
    _.action_rate = -0.01
    _.dof_pos_limits = -10.0
    _.orientation = -5.
    _.base_height = -30.

    _ = Cnfg.terrain
    _.mesh_type = 'trimesh'
    _.measure_heights = False
    _.terrain_noise_magnitude = 0.0
    _.teleport_robots = True
    _.border_size = 50

    _.terrain_proportions = [0, 0, 0, 0, 0, 0, 0, 0, 1.0]
    _.curriculum = False

    _ = Cnfg.env
    _.num_observations = 42
    _.observe_vel = False
    _.num_envs = 4000

    _ = Cnfg.commands
    _.lin_vel_x = [-1.0, 1.0]
    _.lin_vel_y = [-1.0, 1.0]

    _ = Cnfg.commands
    _.heading_command = False
    _.resampling_time = 10.0
    _.command_curriculum = True
    _.num_lin_vel_bins = 30
    _.num_ang_vel_bins = 30
    _.lin_vel_x = [-0.6, 0.6]
    _.lin_vel_y = [-0.6, 0.6]
    _.ang_vel_yaw = [-1, 1]

    _ = Cnfg.domain_rand
    _.randomize_base_mass = True
    _.added_mass_range = [-1, 3]
    _.push_robots = False
    _.max_push_vel_xy = 0.5
    _.randomize_friction = True
    _.friction_range = [0.05, 4.5]
    _.randomize_restitution = True
    _.restitution_range = [0.0, 1.0]
    _.restitution = 0.5  # default terrain restitution
    _.randomize_com_displacement = True
    _.com_displacement_range = [-0.1, 0.1]
    _.randomize_motor_strength = True
    _.motor_strength_range = [0.9, 1.1]
    _.randomize_Kp_factor = False
    _.Kp_factor_range = [0.8, 1.3]
    _.randomize_Kd_factor = False
    _.Kd_factor_range = [0.5, 1.5]
    _.rand_interval_s = 6
