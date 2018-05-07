#
# Copyright (C) 2018 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

model = Model()
i1 = Input("input", "TENSOR_FLOAT32", "{1, 2, 2, 2}")
block = Parameter("block_size", "TENSOR_INT32", "{2}", [2, 2])
paddings = Parameter("paddings", "TENSOR_INT32", "{2, 2}", [0, 0, 0, 0])
output = Output("output", "TENSOR_FLOAT32", "{4, 1, 1, 2}")

model = model.Operation("SPACE_TO_BATCH_ND", i1, block, paddings).To(output)
model = model.RelaxedExecution(True)

# Example 1. Input in operand 0,
input0 = {i1: # input 0
          [1.4, 2.3, 3.2, 4.1, 5.4, 6.3, 7.2, 8.1]}

output0 = {output: # output 0
           [1.4, 2.3, 3.2, 4.1, 5.4, 6.3, 7.2, 8.1]}

# Instantiate an example
Example((input0, output0))
