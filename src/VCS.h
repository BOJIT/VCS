/**
    ****************************************************************************
    * @file    VCS.h
    * @author  James Bennion-Pedley
    * @brief   Exposes version control binary block as a struct so that
    *          variables can be referenced in source
    ****************************************************************************
    */

#ifndef __VCS_H__
#define __VCS_H__

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

/*----------------------------------------------------------------------------*/

/**
 * @brief Version control block structure - typically only one of these
 * is included in the output binary
 */
typedef struct __attribute__ ((packed)) {
    uint8_t frame_start[4];
    uint8_t schema;    /* Version of VCS schema used */
    char compile_time[20];
    char short_hash[10];
    bool is_dirty;
    char tag_describe[20];
    char last_author[20];
    uint8_t frame_end[4];
} vcs_t;

extern const vcs_t vcs;   ///< Actual version control instance

/*----------------------------------------------------------------------------*/

#ifdef __cplusplus
}
#endif

#endif /* __VCS_H__ */