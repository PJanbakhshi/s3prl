import os
import torch

from utility.download import _gdriveids_to_filepaths
from upstream.tera.expert import UpstreamExpert as _UpstreamExpert


def tera_local(ckpt, *args, **kwargs):
    """
        The model from local ckpt
            ckpt (str): PATH
    """
    assert os.path.isfile(ckpt)
    return _UpstreamExpert(ckpt, *args, **kwargs)


def tera_gdriveid(ckpt, refresh=False, *args, **kwargs):
    """
        The model from google drive id
            ckpt (str): The unique id in the google drive share link
            refresh (bool): whether to download ckpt/config again if existed
    """
    return tera_local(_gdriveids_to_filepaths(ckpt, refresh=refresh), *args, **kwargs)


def tera(refresh=False, *args, **kwargs):
    """
        The default model
            refresh (bool): whether to download ckpt/config again if existed
    """
    return tera_logMelBase_time_freq_mag_AdamW_b32_1m_960hr(refresh, *args, **kwargs)


##########
# 100 HR #
##########


def tera_logMelBase_time_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '1-JwGlb3JXXnnXqKL9WVtbv34RR0o6BAX'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_freq_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: freq
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '1ZqTQx6vCqSPFbqtDwL-LjKKpoKrga3cz'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_mag_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '1EE5ieH-bsNynD3COYI8_yS8xxSnL4zFp'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_freq_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time + freq
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '1g2RBcl4xxvpDtA7eeSIGgygNrMGMUxu2'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_mag_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time + mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '1eQrzJ138OXqMTQfNEl_rsT1Y_GTMj0mQ'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_freq_mag_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: freq + mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '1IagYPw9IPMS_8-jwBmduorzjuRyxrsyY'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_freq_mag_AdamW_b32_200k_100hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time + freq + mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 200k
        Unlabled Speech: 100hr
    """
    kwargs['ckpt'] = '12gUQ6RHyujPp7ZoSsr3t1xrsySsoxVOd'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


##########
# 960 HR #
##########


def tera_logMelBase_time_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1XTQQBuj9qFHb1MErlu76zb3GeUu3GJ0f'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_AdamW_b32_500k_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time
        Optimizer: AdamW
        Batch size: 32
        Total steps: 500k
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1ZGDeQUoiUapRGuhvUBmJaE-XTyDceCHf'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_freq_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: freq
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1MezF4LHnu-E8ZQF_pN6Jy7rEp8R0PmQu'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_mag_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1DPI3G34_TI0_DwkckDteH5QKx43y1R7u'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_freq_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time + freq
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1ZmsLfRKilrSn11U3vwPl0DVHIul3xmpz'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_mag_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time + mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1Uwlfcmwab8EL-dniBaI7AkVyAEHsLXnm'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_freq_mag_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: freq + mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = ''
    return tera_gdriveid(refresh=refresh, *args, **kwargs)


def tera_logMelBase_time_freq_mag_AdamW_b32_1m_960hr(refresh=False, *args, **kwargs):
    """
        Feature: 80-dim log Mel
        Alteration: time + freq + mag
        Optimizer: AdamW
        Batch size: 32
        Total steps: 1M
        Unlabled Speech: 960hr
    """
    kwargs['ckpt'] = '1AcH73Us51OkYM5NqT-zoNM55w4Gwu5vB'
    return tera_gdriveid(refresh=refresh, *args, **kwargs)