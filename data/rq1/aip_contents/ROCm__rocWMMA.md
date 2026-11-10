### Deliverables ###

rocWMMA has a set of required deliverables for every pull request that are as follows.

1. **Test Integration**:
    - All new functionality introduced to rocWMMA must be accompanied by unit tests. Unit tests should integrate within the existing
    googletest framework and must have good code coverage. Existing unit tests should be used as a guide and are found in ``test/unit``. Be sure to consider
    rocWMMA's support matrix for datatypes, block sizes and architectures.

    - New features that aim to optimize rocWMMA must have benchmark and validation tests, and performance must approach the compute bound limit or
    memory bound limit. These tests should follow the same googletest framework laid out in the rocWMMA GEMM tests found in ``test/gemm``.
    Features that impact the performance of existing rocWMMA kernels must be accompanied with a performance analysis against the pre-existing
    kernels.

2. **API Documentation**:
    - Any new outward facing rocWMMA API functions must be properly documented and included in the [API Reference Guide](https://github.com/ROCm/rocWMMA/blob/develop/docs/api-reference-guide.rst).

3. **Type Support**:
    - All features introduced to rocWMMA must maintain support for the following types:
        - **Supported Datatypes (gfx9)**
            - Native Data Types: int8, f16, f32, f64*
            - Non-Native Data Types: h16 (__half), bf16, f8**, bf8**

        - **Supported Datatypes (gfx11)**
            - Native Data Types: int8, f16
            - Non-Native Data Types: h16, bf16

        - **Supported Datatypes (gfx12)**
            - Native Data Types: int8, f16
            - Non-Native Data Types: h16, bf16, f8**, bf8**

		| *Only on gfx90a, gfx942 & gfx950. |
		|-----------------------------------|

		| **Only on gfx942, gfx950 and gfx12. |
		|-------------------------------------|

    - Support for the other rocWMMA fragment parameters as described in ``library/include/rocwmma/rocwmma.hpp`` must also be maintained.

4. **Licensing**:
    - <mark>All code submitted to rocWMMA must be original, no AI generated code is currently being accepted.</mark>
    - The code you are contributing is your own, and you have the right to license it.
    - No code found under other licenses is permitted.
    - Any submitted code will subsequently be covered under the MIT License.
    - For each new file introduced in your pull request, please include the licensing header:

    ```
    /*******************************************************************************
    *
    * MIT License
    *
    * Copyright (C) 2024 Advanced Micro Devices, Inc. All rights reserved.
    *
    * Permission is hereby granted, free of charge, to any person obtaining a copy
    * of this software and associated documentation files (the "Software"), to deal
    * in the Software without restriction, including without limitation the rights
    * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    * copies of the Software, and to permit persons to whom the Software is
    * furnished to do so, subject to the following conditions:
    *
    * The above copyright notice and this permission notice shall be included in
    * all copies or substantial portions of the Software.
    *
    * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    * SOFTWARE.
    *
    *******************************************************************************/
    ```
