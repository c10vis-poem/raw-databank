README — vendor-corpora/
Low-Level Systems Architecture: Qualcomm QAIRT/HTP & Google Android NDK/OS
Motto: Xçineribus, in-variis-nunquam-varius, Novi-Æxentis-Copiæ, Vincent
Scope: Definitive Technical Reference for Qualcomm Hexagon NPU Offloading and Google Android Bare-Metal OS IPC.


________________


1. Architectural Mandate: Why This Library Is Decoupled
This corpus stores the immutable low-level engineering references governing how software interacts with mobile silicon. It is strictly partitioned into two specialized domains:


1. Google Android Platform & NDK: Process containerization, POSIX UNIX domain socket file descriptor passing (SCM_RIGHTS), zero-copy anonymous shared memory (ASharedMemory), and Low Memory Killer (LMK) evasion.
2. Qualcomm QAIRT & Hexagon HTP SDK: Hardware tensor pipelines, FastRPC kernel drivers, QNN execution providers, and GenieX on-device GGML Hexagon compilation-free inference.


________________


2. Google Android Systems Architecture & NDK Subsystem
┌────────────────────────────────────────────────────────────────────────┐


│               DECENTRALIZED PROCESS ISOLATION MATRIX                  │


│                      (AndroidManifest.xml)                             │


├───────────────────────────────┬────────────────────────────────────────┤


│ Process Container             │ Engineering Function                   │


├───────────────────────────────┼────────────────────────────────────────┤


│ :orchestrator_daemon          │ Central coordination, WebSocket router │


│ :qairt_engine                 │ Native Qualcomm HTP FastRPC driver     │


│ :llamacpp_engine              │ GGML CPU/OpenCL fallback engine        │


└───────────────────────────────┴────────────────────────────────────────┘
A. NDK Anonymous Shared Memory (ASharedMemory)
Standard Android Binder IPC is capped at 1MB total buffer size across all transactions (TransactionTooLargeException). Passing multi-megabyte tensor weights, KV caches, or raw frame arrays over Binders causes instant runtime crashes.


* The NDK Fix: Memory pools are allocated natively via ASharedMemory_create(name, size).
* Zero-Copy Mapping: The allocating daemon maps the region via mmap(PROT_READ | PROT_WRITE, MAP_SHARED).
* Kernel Protection Enforcement: Before sharing, the daemon invokes ASharedMemory_setProt(fd, PROT_READ) to strip write permissions from child processes, guaranteeing that worker nodes cannot corrupt active model weights.
B. Linux Abstract Namespace UNIX Domain Sockets & SCM_RIGHTS
To bridge the shared memory file descriptor (fd) across isolated Linux processes without writing temporary files to physical flash storage (which degrades UFS 4.0 storage and spikes I/O wait times):


* Abstract Namespace Binding: Sockets are bound with sun_path[0] = '\0', routing traffic entirely within the Linux kernel network namespace.
* Ancillary Message Passing: File descriptors are transmitted using sendmsg() and recvmsg() with POSIX control headers:


struct cmsghdr *cmsg = CMSG_FIRSTHDR(&msg);


cmsg->cmsg_level = SOL_SOCKET;


cmsg->cmsg_type = SCM_RIGHTS; // Direct kernel routing of native file descriptors


cmsg->cmsg_len = CMSG_LEN(sizeof(int));


*((int*)CMSG_DATA(cmsg)) = shared_mem_fd;


* Zero Serialization Overhead: The target engine reconstructs the exact file descriptor handle and maps the identical physical RAM page in microseconds.
C. LMK (Low Memory Killer) Shielding & Priority Promotion
Android's lmkd daemon continuously terminates background processes based on their oom_score_adj values. Heavy LLM runtimes are prime targets for termination:


* Foreground Service Architecture: Daemons invoke startForeground(ID, notification) bound to active notification channels.
* Priority Clamping: This clamps the process priority to FOREGROUND_APP_ADJ (OOM adjustment equivalent to an active user viewport).
* Automated Kernel Resuscitation: Services return START_STICKY, instructing the Android kernel to immediately re-instantiate the daemon if an unexpected thermal drop occurs.
D. Performance Tuning & ADB Loopback Shell Elevation
* ADPF (Android Dynamic Performance Framework): Background engines hook into Android's low-level Performance Hint API and Vendor Game SDKs, unlocking maximum thermal ceilings and pinning thread affinities to high-performance Kryo/Oryon CPU cores.
* Local Wireless ADB Loopback: Operates over 127.0.0.1:5555. Bridges terminal commands to adbd running with UID 2000 (shell) permissions, bypassing app sandboxing to run native background binaries without root.


