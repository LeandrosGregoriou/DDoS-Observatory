/* config.h.  Generated from config.h.in by configure.  */
/* config.h.in.  Generated from configure.ac by autoheader.  */

/* Monitor Name */
#define BGPCORSARO_MONITOR_NAME leandros-VirtualBox

/* Broker URL */
#define BGPSTREAM_DS_BROKER_URL "https://bgpstream.caida.org/broker"

/* CSV file listing the MRT data to read */
#define BGPSTREAM_DS_CSVFILE_CSV_FILE "not-set"

/* RIB MRT file to read */
#define BGPSTREAM_DS_SINGLEFILE_RIB_FILE "not-set"

/* Updates MRT to read */
#define BGPSTREAM_DS_SINGLEFILE_UPDATE_FILE "not-set"

/* SQLite database */
/* #undef BGPSTREAM_DS_SQLITE_DB_FILE */

/* bgpstream major version */
#define BGPSTREAM_MAJOR_VERSION 1

/* bgpstream mid version */
#define BGPSTREAM_MID_VERSION 2

/* bgpstream minor version */
#define BGPSTREAM_MINOR_VERSION 1

/* Debug Mode */
/* #undef DEBUG */

/* plugins to call the init macro for in bgpcorsaro_plugin.c */
#define ED_PLUGIN_INIT_ALL_ENABLED PLUGIN_INIT_ADD(bgpcorsaro_pfxmonitor);PLUGIN_INIT_ADD(bgpcorsaro_pacifier);PLUGIN_INIT_ADD(bgpcorsaro_asmonitor);

/* Define to 1 if you have the <arpa/inet.h> header file. */
#define HAVE_ARPA_INET_H 1

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Define to 1 if you have the `gettimeofday' function. */
#define HAVE_GETTIMEOFDAY 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* Define to 1 if you have the `sqlite3' library (-lsqlite3). */
/* #undef HAVE_LIBSQLITE3 */

/* Define to 1 if you have the <limits.h> header file. */
#define HAVE_LIMITS_H 1

/* Define to 1 if your system has a GNU libc compatible `malloc' function, and
   to 0 otherwise. */
#define HAVE_MALLOC 1

/* Define to 1 if you have the <math.h> header file. */
#define HAVE_MATH_H 1

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* Define to 1 if you have the `memset' function. */
#define HAVE_MEMSET 1

/* Define if you have POSIX threads libraries and header files. */
#define HAVE_PTHREAD 1

/* Have PTHREAD_PRIO_INHERIT. */
#define HAVE_PTHREAD_PRIO_INHERIT 1

/* Define to 1 if your system has a GNU libc compatible `realloc' function,
   and to 0 otherwise. */
#define HAVE_REALLOC 1

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the `strdup' function. */
#define HAVE_STRDUP 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the `strlcpy' function. */
/* #undef HAVE_STRLCPY */

/* Define to 1 if you have the `strsep' function. */
#define HAVE_STRSEP 1

/* Define to 1 if you have the `strstr' function. */
#define HAVE_STRSTR 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/time.h> header file. */
#define HAVE_SYS_TIME_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <time.h> header file. */
#define HAVE_TIME_H 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Define to 1 if you have the `vasprintf' function. */
#define HAVE_VASPRINTF 1

/* libbgpstream major version */
#define LIBBGPSTREAM_MAJOR_VERSION 2

/* libbgpstream mid version */
#define LIBBGPSTREAM_MID_VERSION 0

/* libbgpstream minor version */
#define LIBBGPSTREAM_MINOR_VERSION 0

/* Define to the sub-directory where libtool stores uninstalled libraries. */
#define LT_OBJDIR ".libs/"

/* Define to 1 if assertions should be disabled. */
/* #undef NDEBUG */

/* Name of package */
#define PACKAGE "bgpstream"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT "bgpstream-info@caida.org"

/* Define to the full name of this package. */
#define PACKAGE_NAME "bgpstream"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "bgpstream 1.2.1"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "bgpstream"

/* Define to the home page for this package. */
#define PACKAGE_URL ""

/* Define to the version of this package. */
#define PACKAGE_VERSION "1.2.1"

/* Define to necessary symbol if this constant uses a non-standard name on
   your system. */
/* #undef PTHREAD_CREATE_JOINABLE */

/* Define to necessary func name if pthread_yield or pthread_yield_np do not
   exist on your system */
#define PTHREAD_YIELD_FUNC pthread_yield

/* Define to 1 if you have the ANSI C header files. */
#define STDC_HEADERS 1

/* Version number of package */
#define VERSION "1.2.1"

/* Enable broker debugging output */
/* #undef WITH_BROKER_DEBUG */

/* Building with broker */
#define WITH_DATA_INTERFACE_BROKER 1

/* Building with csvfile */
#define WITH_DATA_INTERFACE_CSVFILE 1

/* Building with singlefile */
#define WITH_DATA_INTERFACE_SINGLEFILE 1

/* Building with sqlite */
/* #undef WITH_DATA_INTERFACE_SQLITE */

/* Building with asmonitor */
#define WITH_PLUGIN_ASMONITOR 1

/* Building with pacifier */
#define WITH_PLUGIN_PACIFIER 1

/* Building with pfxmonitor */
#define WITH_PLUGIN_PFXMONITOR 1

/* Monitor plugin timing */
/* #undef WITH_PLUGIN_TIMING */

/* Enable large inode numbers on Mac OS X 10.5.  */
#ifndef _DARWIN_USE_64_BIT_INODE
# define _DARWIN_USE_64_BIT_INODE 1
#endif

/* Number of bits in a file offset, on hosts where this is settable. */
/* #undef _FILE_OFFSET_BITS */

/* Enable GNU extensions on systems that have them.  */
#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif

/* Define for large files, on AIX-style hosts. */
/* #undef _LARGE_FILES */

/* Define for Solaris 2.5.1 so the uint32_t typedef from <sys/synch.h>,
   <pthread.h>, or <semaphore.h> is not used. If the typedef were allowed, the
   #define below would cause a syntax error. */
/* #undef _UINT32_T */

/* Define for Solaris 2.5.1 so the uint64_t typedef from <sys/synch.h>,
   <pthread.h>, or <semaphore.h> is not used. If the typedef were allowed, the
   #define below would cause a syntax error. */
/* #undef _UINT64_T */

/* Define for Solaris 2.5.1 so the uint8_t typedef from <sys/synch.h>,
   <pthread.h>, or <semaphore.h> is not used. If the typedef were allowed, the
   #define below would cause a syntax error. */
/* #undef _UINT8_T */

/* Define to rpl_malloc if the replacement function should be used. */
/* #undef malloc */

/* Define to rpl_realloc if the replacement function should be used. */
/* #undef realloc */

/* Define to `unsigned int' if <sys/types.h> does not define. */
/* #undef size_t */

/* Define to the type of an unsigned integer type of width exactly 16 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint16_t */

/* Define to the type of an unsigned integer type of width exactly 32 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint32_t */

/* Define to the type of an unsigned integer type of width exactly 64 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint64_t */

/* Define to the type of an unsigned integer type of width exactly 8 bits if
   such a type exists and the standard includes do not define it. */
/* #undef uint8_t */
