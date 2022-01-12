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

/**
 * @brief Version control block
 */
vcs_t vcs = {
    {255, 254, 253, 254},       /* frame_start */
    1,                          /* schema */
    "2000-10-31T10:54:59Z",     /* compile_time */
    {1, 2, 3, 4}                /* frame_end */
};

/*----------------------------------------------------------------------------*/

#ifdef __cplusplus
}
#endif