________________


3. Qualcomm QAIRT, QNN & Hexagon HTP Hardware Architecture
[ GGUF / Serialized Quantized Weights in Flash ]


                        │


                        ▼


[ Linux mmap() / ASharedMemory Physical DMA-BUF ]


                        │


                        ▼ FastRPC IOCTL (/dev/adsprpc-smd)


[ Hexagon v79 HTP NPU Space ] ──► Pinned HTP0 Tensor Engine
A. Snapdragon 8 Elite Hexagon v79 Hardware Specifications
* Throughput: 40+ INT8 TOPs dedicated hardware acceleration.
* FastRPC Kernel Driver: Direct kernel interface via /dev/adsprpc-smd.
* Memory Architecture: Physical contiguous DMA-BUF / ION memory buffers registered with the DSP via remote_register_buf(). The NPU reads token matrices directly from physical RAM with 0% CPU copy tax.
B. Direct On-Device Inference Without Host Compilation (GenieX)
Prior architectures required an x86 Linux computer to run Qualcomm's offline QAIRT GGUF Builder toolchain before pushing binaries via ADB.


* The Modern GenieX Pathway:
   * Any standard HuggingFace GGUF Q4_0 is loaded directly on-device.
   * GenieX hooks into the Qualcomm GGML Hexagon Backend compiled natively for Android.
   * Zero Host Compilation: Eliminates the x86 Linux machine requirement entirely.
* Execution Schedulers:
   * --device hybrid (Default & Fastest): Uses a per-tensor scheduler. Offloads all supported quantized operations (GEMM, activations) to the Hexagon HTP, falling back cleanly to ARM Neon CPU instructions for unsupported layers without crashing. Prefill speeds reach ~90 tok/s, decode ~27 tok/s on Qwen 3.5.
   * --device npu: Pins 100% of graph operations strictly to HTP0 for deterministic, jitter-free execution.
   * --device gpu: Routes operations to Adreno via OpenCL.
   * --device cpu: Pure multi-threaded ARM CPU execution.
C. Multi-Backend Quantization Formats & Context Binary Teardown
* QNN Context Binaries (.bin): Pre-compiled execution graphs built using libQnnHtp.so for Gemma 4 QAT INT4 execution.
* Memory Reclamation & Teardown Protocol: When hot-swapping models, the NPU Manager executes an explicit C-level teardown:
   1. Calls QnnContext_free() to release DSP context handles.
   2. Invokes munmap() on physical DMA-BUF descriptors.
   3. Flushes HTP L2/TCM cache lines via driver ioctl().
   4. Enforces a 500ms quiescence delay to ensure zero lingering locks on /dev/adsprpc-smd before the next model allocates memory.


________________


4. Repository Directory Structure
vendor-corpora/


├── README.md                                # This document (Low-level systems architecture specification)


├── manifest.jsonl                           # Master cryptographic index of all vendor specifications


│


├── qualcomm-qairt-sdk/                      # Qualcomm QAIRT, QNN & Hexagon Reference Core


│   ├── manifest.jsonl                       # Local Qualcomm API index


│   ├── htp-specs/                           # Hexagon v79 HTP hardware limits & tensor schedules


│   ├── fastrpc-drivers/                     # /dev/adsprpc-smd ioctl interfaces & buffer registries


│   ├── qnn-headers/                         # libQnnHtp.so, libQnnSystem.so, and C++ header bindings


│   └── geniex-runtime/                      # GenieX GGML Hexagon backend documentation & run flags


│


└── google-android-platform/                 # Google Android Native Framework Core


    ├── manifest.jsonl                       # Local Android platform index


    ├── asharedmemory-ndk/                   # ASharedMemory_create, mmap, and SCM_RIGHTS socket code


    ├── process-isolation/                   # AndroidManifest.xml :process tags & isolatedProcess rules


    ├── lmk-mitigation/                      # Foreground Service, START_STICKY, and FOREGROUND_APP_ADJ


    ├── adpf-performance/                   # Android Dynamic Performance Framework & Game SDK hints


    └── wireless-adb/                        # adbd TCP loopback on 127.0.0.1:5555 & pairing protocols