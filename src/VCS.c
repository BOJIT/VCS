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
    {0xFF, 0xFE, 0xFD, 0xFC},       /* frame_start */
    1,                          /* schema */
    "2000-10-31T10:54:59Z",     /* compile_time */
    {0x01, 0x02, 0x03, 0x04}        /* frame_end */
};

/*----------------------------------------------------------------------------*/

#ifdef __cplusplus
}
#endif