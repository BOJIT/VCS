/**
    ****************************************************************************
    * @file    VCS.c
    * @author  James Bennion-Pedley
    * @brief   Version control binary block
    ****************************************************************************
    */

#include "VCS.h"

#ifdef __cplusplus
extern "C" {
#endif

/*----------------------------------------------------------------------------*/

#ifndef __VCS_COMPILE_TIME
    #error "VCS macros are not defined!"
#endif /* __VCS_COMPILE_TIME */

#ifndef __VCS_SHORT_HASH
    #error "VCS macros are not defined!"
#endif /* __SHORT_HASH */

#ifndef __VCS_IS_DIRTY
    #error "VCS macros are not defined!"
#endif /* __VCS_IS_DIRTY */

#ifndef __VCS_TAG_DESCRIBE
    #error "VCS macros are not defined!"
#endif /* __VCS_TAG_DESCRIBE */

#ifndef __VCS_LAST_AUTHOR
    #error "VCS macros are not defined!"
#endif /* __VCS_LAST_AUTHOR */

/**
 * @brief Version control block
 */
vcs_t vcs = {
    {0xFF, 0xFE, 0xFD, 0xFC},   /* frame_start */
    1,                          /* schema */
    __VCS_COMPILE_TIME,         /* compile_time */
    __VCS_SHORT_HASH,           /* short_hash */
    __VCS_IS_DIRTY,             /* is_dirty */
    __VCS_TAG_DESCRIBE,         /* tag_describe */
    __VCS_LAST_AUTHOR,          /* author */
    {0x01, 0x02, 0x03, 0x04}    /* frame_end */
};

/*----------------------------------------------------------------------------*/

#ifdef __cplusplus
}
#endif